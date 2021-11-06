from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("aplicacao:detail", kwargs={"slug":self.slug})

class Formulario(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("aplicacao:formulario", kwargs={"id":self.id})    