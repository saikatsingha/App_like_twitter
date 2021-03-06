from os import stat
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse('')
    return render(request, "pages/home.html", context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)
    


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data ={
        "id": tweet_id,
        # "content": obj.content,
        # "image_path": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not Found"
        status = 404

    
    # return HttpResponse(f'<h1>Hello {tweet_id} - {obj.content}</h1>')
    return JsonResponse(data, status= status)
