from django.db import models


class Guest(models.Model):
    guest_id = models.CharField(max_length=4, verbose_name='ID convite')
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    adult_guest = models.IntegerField(verbose_name='Adultos', default=0)
    child_guest = models.IntegerField(verbose_name='Crianças', default=0)
    whatsapp = models.CharField(max_length=15, verbose_name='Whatsapp')
    invite_status = models.IntegerField(verbose_name='Estado do convite', default=0)
    
    def __str__(self):
        return self.first_name
    