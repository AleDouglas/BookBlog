from django.urls import path
from .views import BookListView, SearchResultsListView, NewBookAdd, NewComment, EditComment, DeleteComment

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'), 
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    #User Options
    path('addbook/', NewBookAdd.as_view(), name='add_book'),
    path('<uuid:pk>/addcomment/', NewComment.as_view(), name='add_comment'),
    path('<uuid:id_dados>/<int:pk>/editcomment/', EditComment.as_view(), name='edit_comment'),
    path('<uuid:id_dados>/<int:pk>/deletecomment/', DeleteComment.as_view(), name='delete_comment'),
]