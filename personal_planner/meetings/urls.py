from django.urls import path

from meetings import views

urlpatterns = [
    path('', views.meetings, name="meetings"),
    path('<int:id>', views.detail, name="detail"),
    path('new', views.new, name="new"),
    path('create', views.create_meeting, name="create_meeting")
]
