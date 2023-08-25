from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    listname = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null="True")
    
    def __str__(self):
        return f"{self.id} {self.listname} {self.user}"
