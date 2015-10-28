# -*- coding: utf-8 -*-
__author__ = 'pabloholanda'
import urllib2
from time import sleep

while True:
    try:
        # Tenta acessar a URL dentro do timeout definido em segundos
        code = urllib2.urlopen("http://127.0.0.1:8000", timeout=1).getcode()
    except urllib2.URLError as e:
        # Caso não consiga acessar, checamos o tipo de erro
        if str(e.reason) == 'timed out':
            print "Timed out"
        elif str(e.reason) == '[Errno 61] Connection refused':
            print "Refused"

    sleep(10)
