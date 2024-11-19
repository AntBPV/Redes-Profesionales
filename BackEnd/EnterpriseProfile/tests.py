import json
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import EnterpriseProfile, CompanyData

User = get_user_model()

class TestEnterpriseProfile(TestCase):
    def setUp(self):
        self.enterpriseProfile = EnterpriseProfile.objects.create(
            user = None,
            name = 'profile test',
            backstory = 'backstory test',
            picture = '',
            banner = ''
        )
        self.company_data = CompanyData.objects.create(
            enterprise = self.enterpriseProfile,
            address = 'address test',
            foundationDate = 'foundationDate test',
            workers = 0,
            field = 'field test'
        )
    
    def tearDown(self):
        pass
    
    def test_view_enterprise_profile_list(self):
        url = reverse('enterprise-profile-list')
        response = self.client.get(url)
        data = json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data), 0)
        
    def test_view_enterprise_profile_detail(self):
        url = reverse('enterprise-profile-detail', args=[self.enterpriseProfile.id])
        response = self.client.get(url)
        data = json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], self.enterpriseProfile.id)
        
    def test_view_enterprise_profile_create(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        data = {
            "user": user.id,
            "name": "profile test",
            "backstory": "backstory test",
            "picture": "",
            "banner": "",
            "company_data": {
                "address": "address test",
                "foundationDate": "foundationDate test",
                "workers": 0,
                "field": "field test"
            }
        }
        url = reverse('enterprise-profile-list')
        response = self.client.post(url, data, format='json')
        data = json.loads(response.content.decode('utf-8'))
        
        self.assertIn(response.status_code, [200,201])
    
    def test_view_enterprise_profile_update(self):
        myProfile = EnterpriseProfile.objects.create(
            user = None,
            name = 'profile test',
            backstory = 'backstory test',
            picture = '',
            banner = ''
        )
        valid_profile = {
            'name': 'profile updated'
        }
        url = reverse('enterprise-profile-detail', args=[myProfile.id])
        valid_profile_json = json.dumps(valid_profile)
        response = self.client.put(url, valid_profile_json, content_type='application/json')
        self.assertIn(response.status_code, [200,201])
        
    def test_view_enterprise_profile_delete(self):
        myProfile = EnterpriseProfile.objects.create(
            user = None,
            name = 'profile test',
            backstory = 'backstory test',
            picture = '',
            banner = ''
        )
        url = reverse('enterprise-profile-detail', args=[myProfile.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)