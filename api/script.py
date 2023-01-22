api_keys = ['AIzaSyCnzjxv2xx64VyAouZPSWgLcUOW9GVbxgQ'] #include as many api key
current_key_index = 0

def get_next_key():
    global current_key_index
    key = api_keys[current_key_index]
    current_key_index = (current_key_index + 1) % len(api_keys)
    return key

def fetch_videos():
    try:
        from .models import Video
        import datetime
        import random
        from googleapiclient.discovery import build
        youtube = build('youtube', 'v3', developerKey=api_keys[current_key_index])
        query = random.choice(['cooking','football','cricket','hollywood','corona'])
        request = youtube.search().list(
                part="snippet",
                maxResults=25,
                type='video',
                order='date',
                publishedAfter='1970-01-01T00:00:00Z',
                q=query
            )
        response = request.execute()
        for video in response['items']:
            publish_date_str = video['snippet']['publishedAt']
            publish_date = datetime.datetime.strptime(publish_date_str,"%Y-%m-%dT%H:%M:%SZ")
            description = video['snippet']['description']
            thumbnail_url = video['snippet']['thumbnails']['default']['url']
            title = video['snippet']['title']
            Video.objects.create(publish_date=publish_date,description=description,title=title,thumbnail_url=thumbnail_url)
        print("======Videos Stored in the DB=======")
    except Exception as ex: #To specific exception can also be captured
        print("limit of API key is exhausted using next key onwards")
        get_next_key()
        
            