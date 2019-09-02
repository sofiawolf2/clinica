from django.urls import path
from exames.views import ExameCreateView #, ExameListView, ExameDetailView
# PostListView, PostCreateView, PostUpdateView, PostDeleteView, 

app_name = 'exames'

urlpatterns = [
    path('addexames', ExameCreateView.as_view(),name='add_exames'),
]