from django.db import models


class Producto(models.Model):
    name = models.CharField(max_length=100)
    precio = models.FloatField()
    imagen = models.FileField(upload_to="")

    class Meta:
        db_table = "productos"

