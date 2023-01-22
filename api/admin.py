from django.contrib import admin

# Register your models here.


from api.models import Video

# Register your models here.
@admin.register(Video)
class VideoModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','publish_date','thumbnail_url',]
