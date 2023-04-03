from django.urls import path
from .views import HomePageView, ForumView
from users.views import EditProfile


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('forum/', ForumView.as_view(), name='forum_list'),
    path('<int:pk>/editprofile/', EditProfile.as_view(), name='profile_edit'),
]