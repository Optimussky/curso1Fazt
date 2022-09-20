from django.db import models

# Create your models here.
class Participante(models.Model):
    
    nombre = models.CharField(max_length=80)
    apellido_paterno = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=80)
    correo = models.EmailField(primary_key=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nombre+" | "+self.apellido_materno+" | "+self.apellido_paterno+" | "+"@ "+self.correo

