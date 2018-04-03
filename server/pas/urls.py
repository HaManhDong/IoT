from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devices-info/', views.devices_info, name='devices-info'),
    path('members-info/', views.members_info, name='members-info'),
    path('member-profile/', views.member_profile, name='member-profile'),
    path('api/members/', views.members_api, name='api/members'),
    path('api/upload-image/', views.upload_images, name='api/upload-image'),
]