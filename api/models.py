from django.db import models
from .manager import VideoManager

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100,db_index=True)
    description = models.TextField(db_index=True)
    publish_date = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return str(self.id) + " " + self.title
        
    objects = VideoManager()

    def as_dict(self):
        data = {}
        data['title'] = self.title
        data['description'] = self.description
        data['published_date'] = self.publish_date
        return data


