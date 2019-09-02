from django.urls import path
from exames.views import ExameCreateView #, ExameListView, ExameDetailView
# PostListView, PostCreateView, PostUpdateView, PostDeleteView, 

app_name = 'exames'

urlpatterns = [
    # path('exames',ExameListView.as_view(),name='list_exames'),
    path('addexames', ExameCreateView.as_view(),name='add_exames'),
    # path('exames/<int:pk>/detalhar', ExameDetailView.as_view(), name = 'detail_exames'),
    
    # path('posts/<int:pk>/alterar',PostUpdateView.as_view(),name='update_post'),
    # path('posts/<int:pk>/deletar',PostDeleteView.as_view(),name='delete_post'),
  
]