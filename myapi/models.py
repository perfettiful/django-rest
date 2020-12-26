from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name
class Profile(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    personal_statement = models.CharField(max_length=60)
    resume_url = models.CharField(max_length=60)

    def __str__(self):
        return self.name
