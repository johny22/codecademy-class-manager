from django.http import HttpResponse
from datetime import datetime
from Colect import Collector
from codecademy.Parser.models import Perfil ## Esse código da erro!!!!!!!


parser = Collector("/home/jones/codecademy/Parser/perfis_codecademy")
parser.gerarURLs()
parser.colectPerfis()


def InserirNoBD(request):
    pass
