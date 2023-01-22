from django.db import models
from django.db.models import Q

class VideoManager(models.Manager):
    #TO DO: Search can be optimized using PostgresSQL DB using search lookup or we can use elasticSearch 
    def search_videos_by_title_and_desc(self, title, description):
        matched_videos = self.model.objects.filter(Q(description__icontains=description) | Q(title__icontains=title)).order_by('-publish_date')
        return matched_videos

    def search_videos_by_title_(self, title):
        matched_videos = self.model.objects.filter(title__icontains=title).order_by('-publish_date')
        return matched_videos

    def search_videos_by_description(self, description):
        matched_videos = self.model.objects.filter(description__icontains=description).order_by('-publish_date')
        return matched_videos    

    def get_videos(self):
        all_videos = self.model.objects.filter().order_by('-publish_date')
        return all_videos