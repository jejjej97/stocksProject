from django.shortcuts import render

def my(request):
    context = {};
    context['center'] = 'sidemenu/my.html';
    return render(request, 'index.html', context);

