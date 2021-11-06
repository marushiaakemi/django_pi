from django.contrib import admin
from .models import Post, Formulario

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sexo', 'email')
    