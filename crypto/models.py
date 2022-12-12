from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Crypto(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField(max_length=255,help_text="the name")
    rank=models.IntegerField()
    desc=models.TextField(default="description")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_ad=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name