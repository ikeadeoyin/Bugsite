import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Bug(models.Model):
    BUG_TYPES = [
        ("error", "error"),
        ("new_feature", "new feature"),
        ("improvement", "improvement"),
        ("test_case", "test case")
    ]
    BUG_STATUSES = [
        ("to_do", "to do"),
        ("assigned", "assigned"),
        ("in_progress", "in progress"),
        ("under_review", "under review"),
        ("done", "done")
    ]
    description = models.TextField(max_length=500)
    bug_types = models.CharField(max_length=20, choices=BUG_TYPES)
    report_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=BUG_STATUSES)

    def __str__(self):
        return self.description

