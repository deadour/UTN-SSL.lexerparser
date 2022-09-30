#importar librerias
import ply.lex as lex
import re 
import codecs
import os
import sys
import pathlib


reservadas = ['APERTURA_XML', 'VERSION_XML', 'ENCODING_VERSION', 'CIERRE_XML', 'APERTURA_RSS', 'VERSION_RSS', 'CIERRE_RSS', 'APERTURA_CHANNEL', 'CIERRE_CHANNEL', 'APERTURA_TITLE', 'CIERRE_TITLE', 'APERTURA_LINK', 'CIERRE_LINK', 'APERTURA_DESC', 'CIERRE_DESC', 'APERTURA_CAT', 'CIERRE_CAT', 'APERTURA_COPY', 'CIERRE_COPY', 'APERTURA_IMAG', 'CIERRE_IMAG', 'APERTURA_HEIGHT', 'CIERRE_HEIGHT', 'APERTURA_WIDTH', 'CIERRE_WIDTH', 'APERTURA_ITEM', 'CIERRE_ITEM', 'APERTURA_LANGUAGE', 'CIERRE_LANGUAGE', 'APERTURA_WEBMASTER', 'CIERRE_WEBMASTER', 'URL', 'APERTURA_ULTEDIT', 'CIERRE_ULTEDIT', 'APERTURA_AUTOR','CIERRE_AUTOR', 'APERTURA_BD', 'CIERRE_BD', 'APERTURA_GUID', 'CIERRE_GUID', 'APERTURA_TTL', 'CIERRE_TTL',
 ]

tokens = reservadas+['TXT', 'NUM',]


t_APERTURA_XML =r'\<\?xml'
t_VERSION_XML =r'\ version="1.0"'
t_ENCODING_VERSION= r'\ encoding="UTF-8"'
t_CIERRE_XML= r'\?\>'
#tokens rss
t_APERTURA_RSS=r'\<rss'
t_VERSION_RSS=r'\ version="2.0">'
t_CIERRE_RSS=r'\</rss>'
#tokens tags generales
t_APERTURA_CHANNEL = r'\<channel>'
t_CIERRE_CHANNEL = r'\</channel>' 
t_APERTURA_TITLE = r'\<title>'
t_CIERRE_TITLE = r'\</title>'
t_APERTURA_LINK=r'\<link>'
t_CIERRE_LINK=r'\</link>'
t_APERTURA_DESC=r'\<description>'
t_CIERRE_DESC=r'\</description>'
t_APERTURA_CAT=r'\<category>'
t_CIERRE_CAT=r'\</category>'
t_APERTURA_COPY=r'\<copyright>'
t_CIERRE_COPY=r'\</copyright>'
t_APERTURA_IMAG=r'\<image>'
t_CIERRE_IMAG=r'\</image>'
t_APERTURA_HEIGHT=r'\<height>'
t_CIERRE_HEIGHT=r'\</height>'
t_APERTURA_WIDTH=r'\<width>'
t_CIERRE_WIDTH=r'\</width>'
t_APERTURA_ITEM=r'\<item>'
t_CIERRE_ITEM=r'\</item>'
t_APERTURA_LANGUAGE=r'\<language>'
t_CIERRE_LANGUAGE=r'\</language>'
t_APERTURA_WEBMASTER=r'\<webMaster>'
t_CIERRE_WEBMASTER=r'\</webMaster>'
t_APERTURA_ULTEDIT=r'\<pubDate>'
t_CIERRE_ULTEDIT=r'\</pubDate>'
t_APERTURA_AUTOR=r'\<author>'
t_CIERRE_AUTOR=r'\</author>'
t_APERTURA_BD=r'\<lastBuildDate>'
t_CIERRE_BD=r'\</lastBuildDate>'
t_APERTURA_GUID=r'\<guid>'
t_CIERRE_GUID=r'\</guid>'
t_APERTURA_TTL=r'\<ttl>'
t_CIERRE_TTL=r'\</ttl>'
t_ignore = '\t'

#definición de tokens simbolos
def t_URL(t):
  r'(https|http|ftp|ftps)://(?:[a-zA-Z0-9]*[.][a-zA-Z]*[a-zA-Z.0-9?%/_=:#&$-]*)'
  t.type='URL'
  return t

#definición de tokens de cadena de texto
def t_TXT(t): 
	r'[a-zA-Z][a-zA-Z.,:\:\+\t áéíóú0-9]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value

	return t


#definición de tokens de cadena de numeros
def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

#definición de tokens de cadena de URL

    
#definición de salto de pagina
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)


def t_COMMENT(t):
	r'\#.*'
	pass

def t_error(t):
	#print (" LexToken(SALTODEPAG)%s'" % t.value[0])
	t.lexer.skip(1)

analizador = lex.lex()