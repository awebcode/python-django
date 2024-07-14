from django.shortcuts import render

def helloBlog(request):
    print('Hello from the Blog!',type(request))
    context = {
        'message': 'Hello from the Blog!',
        'author': 'Asikur Rahman',
    }
    return render(request, 'blog/index.html', context)

def aboutPage(request):
    context = {
        'title': 'About Us',
        'description': 'This is the about page.',
    }
    return render(request, 'about.html', context)
