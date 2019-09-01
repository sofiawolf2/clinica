from django.urls import path
from roles.views import UserLoginView, UserLogoutView, UserDetailView

app_name = 'users'

urlpatterns = [
    # path('logar',UserLoginView.as_view(),name = 'logar_user'),
    path('logar', UserLoginView.as_view(), name = 'logar_user'),
    path('logout',UserLogoutView.as_view(),name = 'logout_user'),
    path('sobre/<int:pk>/detalhes', UserDetailView.as_view(),name = 'detalhes_user'), 
    # path('cadastro',UserCadastroView.as_view(),name = 'cadastro_user'),
]