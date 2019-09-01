#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import commands
import sys
import os
import re

DOMINIO = sys.argv[1]
LISTA = DOMINIO.split(".")
TAMANHO = len(LISTA)
SUFIXO = LISTA[TAMANHO-1]

print SUFIXO

if (SUFIXO == "br"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep ^expires: | cut -c14-17"))
    MES = int(commands.getoutput("whois "+DOMINIO+"  | grep ^expires: | cut -c18-19"))
    DIA = int(commands.getoutput("whois "+DOMINIO+"  | grep ^expires: | cut -c20-21"))

elif (SUFIXO == "com"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registrar Registration Expiration' | cut -c41-44"))
    MES = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registrar Registration Expiration' | cut -c46-47"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registrar Registration Expiration' | cut -c49-50"))

elif (SUFIXO == "cl"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Expiration date' | cut -c18-21"))
    MES = int(commands.getoutput("whois "+DOMINIO+" | grep 'Expiration date' | cut -c23-24"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Expiration date' | cut -c26-27"))

elif (SUFIXO == "ai"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "app"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "biz"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "bo"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Fecha de vencimiento' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Fecha de vencimiento' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Fecha de vencimiento' | cut -c31-32"))

elif (SUFIXO == "ca"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "club"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "biz"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "co"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "info"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "io"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "me"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "mo"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "mx"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Expiration Date' | cut -c20-23"))
    MES = int(commands.getoutput("whois "+DOMINIO+" | grep 'Expiration Date' | cut -c25-26"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Expiration Date' | cut -c28-29"))

elif (SUFIXO == "net"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registrar Registration Expiration Date' | cut -c41-44"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registrar Registration Expiration Date' | cut -c46-47"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registrar Registration Expiration Date' | cut -c49-50"))

elif (SUFIXO == "online"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "org"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "sh"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "travel"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "us"):
    ANO = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c23-26"))
    MES = int(commands.getoutput("whois "+DOMINIO+"| grep 'Registry Expiry Date' | cut -c28-29"))
    DIA = int(commands.getoutput("whois "+DOMINIO+" | grep 'Registry Expiry Date' | cut -c31-32"))

elif (SUFIXO == "as"):
    ANO_ATUAL = int(commands.getoutput("date +%Y"))
    ANO_VENCIMENTO = ANO_ATUAL+1
    ANO = ANO_VENCIMENTO
    MES = 1
    DIA = 23


EXPIRACAO = datetime.datetime( ANO, MES, DIA)
HOJE = datetime.datetime.today()
RESULTADO = EXPIRACAO - HOJE
DIAS_RESTANTES=RESULTADO.days

print RESULTADO
print EXPIRACAO
print HOJE
print DIAS_RESTANTES


sys.exit()
