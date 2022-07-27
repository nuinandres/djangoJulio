from django.db import models
from datetime import datetime
# Create your models here.
#Los modelos son entidades en la base de datos

class Empleado(models.model):
    names = models.Charfield(max_lenth=150, verbose_name='Nombres')
    dni = models.Charfield(max_lenth=10, unique=True, verbose_name='Dni')
    date_create = models.Datefield(defaults=datetime.now(), verbose_name='Fecha de registro')
    date_update = models.DateTimefield(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_okaces=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upplad_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upplad_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        reversed_name = 'Empleado'
        reversed_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']

