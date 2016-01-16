from django.db import models

class Review(models.Model):
   comment = models.CharField(default='', max_length=200)