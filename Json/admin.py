from django.contrib import admin
from Json.models import person, pregunta, RespuestaUsu


class pregunasAdmin(admin.ModelAdmin):
    list_display=("pregunta","resA","resB","resC","resD")

# Register your models here.
admin.site.register(person)
admin.site.register(pregunta,pregunasAdmin )
admin.site.register(RespuestaUsu)