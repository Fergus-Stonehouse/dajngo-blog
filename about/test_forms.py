from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Bob',
            'email': 'test@test.com',
            'message': 'Eclipse Phase for the win!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

# Create your tests here.
    def test_form_is_valid(self):    
        """ Test for name field"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Eclipse Phase for the win!'
        })
        self.assertFalse(form.is_valid(), msg="Name was not added but Form is valid")


    def test_form_is_valid(self):
        """ Test for email field"""
        form = CollaborateForm({
            'name': 'Bob',
            'email': '',
            'message': 'Eclipse Phase for the win!'
        })
        self.assertFalse(form.is_valid(), msg="email was not added but Form is valid")


    def test_form_is_valid(self):
        """ Test for message field"""
        form = CollaborateForm({
            'name': 'Bob',
            'email': 'test@test.com',
            'message': ''})
        self.assertFalse(form.is_valid(), msg="message was not added but Form is valid")

