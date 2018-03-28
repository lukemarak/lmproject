# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Chasis(models.Model):
    ipc = models.CharField(max_length=20)

    class Meta:
        ordering = ('ipc',)
        verbose_name = 'chasis'
        verbose_name_plural = 'chasiss'

    def __str__(self):
        return self.ipc

class Motherboard(models.Model):
    part_no = models.CharField(max_length=20)

    class Meta:
        ordering = ('part_no',)
        verbose_name = 'motherboard'
        verbose_name_plural = 'motherboards'

    def __str__(self):
        return self.part_no

class Processor(models.Model):
    cpu = models.CharField(max_length=20)

    class Meta:
        ordering = ('cpu',)
        verbose_name = 'processor'
        verbose_name_plural = 'processors'

    def __str__(self):
        return self.cpu

class Powersupply(models.Model):
    smps = models.CharField(max_length=20)

    class Meta:
        ordering = ('smps',)
        verbose_name = 'powersupply'
        verbose_name_plural = 'powersupplys'

    def __str__(self):
        return self.smps

class Memory(models.Model):
    ram = models.CharField(max_length=20)

    class Meta:
        ordering = ('ram',)
        verbose_name = 'memorie'
        verbose_name_plural = 'memories'

    def __str__(self):
        return self.ram

class Storage(models.Model):
    s_type = models.CharField(max_length=20)
    s_size = models.CharField(max_length=20)

    class Meta:
        ordering = ('s_type', 's_size',)
        verbose_name = 'storage'
        verbose_name_plural = 'storages'

    def __str__(self):
        return self.s_type

class Operatingsys(models.Model):
    O_sys = models.CharField(max_length=50)

    class Meta:
        ordering = ('O_sys',)
        verbose_name = 'operatingsys'
        verbose_name_plural = 'operatingsyss'

    def __str__(self):
        return self.O_sys

class Extras(models.Model):
    extras = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.extras

class Customer(models.Model):
    customer = models.CharField(max_length=100)

    class Meta:
        ordering = ('customer',)
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return self.customer

class Engineer(models.Model):
    engineer = models.CharField(max_length=50)

    class Meta:
        ordering = ('engineer',)
        verbose_name = 'engineer'
        verbose_name_plural = 'engineers'

    def __str__(self):
        return self.engineer

class Boxcomputer(models.Model):
    uno = models.CharField(max_length=50)

    class Meta:
        ordering = ('uno',)
        verbose_name = 'boxcomputer'
        verbose_name_plural = 'boxcomputers'

    def __str__(self):
        return self.uno

class Humachininterface(models.Model):
    hmi = models.CharField(max_length=100)

    class Meta:
        ordering = ('hmi',)
        verbose_name = 'humamachineinterface'
        verbose_name_plural = 'humachininterfaces'

    def __str__(self):
        return self.hmi

class Configuration(models.Model):
    customer = models.ForeignKey(Customer, related_name='configurations')
    ipc = models.ForeignKey(Chasis, related_name='configurations')
    mboard = models.ForeignKey(Motherboard, related_name='configurations')
    cpu = models.ForeignKey(Processor, related_name='configurations')
    smps = models.ForeignKey(Powersupply, related_name='configurations')
    ram = models.ForeignKey(Memory, related_name='configurations')
    storage = models.ForeignKey(Storage, related_name='configurations')
    Osys = models.ForeignKey(Operatingsys, related_name='configurations')
    extra = models.ForeignKey(Extras, related_name='configurations')
    total_pc = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('customer', 'ipc', 'mboard', 'cpu', 'ram', 'storage', 'Osys', 'slug',)
        verbose_name = 'configuration'
        verbose_name_plural = 'configurations'

    def __str__(self):
        return self.customer

class Boxconfig(models.Model):
    customer = models.ForeignKey(Customer, related_name='boxconfigs')
    uno = models.ForeignKey(Boxcomputer, related_name='boxconfigs')
    ram = models.ForeignKey(Memory, related_name='boxconfigs')
    storage = models.ForeignKey(Storage, related_name='boxconfigs')
    Osys = models.ForeignKey(Operatingsys, related_name='boxconfigs')
    extra = models.ForeignKey(Extras, related_name='boxconfigs')
    total_pc = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('customer', 'uno', 'ram', 'storage', 'Osys', 'slug',)
        verbose_name = 'boxconfig'
        verbose_name_plural = 'boxconfigs'

    def __str__(self):
        return self.customer

class Ippconfig(models.Model):
    customer = models.ForeignKey(Customer, related_name='ippconfigs')
    ippc = models.ForeignKey(Humachininterface, related_name='ippconfigs')
    ram = models.ForeignKey(Memory, related_name='ippconfigs')
    storage = models.ForeignKey(Storage, related_name='ippconfigs')
    Osys = models.ForeignKey(Operatingsys, related_name='ippconfigs')
    extra = models.ForeignKey(Extras, related_name='ippconfigs')
    total_pc = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('customer', 'ippc', 'ram', 'storage', 'Osys', 'slug',)
        verbose_name = 'boxconfig'
        verbose_name_plural = 'boxconfigs'

    def __str__(self):
        return self.customer

class IndustrialPCDetail(models.Model):
    customer = models.ForeignKey(Customer, related_name='industrialpcdetails')
    configuration_no = models.ForeignKey(Configuration, related_name='industrialpcdetails')
    ipc_serial = models.CharField(max_length=20, unique=True)
    am_serial = models.CharField(max_length=20, unique=True)
    smps_serial = models.CharField(max_length=200, unique=True)
    ram_serial = models.CharField(max_length=200, unique=True)
    hd_serial = models.CharField(max_length=200, unique=True)
    product_key = models.CharField(max_length=100, unique=True, blank=True)
    extra = models.CharField(max_length=200, blank=True)
    total_pc = models.IntegerField()
    assembled_on = models.DateTimeField(auto_now_add=True)
    assembled_by = models.ForeignKey(Engineer, related_name='industrialpcdetails')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('customer', 'configuration_no', 'ipc_serial', 'product_key', 'total_pc', 'slug',)
        verbose_name = 'industrialpcdetail'
        verbose_name_plural = 'industrialpcdetails'

    def __str__(self):
        return self.customer

class BoxPCDetail(models.Model):
    customer = models.ForeignKey(Customer, related_name='boxpcdetails')
    configuration_no = models.ForeignKey(Configuration, related_name='boxpcdetails')
    uno_serial = models.CharField(max_length=20, unique=True)
    ram_serial = models.CharField(max_length=200, unique=True)
    hd_serial = models.CharField(max_length=200, unique=True)
    product_key = models.CharField(max_length=100, unique=True, blank=True)
    extra = models.CharField(max_length=200, blank=True)
    total_pc = models.IntegerField()
    assembled_on = models.DateTimeField(auto_now_add=True)
    assembled_by = models.ForeignKey(Engineer, related_name='boxpcdetails')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('customer', 'configuration_no', 'uno_serial', 'product_key', 'total_pc', 'slug',)
        verbose_name = 'boxpcdetail'
        verbose_name_plural = 'boxpcdetails'

    def __str__(self):
        return self.customer

class IPPCDetail(models.Model):
    customer = models.ForeignKey(Customer, related_name='ippcdetails')
    configuration_no = models.ForeignKey(Configuration, related_name='ippcdetails')
    ippc_serial = models.CharField(max_length=20, unique=True)
    ram_serial = models.CharField(max_length=200, unique=True)
    hd_serial = models.CharField(max_length=200, unique=True)
    product_key = models.CharField(max_length=100, unique=True, blank=True)
    extra = models.CharField(max_length=200, blank=True)
    total_pc = models.IntegerField()
    assembled_on = models.DateTimeField(auto_now_add=True)
    assembled_by = models.ForeignKey(Engineer, related_name='ippcdetails')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('customer', 'configuration_no', 'ippc_serial', 'product_key', 'total_pc','slug',)
        verbose_name = 'ippcdetail'
        verbose_name_plural = 'ippcdetails'

    def __str__(self):
        return self.customer
