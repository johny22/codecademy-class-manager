# -*- coding: utf-8 -*-
## Jones Romão

##Autor: Jones Romão Bezerra
##Descrição: Módulo que coleta dados em perfis do codecademy.

from requests import get
from lxml import html
from datetime import datetime

import pdb

class Collector:
    def __init__(self, path):
        self.arq = open(path, "r+")
        self.urlist = []
        self.perfis = []

    def gerarURLs(self):
        self.urlist = self.arq.readlines()
        for i in range(len(self.urlist)):
            self.urlist[i] = self.urlist[i].strip("\n")

    def colectPerfis(self):
        for i in self.urlist:
            perfil = get(i)
            document = html.document_fromstring(perfil.content)
            content = document.body

            ## Coleta de Dados
            nome = content.find_class("username")
            if nome:
                nome = content.find_class("username").pop()
                nome = nome.text_content().strip(' \n')
            
            print('Coletando perfil de "%s"...' % nome)
            profile_time = content.find_class("profile-time")
            #pdb.set_trace()
            prof_children = profile_time[0].getchildren()
            
            melhorP = 0
            dias_seg = 0
            hoje = prof_children[2].getchildren()[0].text_content()
            #pontos = content.find_class("stat-count")
            total_score = prof_children[1].getchildren()[0].text_content()

            ## Informações das trilhas
            # track = content.find_class("track-progress")
            # track_n = content.find_class("track-name")
            # track_st = content.find_class("stat-value")

            tracks = []
            
            # for j in range(len(track)):
            #     tracks.append({"name" : track_n[j].text_content(),
            #                        "percent": round(float(track[j].attrib['data-percent']) * 100),
            #                        "last" : track_st[j].text_content().strip(" \n") + " ago"})
                
                

            ## Informações dos achievements
            # perfil2 = get(i + "/achievements")
            # doc2 = html.document_fromstring(perfil2.content)
            # bod2 = doc2.body

            # achievements = bod2.find_class("achievement")
            perf_achievements = []

            # imgs = bod2.find_class("badge")
            # urls = []
            # for k in imgs:
            #     url = k.attrib['style'].split(":").pop()
            #     urls.append("http://www.codecademy.com" + url[4:-1])
            

            # for j in range(len(achievements)):
            #     nomeA = achievements[j].find_class("name").pop()
            #     data = achievements[j].find_class("created_at").pop()
            #     perf_achievements.append({"nomeA": nomeA.text_content().strip(" \n "),
		    #                               "data" : datetime.now().strftime("%B %d, %Y"),
            #                               "imgUrl" : urls[j]})

            # for l in achievements:
            #     if(l == []):
            #         achievements.remove(l)
                

            DictD = dict() ## Dicionário que armazena os dados de cada aluno
            
            DictD["Nome"] = nome
            DictD["Dias Seguidos"] = dias_seg
            DictD["Melhores Pontos"] = melhorP
            DictD["Hoje"] = hoje
            DictD["Total"] = total_score
            DictD["perf_achievements"] = perf_achievements[:]
            DictD["tracks"] = tracks[:]
            DictD["Data_extract"] = datetime.now() ## Data da Coleta dos dados

            self.perfis.append(DictD)
    
    
            
