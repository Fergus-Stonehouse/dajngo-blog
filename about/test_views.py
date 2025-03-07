from django.urls import reverse
from django.test import TestCase
from .models import About
from .forms import CollaborateForm


# Create your tests here.
class TestAboutViews(TestCase):

    def setUp(self):
        
        """
        Build the About Me content
        """

        self.about_content = About(title="About Me",
            content="Read all about me.")
        self.about_content.save()


    def test_render_about_page_with_collaboration_form(self):

        """
        Verify the GET request within About Me for collaboration form... I think...
        """

        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About Me", response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)
    
    def test_successful_collaboration_submission(self):

        """
        Verify the POST submission within About Me
        """

        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Collaboration request received! I endeavour to respond within 2 working days.',
            response.content)