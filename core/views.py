# views.py
import logging
from django.http import JsonResponse,HttpResponse

# Configure logger
logger = logging.getLogger(__name__)
def helloWorld(request):
    context = {
        "message": "Hello From Index World!",
        "author": "Asikur Rahman"
    }
    # ?return HttpResponse("Hello World!")
    return render(request, 'index.html', context)

def helloWorld1(request):
    data = {
        "message": "Hello World!2"
    }
    return JsonResponse(data)

def aboutPageIndex(request):
    return render(request, 'about.html')