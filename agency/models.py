from django.db import models


class RomEng(models.Model):
    rom = models.CharField(max_length=300)
    eng = models.CharField(max_length=300)

    def __str__(self):
        s = ''.join(char for char in self.rom if char.isalnum())
        return s


class WayToSay(models.Model):
    rom = models.CharField(max_length=300)
    eng = models.CharField(max_length=300)

    def __str__(self):
        s = ''.join(char for char in self.rom if char.isalnum())
        return s


class RomEngExp(models.Model):
    romex = models.CharField(max_length=100)
    engex = models.CharField(max_length=100)

    def __str__(self):
        s = ''.join(char for char in self.romex if char.isalnum())
        return s


class EngRomVerbs(models.Model):
    eng = models.CharField(max_length=100)
    engdict = models.CharField(max_length=100)
    rom = models.CharField(max_length=100)

    def __str__(self):
        s = ''.join(char for char in self.rom if char.isalnum())
        return s
