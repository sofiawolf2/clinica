from django.urls import path
from exames.views import ExameCreateView #ExameDetailsView
# PostListView, PostCreateView, PostUpdateView, PostDeleteView, 

app_name = 'exames'

urlpatterns = [
    # path('posts',PostListView.as_view(),name='list_posts'),
    path('addexames', ExameCreateView.as_view(),name='add_exames'),
    # path('posts/<int:pk>/alterar',PostUpdateView.as_view(),name='update_post'),
    # path('posts/<int:pk>/deletar',PostDeleteView.as_view(),name='delete_post'),
  
]