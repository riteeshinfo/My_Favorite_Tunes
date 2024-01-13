from django.urls import path
from . import views
urlpatterns=[
    path('list/', views.List),
    path('list/<int:song_id>',views.song_detail),
    
]