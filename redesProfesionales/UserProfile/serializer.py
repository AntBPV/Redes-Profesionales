from rest_framework import serializers
from .models import Profile, PersonalData, EducationalData, ProfessionalData

class PersonalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalData
        fields = '__all__'

class EducationalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalData
        fields = '__all__'

class ProfessionalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalData
        fields = '__all__'
        
class ProfileSerializer(serializers.ModelSerializer):
    personal_data = PersonalDataSerializer(write_only=True)
    professional_data = ProfessionalDataSerializer(write_only=True)
    educational_data = EducationalDataSerializer(write_only=True)
    
    class Meta:
        model = Profile
        fields = ['id','name', 'personal_data', 'professional_data', 'educational_data', 'picture', 'banner']
        
    def create(self, validated_data):
        personal_data_data = validated_data.pop('personal_data')
        personal_data = PersonalData.objects.create(**personal_data_data)
        
        educational_data_data = validated_data.pop('educational_data')
        educational_data = EducationalData.objects.create(**educational_data_data)
        
        professional_data_data = validated_data.pop('professional_data')
        professional_data = ProfessionalData.objects.create(**professional_data_data)
        
        profile = Profile.objects.create(
            personal_data=personal_data,
            educational_data=educational_data,
            professional_data=professional_data,
            **validated_data
        )
        return profile
    
    def update(self, instance, validated_data):
        personal_data_data = validated_data.pop('personal_data')
        personal_data = instance.personal_data
        professional_data_data = validated_data.pop('professional_data')
        professional_data = instance.professional_data
        educational_data_data = validated_data.pop('educational_data')
        educational_data = instance.educational_data
        
        for attr, value in personal_data_data.items():
            setattr(personal_data, attr, value)
        personal_data.save()
        
        for attr, value in professional_data_data.items():
            setattr(professional_data, attr, value)
        professional_data.save()
        
        for attr, value in educational_data_data.items():
            setattr(educational_data, attr, value)
        educational_data.save()
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['personal_data'] = PersonalDataSerializer(instance.personal_data).data
        representation['professional_data'] = ProfessionalDataSerializer(instance.professional_data).data
        representation['educational_data'] = EducationalDataSerializer(instance.educational_data).data
        return representation