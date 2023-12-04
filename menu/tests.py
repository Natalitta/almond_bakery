from django.test import TestCase


class TestViews(TestCase):

    # Test Home page
    def test_home_page(self):
        # Test correct home page is displayed
        response = self.client.get('/')
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, 'home/index.html')
