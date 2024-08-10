import os
from django.db import models
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def video_file_path(instance, filename):
    # Extrai a extensão do arquivo
    ext = filename.split('.')[-1]
    # Define o novo nome do arquivo baseado no campo 'nome' do modelo
    filename = f"{instance.nome}.{ext}"
    # Retorna o caminho completo do arquivo
    return os.path.join('videos/', filename)


class Video(BaseModel):
    nome = models.CharField(max_length=255)
    video = models.FileField(upload_to=video_file_path)
    history = HistoricalRecords()  # Adiciona o campo de histórico

    def __str__(self):
        return self.nome
