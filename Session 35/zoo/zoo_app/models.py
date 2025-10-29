from django.db import models

# Create your models here.

from django.db import models

class Species(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    category = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'Species ({self.name}, {self.category})'

class Animal(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    birthday = models.DateField(auto_now_add=True, null=False, blank=False)
    species = models.ForeignKey(Species, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f'Animal ({self.name}, {self.species.name})'

class User(models.Model):
    username = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=64, null=False, blank=False)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'User ({self.username})'
