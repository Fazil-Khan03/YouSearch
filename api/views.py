# Create your views here.
from django.views.generic import View
from .responses import *
from .models import Video
from .exceptions import SearchParamsMissing
from django.core.paginator import Paginator
from .constants import *

class VideoView(View):
    def __init__(self):
        self.response = init_response()

    def get(self, request, *args, **kwargs):
        try:
            page = request.GET.get('page',1)
            all_videos = []
            video_objs = Video.objects.get_videos()
            paginator = Paginator(video_objs, 10)
            page = paginator.page(page)    
            for video in page:
                all_videos.append(video.as_dict())
            self.response['res_data'] = all_videos
            self.response['res_str'] = FETCHED_SUCCESSSFULLY
        except Exception as ex:
            self.response['res_data'] = []
            self.response['res_str'] = UNABLE_TO_FETCH
        return send_200(self.response)

class SearchView(View):
    def __init__(self):
        self.response = init_response()

    def validate_params(self, params):
        title = params.get('title')
        description = params.get('description')
        if not title and not description:
            raise SearchParamsMissing(PARAMS_MISSING)
        if title and description:
            return  title, description
        if not title:
            return None, description
        elif not description:
            return  title, None

    def get(self, request, *args, **kwargs):
        try:
            searched_videos = []
            params = request.GET
            title, description = self.validate_params(params)
            if title and description:
                video_objs = Video.objects.search_videos_by_title_and_desc(title, description)
            elif title:
                video_objs = Video.objects.search_videos_by_title_(title)
            else:
                video_objs = Video.objects.search_videos_by_description(description) 
            for video in video_objs:
                searched_videos.append(video.as_dict())
            self.response['res_data'] = searched_videos
            self.response['res_str'] = FETCHED_SUCCESSSFULLY
        except SearchParamsMissing as ex:
            self.response['res_data'] = []
            self.response['res_str'] = str(ex)
            return send_401(self.response)
        except Exception as ex:
           self.response['res_data'] = []
           self.response['res_str'] = FETCHED_SUCCESSSFULLY
        return send_200(self.response)    

