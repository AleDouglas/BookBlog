from django.urls import path
from .views import HomePageView, ForumView, ForumDetailView
from users.views import EditProfile, ViewProfile


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<uuid:pk>', ForumDetailView.as_view(), name='book_detail'), 
    path('forum/', ForumView.as_view(), name='forum_list'),
    path('<int:pk>/profile/', ViewProfile.as_view(), name='profile'),
    path('<int:pk>/editprofile/', EditProfile.as_view(), name='profile_edit'),
]