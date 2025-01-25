from django.contrib import admin
from .models import ComentarioInstituicao, ComentarioCurso

# Register your models here.
admin.site.register(ComentarioInstituicao, ComentarioCurso) 
