import ply.yacc as yacc
import ply.lex as lex
#importo las mismas librerias que el lexer
import os
import codecs
import re
from lex import tokens
from sys import stdin
import msvcrt

titulo_nro=0
head=0
text_gen=0
imag_gen=0
link_gen=0
correcto=0
doc_html =""


#LEXER
#-------------------------------------------------#


reservadas = ['APERTURA_XML', 'VERSION_XML', 'ENCODING_VERSION', 'CIERRE_XML', 'APERTURA_RSS', 'VERSION_RSS', 'CIERRE_RSS', 'APERTURA_CHANNEL', 'CIERRE_CHANNEL', 'APERTURA_TITLE', 'CIERRE_TITLE', 'APERTURA_LINK', 'CIERRE_LINK', 'APERTURA_DESC', 'CIERRE_DESC', 'APERTURA_CAT', 'CIERRE_CAT', 'APERTURA_COPY', 'CIERRE_COPY', 'APERTURA_IMAG', 'CIERRE_IMAG', 'APERTURA_HEIGHT', 'CIERRE_HEIGHT', 'APERTURA_WIDTH', 'CIERRE_WIDTH', 'APERTURA_ITEM', 'CIERRE_ITEM', 'APERTURA_LANGUAGE', 'CIERRE_LANGUAGE', 'APERTURA_WEBMASTER', 'CIERRE_WEBMASTER', 'URL', 'APERTURA_ULTEDIT', 'CIERRE_ULTEDIT', 'APERTURA_AUTOR','CIERRE_AUTOR', 'APERTURA_BD', 'CIERRE_BD', 'APERTURA_GUID', 'CIERRE_GUID', 'APERTURA_TTL', 'CIERRE_TTL',
 ]

tokens = reservadas+['NUM','TXT']

t_APERTURA_XML =r'\<\?xml'
t_VERSION_XML =r'\ version="1.0"'
t_ENCODING_VERSION= r'\ encoding="UTF-8"'
t_CIERRE_XML= r'\?\>'
#tokens rss
#t_APERTURA_RSS=r'\<rss'
t_VERSION_RSS=r'\ version="2.0">'
#t_CIERRE_RSS=r'\</rss>'
#tokens tags generales
#t_APERTURA_CHANNEL = r'\<channel>'
t_CIERRE_CHANNEL = r'\</channel>' 
#t_APERTURA_TITLE = r'\<title>'
#t_CIERRE_TITLE = r'\</title>'
#t_APERTURA_LINK=r'\<link>'
#t_CIERRE_LINK=r'\</link>'
#t_APERTURA_DESC=r'\<description>'
#t_CIERRE_DESC=r'\</description>'
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
#t_APERTURA_ITEM=r'\<item>'
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

#   definición de tags que se escriben en el html
#---------------------------------------#

def t_APERTURA_RSS(t):
    r'<rss'
    doc_html.write("<html>")
    return t
  
def t_CIERRE_RSS(t):
    r'</rss>'
    global head
    if head == 0:
        doc_html.write("</head>\n<body>")

    doc_html.write("</body>\n</html>")
    return t

def t_APERTURA_CHANNEL(t):
    r'<channel>'
    doc_html.write("<head>")
    return t

def t_APERTURA_ITEM(t):
    r'<item>'
    global head
    if head == 0:
        doc_html.write("</head>\n<body>")
    head=+1
    return t

def t_APERTURA_TITLE(t):
    r'<title>'
    global text_gen
    text_gen=1
    global titulo_nro
    global imag_gen
    if titulo_nro<=1:      
        doc_html.write("<H1>")
        titulo_nro+=1
    else:
        if imag_gen == 0:
            doc_html.write("<H3>")
    return t


def t_CIERRE_TITLE(t):
    r'</title>'
    global text_gen
    text_gen=0
    global titulo_nro
    global imag_gen
    if titulo_nro<=1:      
        doc_html.write("</H1>")
        titulo_nro+=1
    else:
        if imag_gen == 0:
            doc_html.write("</H3>")
    return t


def t_APERTURA_LINK(t):
    r'<link>'
    global link_gen
    if link_gen<=1:
        doc_html.write("<a href='")
        link_gen+=0
    return t

def t_CIERRE_LINK(t):
    r'</link>'
    global link_gen
    if link_gen<=1:      
        doc_html.write("'>LINK</a>")
        link_gen+=0
    return t

def t_APERTURA_DESC(t):
    r'<description>'
    global text_gen
    text_gen=1
    doc_html.write("<p>")
    return t

def t_CIERRE_DESC(t):
    r'</description>'
    global text_gen
    text_gen=0
    doc_html.write("</p>")
    return t
  
#definición de tokens de cadena de numeros
def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

#definición de tokens de cadena de URL
def t_URL(t): 

  r'(https|http|ftp|ftps)://(?:[a-zA-Z0-9]*[.][a-zA-Z]*[a-zA-Z.0-9?%/_=:#&$-]*)'
  
  
  if link_gen==0:
     doc_html.write(t.value)
  return t

def t_TAB(t):
  r'\t'
  doc_html.write("\t")
  pass

def t_ESPACIO(t):
    r'\ '
    doc_html.write(" ")
    pass

#definición de salto de pagina
def t_newline(t):
    r'\n+'
    global lineas
    t.lexer.lineno += len(t.value)
    doc_html.write(os.linesep)


def t_COMMENT(t):
	r'\#.*'
	pass

#definición de tokens de cadena de texto
def t_TXT(t): 
 r'[a-zA-Z][a-zA-Z.,:\:\+\t áéíóú0-9]*'
 if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
    
 if text_gen==1 and imag_gen == 0:
   doc_html.write(t.value)
 return t
  
def t_error(t):
    t.lexer.skip(1)

#--------------------------------------#


#-------------------------------------------------#
#_------------------------#

#Sigma
def p_sigma(p):
	'''sigma : aperturaxml aperturarss'''

#xml
def p_aperturaxml(p):
	'''aperturaxml : APERTURA_XML VERSION_XML ENCODING_VERSION CIERRE_XML'''
	print ("TAG Apertura XML")


#rss
def p_aperturarss(p):
	'''aperturarss : APERTURA_RSS VERSION_RSS canal CIERRE_RSS'''
	print ("TAG Apertura RSS")

#tag CHANNEL
def p_canal_basico(p):
	'''canal : APERTURA_CHANNEL titulo LINK desc item CIERRE_CHANNEL'''
	print ("TAG channel")
  
def p_canal_basico2(p):
	'''canal : APERTURA_CHANNEL titulo desc LINK item CIERRE_CHANNEL'''
	print ("TAG channel")
  
def p_canal_opcionales(p):
	'''canal : APERTURA_CHANNEL titulo LINK desc opc item CIERRE_CHANNEL'''
	print ("TAG channel")
  
def p_canal_opcionales2(p):
	'''canal : APERTURA_CHANNEL titulo desc LINK opc item CIERRE_CHANNEL'''
	print ("TAG channel")

def p_item(p):
  '''item : APERTURA_ITEM titulo LINK desc CIERRE_ITEM'''
  print("TAG ITEM")

def p_item2(p):
  '''item : APERTURA_ITEM titulo desc LINK CIERRE_ITEM'''
  print("TAG ITEM")
def p_item_recursivo(p):
  '''item : APERTURA_ITEM titulo LINK desc CIERRE_ITEM item'''
  print("TAG ITEM")

def p_item_recursivo2(p):
  '''item : APERTURA_ITEM titulo desc LINK CIERRE_ITEM item'''
  print("TAG ITEM")

def p_item_opcionales(p):
  '''item : APERTURA_ITEM titulo LINK desc opc CIERRE_ITEM'''
  print("TAG ITEM")

def p_item_opcionales2(p):
  '''item : APERTURA_ITEM titulo desc LINK opc CIERRE_ITEM'''
  print("TAG ITEM")

def p_item_opcionales_recursivo(p):
  '''item : APERTURA_ITEM titulo LINK desc opc CIERRE_ITEM item'''
  print("TAG ITEM")
def p_item_opcionales_recursivo2(p):
  '''item : APERTURA_ITEM titulo desc LINK opc CIERRE_ITEM item'''
  print("TAG ITEM")

def p_titulo(p):
	'''titulo : APERTURA_TITLE TXT CIERRE_TITLE'''
	print ("TAG titulo")

def p_LINK(p):
	'''LINK : APERTURA_LINK URL CIERRE_LINK'''
	print ("TAG link")

def p_desc(p):
	'''desc : APERTURA_DESC TXT CIERRE_DESC'''
	print ("TAG descripción")

#                     TAGS OPCIONALES
#--------------------------------------------------------------#
#TAG CATEGORIA
def p_opc1(p):
	'''opc : categoria'''

def p_categoria(p):
	'''categoria : APERTURA_CAT TXT CIERRE_CAT'''
	print ("TAG categoria")

#TAG COPYRIGHT
def p_opc2(p):
	'''opc : copyright'''

def p_copyright(p):
	'''copyright : APERTURA_COPY TXT CIERRE_COPY'''
	print ("TAG copyright")

#TAG IMAGE
def p_opc3(p):
	'''opc : image'''

def p_image1(p):
	'''image : APERTURA_IMAG URL titulo LINK CIERRE_IMAG'''
	print ("TAG image")

#imagen con elementos opcionales
def p_image2(p):
	'''image : APERTURA_IMAG URL titulo LINK opcimag CIERRE_IMAG'''
	print ("TAG image")

#elementos opcionales de imagen (largo-ancho, largo, ancho)
def p_opcimag1(p):
	'''opcimag : height width'''

def p_opcimag2(p):
	'''opcimag : height'''

def p_opcimag3(p):
	'''opcimag : width'''

def p_height(p):
	'''height : APERTURA_HEIGHT NUM CIERRE_HEIGHT'''

def p_width(p):
	'''width : APERTURA_WIDTH NUM CIERRE_WIDTH'''

def p_opc4(p):
	'''opc : lenguaje'''

def p_lenguaje(p):
	'''lenguaje : APERTURA_LANGUAGE TXT CIERRE_LANGUAGE'''
	print ("TAG language")

def p_opc5(p):
	'''opc : webmaster'''

def p_WEBMASTER(p):
	'''webmaster : APERTURA_WEBMASTER TXT CIERRE_WEBMASTER'''
	print ("TAG webmaster") 

def p_opc6(p):
	'''opc : ultedit'''

def p_pubdate(p):
	'''ultedit : APERTURA_ULTEDIT TXT CIERRE_ULTEDIT'''
	print ("TAG pubdate")

def p_opc7(p):
	'''opc : autor'''

def p_autor(p):
	'''autor : APERTURA_AUTOR TXT CIERRE_AUTOR'''
	print ("TAG author")

def p_opc8(p):
	'''opc : lastbuilddate'''

def p_lastbuilddate(p):
	'''lastbuilddate : APERTURA_BD TXT CIERRE_BD'''
	print ("TAG lastBuildDate")

def p_opc9(p):
	'''opc : guid'''

def p_guid(p):
	'''guid : APERTURA_GUID TXT CIERRE_GUID'''
	print ("TAG guid")

def p_opc10(p):
	'''opc : ttl'''

def p_ttl(p):
	'''ttl : APERTURA_TTL TXT CIERRE_TTL'''
	print ("TAG ttl")
# fin elementos opcionales ----------------------------------------#

def p_error(p):
  global correcto
  correcto += 1
  print ("Error de sintaxis "), p
  print ("Error en la linea "+str(p.lineno))
  
def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Tags reconocidos en el archivo \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

print ("---------ANALIZADOR SINTÁCTICO---------")
print ("Por favor, ingrese por teclado la dirección de la carpeta en donde se encuntra los archivos.rss")
directorio = input() +'/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()

result = parser.parse(cadena)


print (result)

if correcto == 0:
  print ('felicidades, su código funciona correctamente')
  doc_html = open(archivo.replace(".rss",".html"), "w")
  doc_html.write("<!DOCTYPE html>")
  print ("---------ANALIZADOR LÉXICO---------")
  analizador = lex.lex()

  analizador.input(cadena)

  while True:
	  tok = analizador.token()
	  if not tok : break
	  print (tok)

doc_html.close()
msvcrt.getch()