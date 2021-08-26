# -*- coding: utf-8 -*-
import os
from http.server import HTTPServer, CGIHTTPRequestHandler
#каталог с файлами HTML и подкаталогом cgi-bin для сценариев
webdir = r'..\5'
port = 80
os.chdir(webdir) #перейти в корневой веб-каталог
srvraddr = ('', port) # имя хоста (или IP), номер порта
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever() #обслуживать клиентов до завершения

