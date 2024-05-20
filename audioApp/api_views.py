from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Audio
import os
from server.settings import BASE_DIR
class AudioView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        max_data = request.data.get('max_data')
        if max_data is None:
            max_data = -1
        raw_audios = Audio.objects.all()[::max_data]
        audios = []
        for audio in raw_audios:
            audios.append({
                'url': audio.archivo.url,
                'abs_url': f'{BASE_DIR}/{audio.archivo.url}'.replace('\\','/'),
                'portada': audio.portada.url,
                'abs_portada': f'{BASE_DIR}/{audio.portada.url}'.replace('\\','/'),
                
                'titulo':audio.nombre,
                'description':audio.descripción,
                'usuario creador':audio.usuario_creador
            })
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
            'audios': audios
        }
        return Response(content)