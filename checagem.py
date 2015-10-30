# -*- coding: utf-8 -*-
__author__ = 'pabloholanda'
import urllib2
from time import sleep
import yaml
import socket
import sys
import signal
import os


def carregar_configuracoes():
    with open("config.yaml", "r") as configuracoes:
        return yaml.load(configuracoes)


def enviar_sms(data, projeto, tipo_erro):
    for destinatario in data['destinatarios']:
        destino = '/var/spool/sms/outgoing/%s.txt' % destinatario
        arquivo = open(destino, 'a')
        arquivo.write("To: %s \n\nOlá %s, estamos enfrentando o seguinte erro no servidor do %s: %s." %
                      (data['destinatarios'][destinatario]['telefone'], destinatario, projeto, tipo_erro))
        arquivo.close()
        sleep(0.5)


def signal_handler(signal, frame):
    print('Você apertou Ctrl+C!')
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    print "Process ID = ", os.getpid()
    data = carregar_configuracoes()

    while True:
        for projeto in data['projetos']:
            try:
                # Tenta acessar a URL dentro do timeout definido em segundos
                code = urllib2.urlopen(data['projetos'][projeto]['url'], timeout=3).getcode()
            except urllib2.URLError as e:
                # Caso não consiga acessar, checamos o tipo de erro
                if str(e.reason) == 'timed out':
                    enviar_sms(data['projetos'][projeto], projeto, str(e.reason))
                elif str(e.reason) == '[Errno 61] Connection refused':
                     enviar_sms(data['projetos'][projeto], projeto, str(e.reason))
            except socket.timeout as e:
                if str(e) == 'timed out':
                     enviar_sms(data['projetos'][projeto], projeto, str(e))
            except:
                enviar_sms(data['projetos'][projeto], projeto, 'Valha-me deus, erro desconhecido')

        sleep(120)
