from django.shortcuts import render,redirect,HttpResponse
from .models import Audio,FormAudio
# Create your views here.
def homepage(request):
    FORMULARIO = FormAudio()
    
    # elif request.method == 'GET':
    audios = Audio.objects.all()
    return render(request,'homepage.html',{'formularioAudio':FORMULARIO,'audios':audios})

def registrar(request):
    if request.method == 'POST':
        form = FormAudio(request.POST, request.FILES)  # Asegúrate de incluir request.FILES
        if form.is_valid():
            audio = form.save()
            print(f'{audio=}')
            return redirect('home_audio')
    else:
        form = FormAudio()
    
    return render(request, 'homepage.html', {'formularioAudio': form})