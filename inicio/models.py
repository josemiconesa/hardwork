from django.db import models
from django.utils import timezone

class Formulario(models.Model):
    Nombre = models.CharField(max_length = 20, blank = False, null = False)
    Email = models.EmailField()
    Asunto = models.CharField(max_length = 80, blank = False, null = False)
    Mensaje = models.CharField(max_length = 500, blank = False, null = False)
    Timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Email
