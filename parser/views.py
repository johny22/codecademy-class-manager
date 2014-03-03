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
        try:
            perf = Perfil.objects.get(nome = i["Nome"])
            perf.nome = i["Nome"]
            perf.melhorP = i["Melhores Pontos"]
            perf.hoje = i["Hoje"]
            perf.dias_seg = i["Dias Seguidos"]
            perftotal_ponts = i["Total"]
            
        except Perfil.DoesNotExist:
            perf = Perfil(nome = i["Nome"], melhorP = i["Melhores Pontos"], hoje = i["Hoje"], dias_seg = i["Dias Seguidos"], total_ponts = i["Total"])
            perf.save()

        achi = i["perf_achievements"][:]
        
        for j in achi:
            achiv, created = Achievements.objects.get_or_create(perfil = Perfil.objects.get(nome=i["Nome"]), nome = j.pop(0), data = j.pop(0))
        

        tracks = i["tracks"][:]
        
        for k in tracks:

            try:
                trk = Track.objects.get(perfil = Perfil.objects.get(nome=i["Nome"]), nome = k["name"])
                trk.perfil = Perfil.objects.get(nome=i["Nome"])
                trk.nome = k["name"]
                trk.percent = k["percent"]
                trk.data = k["last"]
                trk.save()
                
            except Track.DoesNotExist:
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
