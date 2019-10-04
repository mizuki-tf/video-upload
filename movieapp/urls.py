from django.urls import path
from .import views

app_name = 'movieapp'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('upload/',views.UploadView.as_view(),name='upload'),
    path('play/<int:pk>/',views.PlayView.as_view(),name='play'),
]
