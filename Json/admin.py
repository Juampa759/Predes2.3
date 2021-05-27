from django.contrib import admin
from Json.models import person, pregunta, RespuestaUsu
class personAdmin(admin.ModelAdmin):
    list_display=("User_id","pregunta","score")

class pregunasAdmin(admin.ModelAdmin):
    list_display=("pregunta","resA","resB","resC","resD")

class respuestaAdmin(admin.ModelAdmin):
    list_display=("User_id","Pregunta_id","respuesta")


# Register your models here.
admin.site.register(person, personAdmin)
admin.site.register(pregunta,pregunasAdmin )
admin.site.register(RespuestaUsu, respuestaAdmin)