# -*- coding: utf-8 -*-
__author__ = 'pabloholanda'
import urllib2
from time import sleep
import yaml
import socket
import sys
import signal


def carregar_configuracoes():
    with open("config.yaml", "r") as configuracoes:
        data = yaml.load(configuracoes)


def enviar_sms(tipo_erro):

    with open("config.yaml", "r") as destinatarios:
        data = yaml.load(destinatarios)

    for destinatario in data['destinatarios']:
        destino = '/var/spool/sms/outgoing/%s.txt' % destinatario
        arquivo = open(destino, 'a')
        arquivo.write("To: %s \n\nOlá %s, estamos enfrentando o seguinte erro no servidor do AMAQ: %s." %
                      (data['destinatarios'][destinatario]['telefone'], destinatario, tipo_erro))
        arquivo.close()
        sleep(0.5)


def signal_handler(signal, frame):
    print('Você apertou Ctrl+C!')
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        try:
            # Tenta acessar a URL dentro do timeout definido em segundos
            code = urllib2.urlopen("http://pmaq.lais.huol.ufrn.br/amaq", timeout=10).getcode()
        except urllib2.URLError as e:
            # Caso não consiga acessar, checamos o tipo de erro
            if str(e.reason) == 'timed out':
                enviar_sms(str(e.reason))
            elif str(e.reason) == '[Errno 61] Connection refused':
                 enviar_sms(str(e.reason))
        except socket.timeout as e:
            if str(e) == 'timed out':
                 enviar_sms(str(e.reason))
        except:
            pass

        sleep(60)
