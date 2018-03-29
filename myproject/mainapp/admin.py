# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Chasis, Motherboard, Processor, Powersupply, Memory, Storage, Operatingsys
from .models import Customer, Extras, Engineer, Boxcomputer, Humachininterface, Configuration
from .models import Boxconfig, Ippconfig, IndustrialPCDetail, BoxPCDetail, IPPCDetail

class ChasisAdmin(admin.ModelAdmin):
    list_display = ['ipc']
admin.site.register(Chasis, ChasisAdmin)

class MotherboardAdmin(admin.ModelAdmin):
    list_display = ['part_no']
admin.site.register(Motherboard, MotherboardAdmin)

class ProcessorAdmin(admin.ModelAdmin):
    list_display = ['cpu']
admin.site.register(Processor, ProcessorAdmin)

class PowersupplyAdmin(admin.ModelAdmin):
    list_display = ['smps']
admin.site.register(Powersupply, PowersupplyAdmin)

class MemoryAdmin(admin.ModelAdmin):
    list_display = ['ram']
admin.site.register(Memory, MemoryAdmin)

class StorageAdmin(admin.ModelAdmin):
    list_display = ['s_type', 's_size']
admin.site.register(Storage, StorageAdmin)

class OperatingsysAdmin(admin.ModelAdmin):
    list_display = ['O_sys']
admin.site.register(Operatingsys, OperatingsysAdmin)

class ExtrasAdmin(admin.ModelAdmin):
    list_display = ['extras']
admin.site.register(Extras, ExtrasAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer']
admin.site.register(Customer, CustomerAdmin)

class EngineerAdmin(admin.ModelAdmin):
    list_display = ['engineer']
admin.site.register(Engineer, EngineerAdmin)

class BoxcomputerAdmin(admin.ModelAdmin):
    list_display = ['uno']
admin.site.register(Boxcomputer, BoxcomputerAdmin)

class HumachininterfaceAdmin(admin.ModelAdmin):
    list_display = ['hmi']
admin.site.register(Humachininterface, HumachininterfaceAdmin)

class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ['customer', 'ipc', 'mboard', 'cpu', 'smps', 'created']
admin.site.register(Configuration, ConfigurationAdmin)

class BoxconfigAdmin(admin.ModelAdmin):
    list_display = ['customer', 'uno', 'ram', 'storage', 'Osys', 'created']
admin.site.register(Boxconfig, BoxconfigAdmin)

class IppconfigAdmin(admin.ModelAdmin):
    list_display = ['customer', 'ippc', 'ram', 'storage', 'Osys', 'created']
admin.site.register(Ippconfig, IppconfigAdmin)

class IndustrialPCDetailAdmin(admin.ModelAdmin):
    list_display = ['customer', 'configuration_no', 'ipc_serial', 'am_serial', 'product_key', 'total_pc', 'assembled_on']
admin.site.register(IndustrialPCDetail, IndustrialPCDetailAdmin)

class BoxPCDetailAdmin(admin.ModelAdmin):
    list_display = ['customer','configuration_no', 'uno_serial', 'product_key', 'total_pc', 'assembled_on', 'assembled_by']
admin.site.register(BoxPCDetail, BoxPCDetailAdmin)

class IPPCDetailAdmin(admin.ModelAdmin):
    list_display = ['customer','configuration_no', 'ippc_serial', 'product_key', 'total_pc', 'assembled_on', 'assembled_by']
admin.site.register(IPPCDetail, IPPCDetailAdmin)
