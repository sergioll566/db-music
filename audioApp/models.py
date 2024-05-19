from django.db import models
from django import forms
# Create your models here.
def validate_audio_extension(value):
    if not value.name.endswith('.mp3'):
        raise forms.ValidationError('Solo se permiten archivos PDF.')
    
class Audio(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='audios/',validators=[validate_audio_extension])
    portada = models.FileField(upload_to='audios/portadas/')
    descripción = models.CharField(max_length=255)
    usuario_creador = models.CharField(max_length=50)


class FormAudio(forms.ModelForm):
    class Meta:
        model = Audio
        fields = '__all__'