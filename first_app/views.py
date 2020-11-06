from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Bloglist
# Create your views here.


def index(request):

    my_dict = {}
    my_dict['topic'] = Topic.objects.all().order_by('-timestamp')
    my_dict['blogs'] = Bloglist.objects.all()
    return render(request,"index.html",context=my_dict)

def topic_view(request,id):

    my_dict = {}
    my_dict['blogs'] = Bloglist.objects.filter(topic=id)
    my_dict['topic'] = Topic.objects.all().order_by('-timestamp')
    return render(request,"topic_page.html",context=my_dict)

def blog_view(request,id):

    my_dict = {}
    my_dict['blog'] = Bloglist.objects.filter(id=id)
    my_dict['topic'] = Topic.objects.all().order_by('-timestamp')
    return render(request,"blog_page.html",context=my_dict)
