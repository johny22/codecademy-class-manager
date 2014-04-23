# -*- coding: utf-8 -*-
## Jones Romão 


from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render_to_response
from Colect import Collector
from codecademy.parser2.models import *




parser = Collector("/home/jones/codecademy/codecademy/parser2/perfis_codecademy")
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
            perf.total_ponts = i["Total"]
            perf.save()
            
        except Perfil.DoesNotExist:
            perf = Perfil(nome = i["Nome"], melhorP = i["Melhores Pontos"], hoje = i["Hoje"], dias_seg = i["Dias Seguidos"], total_ponts = i["Total"])
            perf.save()


        achi = i["perf_achievements"][:]
        for j in achi:
            achiv, created = Achievements.objects.get_or_create(perfil = Perfil.objects.get(nome=i["Nome"]), nome = j["nomeA"], data = j["data"], imgUrl = j["imgUrl"])
        

        tracks = i["tracks"][:]
        
        for k in tracks:

            try:
                trk = Track.objects.get(perfil = Perfil.objects.get(nome=i["Nome"]), nome = k["name"])
                trk.nome = k["name"]
                trk.percent = k["percent"]
                trk.data = k["last"]
                trk.save()
                
            except Track.DoesNotExist:
                trk = Track(perfil = Perfil.objects.get(nome=i["Nome"]), nome = k["name"], percent = k["percent"], data = k["last"])
                trk.save()

        hist = History(perfil = Perfil.objects.get(nome=i["Nome"]), melhorP = i["Melhores Pontos"], hoje = i["Hoje"], dias_seg = i["Dias Seguidos"], total_ponts = i["Total"], data_extract = i["Data_extract"])
        hist.save()
        
    html = """<hmtl>
                  <body>

                 	<h1>Atualização efetuada com sucesso!</h1>
                    </body></html>"""
    return HttpResponse(html)



def index(request):
	now = datetime.now()
	Perfis = Perfil.objects.all()
	Nomes = ""
	Pontos = []
	Pks = []
	for i in range(len(Perfis)):
		if(Nomes == ""):
			Nomes += Perfis[i].nome
		else:
			Nomes += "." + Perfis[i].nome
		Pontos.append(Perfis[i].total_ponts)
		Pks.append(Perfis[i].pk)
	return render_to_response('index.html', locals())	

		
		
		
	

def charts(request, PK):
	historico = History.objects.all().order_by('data_extract')
	datas = ""
	Pk = 0
	for i in range(len(historico)):
		if(historico[i].perfil.pk == int(PK)):
			data = str(historico[i].data_extract.day) + "/" + str(historico[i].data_extract.month)  + "/" + str(historico[i].data_extract.year)
			if (Pk != historico[i].pk):
				if(datas == ""):
					datas += data
				else:
					datas +=  " " + data
			Pk = historico[i].pk

	ordered_hist = History.objects.all().order_by('perfil')
	Pontos = []
	perf = Perfil.objects.get(pk=int(PK))
	Nome = perf.nome
	Melhor = perf.melhorP
        Hoje = perf.hoje
        Dias_seg = perf.dias_seg
        Total = perf.total_ponts

	for i in range(len(ordered_hist)):
		if(ordered_hist[i].perfil.pk == int(PK)):
			Pontos.append(ordered_hist[i].total_ponts)
	
	return render_to_response('charts.html', locals())

def badges(request, PK):
	badges = Achievements.objects.all().order_by('perfil')
	datas = ""
	nomes = ""
	imgUrl = ""

	
	for i in range(len(badges)):
		if(badges[i].perfil.pk == int(PK)):
			data = str(badges[i].data.day) + "/" + str(badges[i].data.month)  + "/" + str(badges[i].data.year)
			if(datas == ""):
                            datas += data
			else:
			    datas +=  " " + data

	for i in range(len(badges)):
		if(badges[i].perfil.pk == int(PK)):
                    nome = badges[i].nome
                    if(nomes == ""):
                        nomes += nome
                    else:
                        nomes +=  "." + nome

        for i in range(len(badges)):
		if(badges[i].perfil.pk == int(PK)):
                    url = badges[i].imgUrl
                    if(imgUrl == ""):
                        imgUrl += url
                    else:
                        imgUrl +=  " " + url
                    
        Nome = Perfil.objects.get(pk=int(PK)).nome
	qt = len(nomes[:].split("."))

	return render_to_response('badges.html', locals())

def track_percent(request, PK):
	now = datetime.now()
	tracks = Track.objects.all()
	track_names = ""
	percents = []
	for i in tracks:
		if(i.perfil.pk == int(PK)):
			percents.append(i.percent)
			if(track_names == ""):
				track_names += i.nome
			else:
				track_names += "." + i.nome
	return render_to_response('track_percent.html', locals())







