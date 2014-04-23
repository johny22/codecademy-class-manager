# -*- coding: cp1252 -*-
## Jones Rom�o

##Autor: Jones Rom�o Bezerra
##Descri��o: M�dulo que coleta dados em perfis do codecademy on-line.

from requests import get
from lxml import html
from datetime import datetime


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
            perfil = get(i) ## Faz uma requisi��o HTTP apartir da URL
            doc = html.document_fromstring(perfil.content) ## Documento HTML do Perfil
            bod = doc.body ## Corpo da p�gina



            
            ## Coleta de Dados
            nome = bod.find_class("full-name").pop()
            if(nome.text_content() == ""):
                nome = bod.find_class("username").pop()
            melhorP = bod.find_class("best-count").pop()
            hoje = bod.find_class("points-today-count").pop() ## Necessita de str.strip("\n ")
            pontos = bod.find_class("stat-count")
            dias_seg = pontos.pop()
            total_ponts = pontos.pop()

            ## Informa��es das trilhas
            track = bod.find_class("track-progress")
            track_n = bod.find_class("track-name")
            track_st = bod.find_class("stat-value")


            tracks = []
            

            
            for j in range(len(track)):
                tracks.append({"name" : track_n[j].text_content(),
                                   "percent": round(float(track[j].attrib['data-percent']) * 100),
                                   "last" : track_st[j].text_content().strip(" \n") + " ago"})
                
                

            ## Informa��es dos achievements
            perfil2 = get(i + "/achievements")
            doc2 = html.document_fromstring(perfil2.content)
            bod2 = doc2.body

            achievements = bod2.find_class("achievement")
            perf_achievements = []

            imgs = bod2.find_class("badge")
            urls = []
            for k in imgs:
                url = k.attrib['style'].split(":").pop()
                urls.append("http://www.codecademy.com" + url[4:-1])
            

            for j in range(len(achievements)):
                nomeA = achievements[j].find_class("name").pop()
                data = achievements[j].find_class("created_at").pop()
                perf_achievements.append({"nomeA": nomeA.text_content().strip(" \n "), "data" : datetime.strptime(data.text_content().strip(" \n "), "%B %d, %Y"),
                                          "imgUrl" : urls[j]})

            for l in achievements:
                if(l == []):
                    achievements.remove(l)
                

            DictD = dict() ## Dicion�rio que armazena os dados de cada aluno
            
            DictD["Nome"] = nome.text_content()
            DictD["Melhores Pontos"] = melhorP.text_content()
            DictD["Hoje"] = hoje.text_content().strip("\n ")
            DictD["Dias Seguidos"] = dias_seg.text_content()
            DictD["Total"] = total_ponts.text_content()
            DictD["perf_achievements"] = perf_achievements[:]
            DictD["tracks"] = tracks[:]
            DictD["Data_extract"] = datetime.now() ## Data da Coleta dos dados
                

            ## Colocar os perfis na lista

            self.perfis.append(DictD)
    
    
            
