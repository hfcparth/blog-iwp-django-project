from django.urls import path
from first_app import views

urlpatterns = [

    path('',views.index),
    path('topics/<int:id>',views.topic_view),
    path('blog/<int:id>',views.blog_view)

]
