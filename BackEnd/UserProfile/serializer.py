from rest_framework import serializers
from .models import Profile, PersonalData, EducationalData, ProfessionalData

class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = ['age', 'experience_years', 'phone', 'freeSpace']
        
class ProfessionalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalData
        fields = ['company', 'role', 'timeworked', 'actualwork']

class EducationalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalData
        fields = ['certification', 'year', 'file']
        
class ProfileSerializer(serializers.ModelSerializer):
    personal_data = PersonalDataSerializer(write_only=True, required=True)
    professional_data = ProfessionalDataSerializer(write_only=True, many=True, required=False)
    educational_data = EducationalDataSerializer(write_only=True, many=True, required=False)
    
    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'name', 'picture', 'banner',
            'personal_data', 'professional_data', 'educational_data'
        ]
        
    def validate(self, data):
        if 'personal_data' not in data:
            raise serializers.ValidationError({
                "personal_data": "Los datos personales son obligatorios"
            })
        return data
        
    def create(self, validated_data):
        personal_data = validated_data.pop('personal_data')
        professional_data = validated_data.pop('professional_data', [])
        educational_data = validated_data.pop('educational_data', [])
        
        profile = Profile.objects.create(**validated_data)
        
        PersonalData.objects.create(profile=profile, **personal_data)
        
        for prof_data in professional_data:
            ProfessionalData.objects.create(profile=profile, **prof_data)
        
        for edu_data in educational_data:
            EducationalData.objects.create(profile=profile, **edu_data)
        
        return profile
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr not in ['personal_data', 'professional_data', 'educational_data']:
                setattr(instance, attr, value)
        instance.save()
        
        if 'personal_data' in validated_data:
            personal_data = validated_data.get('personal_data')
            personal_data_instance, _ = PersonalData.objects.get_or_create(profile=instance)
            for attr, value in personal_data.items():
                setattr(personal_data_instance, attr, value)
            personal_data_instance.save()
        
        if 'professional_data' in validated_data:
            for prof_data in validated_data.get('professional_data', []):
                if 'id' in prof_data:
                    prof_id = prof_data.pop('id')
                    ProfessionalData.objects.filter(
                        id = prof_id,
                        profile = instance
                    ).update(**prof_data) 
                else:
                    ProfessionalData.objects.create(profile=instance, **prof_data)
        
        if 'educational_data' in validated_data:
            for edu_data in validated_data.get('educational_data', []):
                if 'id' in edu_data:
                    edu_id = edu_data.pop('id')
                    EducationalData.objects.filter(
                        id = edu_id,
                        profile = instance
                    ).update(**edu_data)
                else:
                    EducationalData.objects.create(profile=instance, **edu_data)
        
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        personal_data = PersonalData.objects.get(profile=instance)
        representation['personal_data'] = PersonalDataSerializer(personal_data).data
        
        professional_data = instance.professional_data.all()
        representation['professional_data'] = ProfessionalDataSerializer(professional_data, many=True).data
        
        educational_data = instance.educational_data.all()
        representation['educational_data'] = EducationalDataSerializer(educational_data, many=True).data
        
        if instance.picture:
            representation['picture'] = instance.picture.url if instance.picture else None
        if instance.banner:
            representation['banner'] = instance.banner.url if instance.banner else None
        
        return representation 