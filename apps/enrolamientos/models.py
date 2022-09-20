from django.db import models
from apps.cursos.models import Curso
from apps.participantes.models import Participante

# Create your models here.
class Enrolamiento(models.Model):
    enrola = models.BooleanField()
    fecha_enrola = models.DateField()
    curso = models.ManyToManyField(Curso)#,through=''
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)

    def __str__(self):
        return self.participante+self.curso
