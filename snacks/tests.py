from django.test import TestCase
from django.urls import reverse
# Create your tests here.


# Create your tests here.
class ThingsTest(TestCase):
    def test_list_view_status(self):
        url = reverse('snacks')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_list_view_template(self):
        url = reverse('snacks')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'snack_list.html')