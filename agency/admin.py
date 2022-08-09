from django.contrib import admin
from agency.models import RomEng, RomEngExp, EngRomVerbs, WayToSay


@admin.register(RomEng)
class RomEngAdmin(admin.ModelAdmin):
    list_display = ['id', 'rom', 'eng']


@admin.register(WayToSay)
class WayToSayAdmin(admin.ModelAdmin):
    list_display = ['id', 'rom', 'eng']


@admin.register(RomEngExp)
class RomEngExpAdmin(admin.ModelAdmin):
    list_display = ['romex', 'engex']


@admin.register(EngRomVerbs)
class EngRomVerbsAdmin(admin.ModelAdmin):
    list_display = ['eng', 'engdict', 'rom']

