from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Model

from zuri_sample.links.managers import ActiveLinkManager

User=get_user_model()
# Create your models here.
class Links(models.Model):
    target_url= models.URLField(max_length=200)
    description= models.CharField(max_length=200)
    identifier=models.SlugField(max_length=20, blank=True, unique=False)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_date= models.DateTimeField()
    active= models.BooleanField()
    objects= models.Manager()
    public=ActiveLinkManager()

 #   def __str__(self) -> str:
 #       return self.name


