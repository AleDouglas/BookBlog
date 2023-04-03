from django.urls import path
from .views import HomePageView, ForumView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('forum/', ForumView.as_view(), name='forum_list'),
]