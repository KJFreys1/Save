from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class List(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='lists')
    title = models.TextField()    

    def __str__(self):
        return self.title

class Items(models.Model):
    _list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')
    item = models.CharField(max_length = 200)
    completed_item = models.TextField(default=' ', blank=True)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.item