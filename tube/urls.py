from django.urls import path
from . import views

urlpatterns = [
    path('', views.youtube, name='home'),
    path('download/', views.download, name='download'),
    path('downloaded/<res>', views.downloaded, name='download_complete'),

]