from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be more than 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Course description should be more than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = CourseManager()

    def __unicode__(self):
        return "id: " + str(self.id) + ", name: " + self.name + ", description: " + self.desc + ", created_at: " + str(self.created_at)
