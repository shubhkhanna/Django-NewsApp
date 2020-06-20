from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    api_request = requests.get("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=b910d1f00d0f4f4b8a4be92cbdb6bb50")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api' : api})