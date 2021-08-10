from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.utils.timezone import now

# Ignored, as we use User for now.
class Person(models.Model):
    username = models.CharField("username", max_length=40, unique=True, default="-1")
    first_name = models.CharField("first_name", max_length=40)
    last_name = models.CharField("last_name", max_length=40)
    # reputation ?

class Assignment(models.Model):
    date = models.DateTimeField("date") # auto ?
    due_date = models.DateTimeField("due_date", default=now)
    name = models.CharField("name", max_length=100)
    description = models.CharField("description", max_length=240)
    file_address = models.CharField("file_address", max_length=240)
    max_score = models.SmallIntegerField("max_score")

class Submission(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=models.DO_NOTHING, default="-1")
    assignment_id = models.ForeignKey(Assignment, to_field="id", on_delete=models.DO_NOTHING, default="-1")
    date = models.DateTimeField("date") # auto ?
    file_address = models.CharField("file_address", max_length=240)

class Assessment(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=models.DO_NOTHING, default="-1")
    assignment_id = models.ForeignKey(Assignment, to_field="id", on_delete=models.DO_NOTHING, default="-1")
    date = models.DateTimeField("date") # auto ?
    score = models.DecimalField("score", max_digits=8, decimal_places=4)
