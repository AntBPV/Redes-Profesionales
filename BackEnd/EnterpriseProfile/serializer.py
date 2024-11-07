from rest_framework import serializers
from .models import EnterpriseProfile, CompanyData

class CompanyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyData
        fields = ['address', 'foundationDate', 'workers', 'field']

class EnterpriseProfileSerializer(serializers.ModelSerializer):
    company_data = CompanyDataSerializer(write_only=True, required=True)
    
    class Meta:
        model = EnterpriseProfile
        fields = [
            'user', 'name', 'backstory', 'picture',
            'banner', 'company_data'
        ]
    
    def validate(self, data):
        if 'company_data' not in data:
            raise serializers.ValidationError({
                "company_data": "Los datos de la empresa son obligatorios"
            })
        return data
    
    def create(self, validated_data):
        company_data = validated_data.pop('company_data')
        
        profile = EnterpriseProfile.objects.create(**validated_data)
        
        CompanyData.objects.create(profile=profile, **company_data)
        
        return profile
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr not in ['company_data']:
                setattr(instance, attr, value)
        instance.save()
        
        if 'company_data' in validated_data:
            company_data = validated_data.get('company_data')
            company_data_instance, _ = CompanyData.objects.get_or_create(profile = instance)
            for attr, value in company_data.items():
                setattr(company_data_instance, attr, value)
            company_data_instance.save()
            
        return instance
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        company_data = CompanyData.objects.get(profile = instance)
        representation['company_data'] = CompanyDataSerializer(company_data).data
        
        if instance.picture:
            representation['picture'] = instance.picture.url if instance.picture else None
        if instance.banner:
            representation['banner'] = instance.banner.url if instance.banner else None
        
        return representation