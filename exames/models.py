from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Exame(models.Model):
    medico = models.ForeignKey("roles.Medico", verbose_name='medico',on_delete=models.CASCADE)
    paciente = models.ForeignKey("roles.Paciente", verbose_name='paciente',
        related_name = 'examesFromPaciente' , on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='texto')
    created_at = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return f'Exame {self.pk} | Medico {self.medico} | Paciente {self.paciente} | Created at {self.created_at}'

    
