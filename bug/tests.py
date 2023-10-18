from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from .models import Bug
from django.core.exceptions import ValidationError

# tests for bug model 

class BugModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.bug = Bug.objects.create(
            description="404 page does not exist",
            bug_type="improvement",
            report_date=timezone.now(),
            status="assigned",
        )
    
    def test_bug_creation(self):
        # Test whether the bug instance was created successfully
        self.assertEqual(self.bug.description, "404 page does not exist")
        self.assertEqual(self.bug.bug_type, "improvement")
        self.assertEqual(self.bug.status, "assigned")

    def test_bug_str_representation(self):
        """
        Test that the string representation of a bug is its description.
        """
        self.assertEqual(str(self.bug), "404 page does not exist")

    def test_status_choices(self):
        """Test that status field accepts only valid choices."""
        invalid_status = Bug(
            description="Invalid Status",
            bug_type="error",
            report_date=timezone.now(),
            status="invalid_status"
        )
        with self.assertRaises(ValidationError):
            invalid_status.full_clean()

    def test_status_choices(self):
        """Test that bug field accepts only valid choices."""
        invalid_status = Bug(
            description="Invalid Bug Type",
            bug_type="docs",
            report_date=timezone.now(),
            status="assigned"
        )
        with self.assertRaises(ValidationError):
            invalid_status.full_clean()

    def test_bug_update(self):
        """Test that a Bug object can be updated successfully."""
        bug = Bug(description="This is a bug.")
        bug.save()

        bug.description = "This bug has been updated."
        bug.bug_type = "improvement"
        bug.status = "in_progress"
        bug.save()

        self.assertEqual(bug.description, "This bug has been updated.")
        self.assertEqual(bug.bug_type, "improvement")
        self.assertEqual(bug.status, "in_progress")

# tests for the views
class BugViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date="2023-10-18",
            status="to_do"
        )
        self.bug_list_url = reverse("bug:bug_list")
        self.bug_detail_url = reverse("bug:bug_detail", args=[self.bug.id])
        self.bug_create_url = reverse("bug:register_bug")

    def test_index_view(self):
        response = self.client.get(reverse("bug:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug/index.html")

    def test_bug_list_view(self):
        response = self.client.get(self.bug_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug/bug_list.html")
        self.assertIn(self.bug, response.context["bug_list"])

    def test_bug_detail_view(self):
        response = self.client.get(self.bug_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug/bug_detail.html")
        self.assertEqual(response.context["bug_detail"], self.bug)

    def test_bug_create_view(self):
        response = self.client.get(self.bug_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bug/add_bug.html")

    def test_bug_create_form_submission(self):
        data = {
            "description": "New Test Bug",
            "bug_type": "new_feature",
            "report_date": "2023-10-18",
            "status": "to_do"
        }
        response = self.client.post(self.bug_create_url, data)
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful form submission
        self.assertTrue(Bug.objects.filter(description="New Test Bug").exists())

    def test_bug_create_form_invalid_submission(self):
        data = {
            "description": "",  # This field is required, so it's intentionally left empty
            "bug_type": "invalid_type",  # Invalid choice
            "report_date": "2023-10-18",
            "status": "to_do"
        }
        response = self.client.post(self.bug_create_url, data)
        self.assertEqual(response.status_code, 200)  # Expect a re-render of the form
        self.assertFormError(response, "form", "description", "This field is required.")
        self.assertFormError(response, "form", "bug_type", "Select a valid choice. invalid_type is not one of the available choices.")
