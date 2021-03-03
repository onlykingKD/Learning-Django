from django.urls import path
from playlist import views

urlpatterns = [
    # TODO: Add the path for home view at ''
    path('',views.home),
    path('about/',views.about,name="about"),
    path('<int:id>',views.playlist,name="playlist"),
    # TODO: Add the path for playlist with given id
    # HINT: path('playlist/<int:id>', ...)
    
]