from django.contrib import admin
from .models import aluno

class alunoAdmin(admin.ModelAdmin):

    list_display = ['nome', 'rcq', 'imc', 'peso', 'altura', 'cintura', 'quadril']

admin.site.register(aluno)