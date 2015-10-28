# -*- coding: utf-8 -*-
__author__ = 'pabloholanda'
import urllib2
from time import sleep
import yaml
import socket


def carregar_configuracoes():
    with open("config.yaml", "r") as configuracoes:
        data = yaml.load(configuracoes)


while True:
    try:
        # Tenta acessar a URL dentro do timeout definido em segundos
        code = urllib2.urlopen("http://pmaq.lais.huol.ufrn.br/amaq", timeout=1).getcode()
    except urllib2.URLError as e:
        # Caso não consiga acessar, checamos o tipo de erro
        if str(e.reason) == 'timed out':
            print "Timed out"
        elif str(e.reason) == '[Errno 61] Connection refused':
            print "Refused"
    except socket.timeout as e:
        if str(e) == 'timed out':
            print "socket timed out"
    except:
        pass

    sleep(10)
