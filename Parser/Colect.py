# -*- coding: cp1252 -*-
##Autor: Jones Romão Bezerra
##Descrição: Módulo que coleta dados em perfis do codecademy on-line.

from requests import get
from lxml import html


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
            perfil = get(i) ## Faz uma requisição HTTP apartir da URL
            doc = html.document_fromstring(perfil.content) ## Documento HTML do Perfil
            bod = doc.body ## Corpo da página

            ## Coleta de Dados
            nome = bod.find_class("full-name").pop()
            if(nome.text_content() == ""):
                nome = bod.find_class("username").pop()
            melhorP = bod.find_class("best-count").pop()
            hoje = bod.find_class("count-right").pop() ## Necessita de str.strip("\n ")
            pontos = bod.find_class("stat-count")
            dias_seg = pontos.pop()
            total_ponts = pontos.pop()

            DictD = dict() ## Dicionário que armazena os dados de cada aluno
            
            DictD["Nome"] = nome.text_content()
            DictD["Melhor Pontuação"] = melhorP.text_content()
            DictD["Hoje"] = hoje.text_content().strip("\n ")
            DictD["Dias Seguidos"] = dias_seg.text_content()
            DictD["Total"] = total_ponts.text_content()

            ## Colocar os perfis na lista

            self.perfis.append(DictD)
            



