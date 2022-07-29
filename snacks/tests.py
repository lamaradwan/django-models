from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.


# Create your tests here.
from snacks.models import Snack


class SnacksTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='lama1996'
        )
        self.snack = Snack.objects.create(
            name='snack test',
            purchaser=self.user,
            description='description for testing'
        )

    def test_list_view_status(self):
        url = reverse('snacks')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_list_view_template(self):
        url = reverse('snacks')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'snack_list.html')

    def test_str(self):
        self.assertEqual(str(self.snack), 'snack test')

    def test_detail_view(self):
        url = reverse('snack_detail', args=[self.snack.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_create_view(self):
        url = reverse('snack_create')
        data = {
            'name': 'snack test',
            'purchaser': self.user.pk,
            'description': 'description for testing'
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snack_detail.html')
        self.assertRedirects(response, reverse('snack_detail', args=[2]))
        self.assertEqual(len(Snack.objects.all()),2)