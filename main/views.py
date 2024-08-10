from django.shortcuts import render
from .models import Video

def index(request):
    # Busca o vídeo específico no banco de dados
    video = Video.objects.filter(nome="juliana_gaioso_video_1").first()
    return render(request, 'main/index.html', {'video': video})
