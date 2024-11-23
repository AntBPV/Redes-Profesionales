import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Profile, PersonalData, ProfessionalData, EducationalData

User = get_user_model()

class test_user_profile(TestCase):
    def setUp(self):
        self.profile = Profile.objects.create(
            user = None,
            name = 'profile test',
            picture = '',
            banner = ''
        )
        self.personal_data = PersonalData.objects.create(
            profile = self.profile,
            age = 0,
            experience_years = 0,
            phone = '1111',
            freeSpace = 'personal data test'
        )
        self.professional_data = ProfessionalData.objects.create(
            profile = self.profile,
            company = 'mock company',
            role = 'mock role',
            timeworked = 'mock time',
            actualwork = False
        )
        self.educational_data = EducationalData.objects.create(
            profile = self.profile,
            certification = 'mock certification',
            file = ''
        )
        
    def tearDown(self):
        pass
    
    def test_view_profile_list(self):
        url = reverse('profile-list')
        response = self.client.get(url)
        data = json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data),0)
    
    def test_view_profile_detail(self):
        url = reverse('profile-detail', args=[self.profile.id])
        response = self.client.get(url)
        data = json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], self.profile.id)
        
    ## FIXME: 400 Bad request on these tests
    ## Separator: ----------------------------------------------------------
    def test_view_profile_create(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        data = {
            "user": user.id,
            "name": "post test",
            "picture": "",
            "banner": "",
            "personal_data": {
                "age": 0,
                "experience_years": 0,
                "phone": "2222",
                "freespace": "Post test"
            }
        }
        url = reverse('profile-list')
        response = self.client.post(url, data, format='json')
        data = json.loads(response.content.decode('utf-8'))
        
        self.assertIn(response.status_code, [200,201])
        
    def test_view_profile_update(self):
        myProfile = Profile.objects.create(
            user = None,
            name = 'profile test',
            picture = '',
            banner = ''
        )
        valid_profile = {
            'name': 'profile updated'
        }
        url = reverse('profile-detail', args=[myProfile.id])
        valid_profile_json = json.dumps(valid_profile)
        response = self.client.put(url, valid_profile_json, content_type='application/json')
        self.assertIn(response.status_code, [200,201])
        
    ## End of separator: ---------------------------------------------------
    
    def test_view_profile_delete(self):
        myProfile = Profile.objects.create(
            user = None,
            name = 'profile test',
            picture = '',
            banner = ''
        )
        url = reverse('profile-detail', args=[myProfile.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)