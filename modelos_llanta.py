# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Existencia(models.Model):
    idcodigo = models.IntegerField(primary_key=True)
    idproveedor = models.IntegerField()
    fcompra = models.DateField()
    nqtycompra = models.IntegerField(blank=True, null=True)
    nqtyexistencia = models.IntegerField()
    fultcompra = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'existencia'
        unique_together = (('idcodigo', 'idproveedor', 'fcompra'),)


class Maestro(models.Model):
    ccodigo = models.CharField(unique=True, max_length=20)
    ccodbarra = models.CharField(max_length=50, blank=True, null=True)
    cdescrip = models.CharField(max_length=100)
    cdescripcorto = models.CharField(max_length=100, blank=True, null=True)
    nprecio = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    ncosto = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    fultcmp = models.DateField(blank=True, null=True)
    lestado = models.BooleanField()
    idmarca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='idmarca', blank=True, null=True)
    idum = models.ForeignKey('Um', models.DO_NOTHING, db_column='idum', blank=True, null=True)
    uc = models.CharField(max_length=20)
    fc = models.DateTimeField()
    um = models.CharField(max_length=20, blank=True, null=True)
    fm = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maestro'


class Marca(models.Model):
    idmarca = models.AutoField(primary_key=True)
    cdescrip = models.CharField(max_length=100, blank=True, null=True)
    uc = models.CharField(max_length=20)
    fc = models.DateTimeField()
    um = models.CharField(max_length=20, blank=True, null=True)
    fm = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marca'


class Um(models.Model):
    idum = models.AutoField(primary_key=True)
    cdescrip = models.CharField(max_length=-1, blank=True, null=True)
    uc = models.CharField(max_length=20)
    fc = models.DateTimeField()
    um = models.CharField(max_length=20, blank=True, null=True)
    fm = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'um'
