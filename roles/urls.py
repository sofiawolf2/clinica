from django.urls import path
from roles.views import UserLoginView, UserLogoutView, MedicoDetailView, PacienteDetailView

app_name = 'users'

urlpatterns = [
    # path('logar',UserLoginView.as_view(),name = 'logar_user'),
    path('logar', UserLoginView.as_view(), name = 'logar_user'),
    path('logout',UserLogoutView.as_view(),name = 'logout_user'),
    path('medico/<int:pk>/detalhes', MedicoDetailView.as_view(),name = 'detalhes_medico'), 
    path('paciente/<int:pk>/detalhes', PacienteDetailView.as_view(),name = 'detalhes_paciente'), 
    # path('cadastro',UserCadastroView.as_view(),name = 'cadastro_user'),
]