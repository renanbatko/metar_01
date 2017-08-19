#/usr/bin/env python
import urllib
import time
import datetime
from datetime import date	
codigo_oaci = raw_input("Codigo OACI: ")
hoje = date.today()
hoje = hoje.strftime("%d-%m-%Y")
dia = hoje.split("-", 2)[0]
mes = hoje.split("-", 2)[1]
ano = hoje.split("-", 2)[2]
#print dia
#print mes
#print ano
now = datetime.datetime.now()
hora = now.hour
#print hora
url_base = "https://www.ogimet.com/display_metars2.php?lugar="+codigo_oaci+"&tipo=ALL&ord=REV&nil=SI&fmt=html&ano="+str(ano)+"&mes="+str(mes)+"&day="+str(dia)+"&hora="+str(hora)+"&anof="+str(ano)+"&mesf="+str(mes)+"&dayf="+str(dia)+"&horaf="+str(hora)+"&minf=59&enviar=Ver"
#print url_base
#print "aqui ok"
pagina = urllib.urlopen(url_base)
#print "cheguei aqui"
for linha in pagina:
	if (linha.find("<pre>METAR") != -1):
		#print "achei"
		#print linha
		metar = linha.split("<pre>", 2)[1]
		metar = metar.split("<", 2)[0]
		print metar
