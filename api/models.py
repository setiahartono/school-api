import uuid
from django.db import models
from model_utils import FieldTracker


class School(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, db_index=True)
    capacity = models.PositiveIntegerField()
    address = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=63, null=False, blank=False)

    tracker = FieldTracker()

    def __str__(self):
        return self.name


class Student(models.Model):
    identification = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, db_index=True)

    tracker = FieldTracker()

    def __str__(self):
        return f"{self.school} - {self.first_name} {self.last_name} - {self.identification}"


class ChangeLog(models.Model):
    model_name = models.CharField(max_length=255)
    instance_id = models.IntegerField()
    action = models.CharField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model_name} - {self.action}"