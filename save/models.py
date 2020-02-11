from django.db import models

# Create your models here.
class List(models.Model):
    title = models.TextField()    

    def __str__(self):
        return self.title

class Items(models.Model):
    _list = models.ForeignKey(List, on_delete=models.CASCADE, related_name='items')
    item = models.CharField(max_length = 200)
    completed_item = models.TextField(default=' ', blank=True)

    def __str__(self):
        return self.item