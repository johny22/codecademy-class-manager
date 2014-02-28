# -*- coding: utf-8 -*-
## Jones Romão 

from django.http import HttpResponse
from datetime import datetime
from Colect import Collector
from codecademy.parser.models import *


parser = Collector("/home/jones/codecademy/parser/perfis_codecademy")
parser.gerarURLs()
parser.colectPerfis()


def InserirNoBD(request):
    for i in parser.perfis:

        perf = Perfil(nome = i["Nome"], melhorP = i["Melhores Pontos"], hoje = i["Hoje"], dias_seg = i["Dias Seguidos"], total_ponts = i["Total"])
        perf.save()

        achi = i["perf_achievements"][:]
        for j in achi:
            achiv = Achievements(perfil = Perfil.objects.get(nome=i["Nome"]), nome = j.pop(0), data = j.pop(0))
            achiv.save()

        tracks = i["tracks"][:]
        for k in tracks:
            trk = Track(perfil = Perfil.objects.get(nome=i["Nome"]), nome = k["name"], percent = k["percent"], data = k["last"])
            trk.save()

        hist = History(perfil = Perfil.objects.get(nome=i["Nome"]), melhorP = i["Melhores Pontos"], hoje = i["Hoje"], dias_seg = i["Dias Seguidos"], total_ponts = i["Total"], data_extract = i["Data_extract"])
        hist.save()
        
    now = datetime.now()
    html = """<hmtl>
                  <body>

                 	The time is %s.
                    </body></html>""" % now
    return HttpResponse(html)
