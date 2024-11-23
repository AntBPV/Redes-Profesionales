import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest.mock import MagicMock
from django.core.files import File

from .models import PostModel
from UserProfile.models import Profile
from EnterpriseProfile.models import EnterpriseProfile

User = get_user_model()

class test_post(TestCase):
    def setUp(self):
        self.post = PostModel.objects.create(
            user = None,
            UserProfile = None,
            EnterpriseProfile = None,
            image = '',
            text = 'text'
        )
        
    def tearDown(self):
        pass
    
    def test_view_post_list(self):
        url = reverse('post-list')
        response = self.client.get(url)
        data = json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data),0)
        
    def test_view_post_detail(self):
        url = reverse('post-detail', args=[self.post.id])
        response = self.client.get(url)
        data = json.loads(response.content.decode('utf-8'))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['id'], self.post.id)
        
    ## FIXME: 400 Bad Request on this test
    ## Separator: --------------------------------------------------------------------
    def test_view_post_create(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        user_profile = Profile.objects.create(user=user)
        enterprise_profile = EnterpriseProfile.objects.create(name='Test Enterprise')
        
        image_file = MagicMock(spec=File)
        image_file.name = 'test_image.jpg'
        
        data = {
            'user': user.id,
            'UserProfile': user_profile.id,
            'EnterpriseProfile': enterprise_profile.id,
            'image': image_file,
            'text': 'text',

        }
        url = reverse('post-list')
        response = self.client.post(url, data, format='multipart')
        data = json.loads(response.content.decode('utf-8'))
        
        self.assertIn(response.status_code, [200,201])
        
    def test_view_post_update(self):
        myPost = PostModel.objects.create(
            user = None,
            UserProfile = None,
            EnterpriseProfile = None,
            image = None,
            text = 'text'
        )
        valid_post = {
            'text': 'text updated'
        }
        url = reverse('post-detail', args=[myPost.id])
        valid_post_json = json.dumps(valid_post)
        response = self.client.put(url, valid_post_json, content_type='application/json')
        self.assertIn(response.status_code, [200,201])
    
    ## End Of Separator: ------------------------------------------------------------
    
    def test_view_post_delete(self):
        myPost = PostModel.objects.create(
            user = None,
            UserProfile = None,
            EnterpriseProfile = None,
            image = None,
            text = 'text'
        )
        url = reverse('post-detail', args=[myPost.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)