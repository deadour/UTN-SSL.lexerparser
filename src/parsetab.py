
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'APERTURA_AUTOR APERTURA_BD APERTURA_CAT APERTURA_CHANNEL APERTURA_COPY APERTURA_DESC APERTURA_GUID APERTURA_HEIGHT APERTURA_IMAG APERTURA_ITEM APERTURA_LANGUAGE APERTURA_LINK APERTURA_RSS APERTURA_TITLE APERTURA_TTL APERTURA_ULTEDIT APERTURA_WEBMASTER APERTURA_WIDTH APERTURA_XML CIERRE_AUTOR CIERRE_BD CIERRE_CAT CIERRE_CHANNEL CIERRE_COPY CIERRE_DESC CIERRE_GUID CIERRE_HEIGHT CIERRE_IMAG CIERRE_ITEM CIERRE_LANGUAGE CIERRE_LINK CIERRE_RSS CIERRE_TITLE CIERRE_TTL CIERRE_ULTEDIT CIERRE_WEBMASTER CIERRE_WIDTH CIERRE_XML ENCODING_VERSION NUM TXT URL VERSION_RSS VERSION_XMLsigma : aperturaxml aperturarssaperturaxml : APERTURA_XML VERSION_XML ENCODING_VERSION CIERRE_XMLaperturarss : APERTURA_RSS VERSION_RSS canal CIERRE_RSScanal : APERTURA_CHANNEL titulo LINK desc item CIERRE_CHANNELcanal : APERTURA_CHANNEL titulo desc LINK item CIERRE_CHANNELcanal : APERTURA_CHANNEL titulo LINK desc opc item CIERRE_CHANNELcanal : APERTURA_CHANNEL titulo desc LINK opc item CIERRE_CHANNELitem : APERTURA_ITEM titulo LINK desc CIERRE_ITEMitem : APERTURA_ITEM titulo desc LINK CIERRE_ITEMitem : APERTURA_ITEM titulo LINK desc CIERRE_ITEM itemitem : APERTURA_ITEM titulo desc LINK CIERRE_ITEM itemitem : APERTURA_ITEM titulo LINK desc opc CIERRE_ITEMitem : APERTURA_ITEM titulo desc LINK opc CIERRE_ITEMitem : APERTURA_ITEM titulo LINK desc opc CIERRE_ITEM itemitem : APERTURA_ITEM titulo desc LINK opc CIERRE_ITEM itemtitulo : APERTURA_TITLE TXT CIERRE_TITLELINK : APERTURA_LINK URL CIERRE_LINKdesc : APERTURA_DESC TXT CIERRE_DESCopc : categoriacategoria : APERTURA_CAT TXT CIERRE_CATopc : copyrightcopyright : APERTURA_COPY TXT CIERRE_COPYopc : imageimage : APERTURA_IMAG URL titulo LINK CIERRE_IMAGimage : APERTURA_IMAG URL titulo LINK opcimag CIERRE_IMAGopcimag : height widthopcimag : heightopcimag : widthheight : APERTURA_HEIGHT NUM CIERRE_HEIGHTwidth : APERTURA_WIDTH NUM CIERRE_WIDTHopc : lenguajelenguaje : APERTURA_LANGUAGE TXT CIERRE_LANGUAGEopc : webmasterwebmaster : APERTURA_WEBMASTER TXT CIERRE_WEBMASTERopc : ulteditultedit : APERTURA_ULTEDIT TXT CIERRE_ULTEDITopc : autorautor : APERTURA_AUTOR TXT CIERRE_AUTORopc : lastbuilddatelastbuilddate : APERTURA_BD TXT CIERRE_BDopc : guidguid : APERTURA_GUID TXT CIERRE_GUIDopc : ttlttl : APERTURA_TTL TXT CIERRE_TTL'
    
_lr_action_items = {'APERTURA_XML':([0,],[3,]),'$end':([1,4,12,],[0,-1,-3,]),'APERTURA_RSS':([2,11,],[5,-2,]),'VERSION_XML':([3,],[6,]),'VERSION_RSS':([5,],[7,]),'ENCODING_VERSION':([6,],[8,]),'APERTURA_CHANNEL':([7,],[10,]),'CIERRE_XML':([8,],[11,]),'CIERRE_RSS':([9,52,65,67,80,],[12,-4,-5,-6,-7,]),'APERTURA_TITLE':([10,27,57,],[14,14,14,]),'APERTURA_LINK':([13,16,24,51,54,69,72,],[17,17,-16,-18,17,17,17,]),'APERTURA_DESC':([13,15,24,50,54,68,],[18,18,-16,-17,18,18,]),'TXT':([14,18,38,39,41,42,43,44,45,46,47,],[19,23,55,56,58,59,60,61,62,63,64,]),'URL':([17,40,],[22,57,]),'CIERRE_TITLE':([19,],[24,]),'APERTURA_ITEM':([20,21,26,28,29,30,31,32,33,34,35,36,37,49,50,51,70,71,73,74,75,76,77,78,79,84,86,88,95,97,98,],[27,27,27,-19,-21,-23,-31,-33,-35,-37,-39,-41,-43,27,-17,-18,-20,-22,-32,-34,-36,-38,-40,-42,-44,27,27,-24,27,27,-25,]),'APERTURA_CAT':([20,21,50,51,81,82,],[38,38,-17,-18,38,38,]),'APERTURA_COPY':([20,21,50,51,81,82,],[39,39,-17,-18,39,39,]),'APERTURA_IMAG':([20,21,50,51,81,82,],[40,40,-17,-18,40,40,]),'APERTURA_LANGUAGE':([20,21,50,51,81,82,],[41,41,-17,-18,41,41,]),'APERTURA_WEBMASTER':([20,21,50,51,81,82,],[42,42,-17,-18,42,42,]),'APERTURA_ULTEDIT':([20,21,50,51,81,82,],[43,43,-17,-18,43,43,]),'APERTURA_AUTOR':([20,21,50,51,81,82,],[44,44,-17,-18,44,44,]),'APERTURA_BD':([20,21,50,51,81,82,],[45,45,-17,-18,45,45,]),'APERTURA_GUID':([20,21,50,51,81,82,],[46,46,-17,-18,46,46,]),'APERTURA_TTL':([20,21,50,51,81,82,],[47,47,-17,-18,47,47,]),'CIERRE_LINK':([22,],[50,]),'CIERRE_DESC':([23,],[51,]),'CIERRE_CHANNEL':([25,48,53,66,84,86,94,95,96,97,102,103,],[52,65,67,80,-8,-9,-10,-12,-11,-13,-14,-15,]),'CIERRE_ITEM':([28,29,30,31,32,33,34,35,36,37,50,51,70,71,73,74,75,76,77,78,79,81,82,85,87,88,98,],[-19,-21,-23,-31,-33,-35,-37,-39,-41,-43,-17,-18,-20,-22,-32,-34,-36,-38,-40,-42,-44,84,86,95,97,-24,-25,]),'CIERRE_IMAG':([50,83,89,90,91,99,104,105,],[-17,88,98,-27,-28,-26,-29,-30,]),'APERTURA_HEIGHT':([50,83,],[-17,92,]),'APERTURA_WIDTH':([50,83,90,104,],[-17,93,93,-29,]),'CIERRE_CAT':([55,],[70,]),'CIERRE_COPY':([56,],[71,]),'CIERRE_LANGUAGE':([58,],[73,]),'CIERRE_WEBMASTER':([59,],[74,]),'CIERRE_ULTEDIT':([60,],[75,]),'CIERRE_AUTOR':([61,],[76,]),'CIERRE_BD':([62,],[77,]),'CIERRE_GUID':([63,],[78,]),'CIERRE_TTL':([64,],[79,]),'NUM':([92,93,],[100,101,]),'CIERRE_HEIGHT':([100,],[104,]),'CIERRE_WIDTH':([101,],[105,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sigma':([0,],[1,]),'aperturaxml':([0,],[2,]),'aperturarss':([2,],[4,]),'canal':([7,],[9,]),'titulo':([10,27,57,],[13,54,72,]),'LINK':([13,16,54,69,72,],[15,21,68,82,83,]),'desc':([13,15,54,68,],[16,20,69,81,]),'item':([20,21,26,49,84,86,95,97,],[25,48,53,66,94,96,102,103,]),'opc':([20,21,81,82,],[26,49,85,87,]),'categoria':([20,21,81,82,],[28,28,28,28,]),'copyright':([20,21,81,82,],[29,29,29,29,]),'image':([20,21,81,82,],[30,30,30,30,]),'lenguaje':([20,21,81,82,],[31,31,31,31,]),'webmaster':([20,21,81,82,],[32,32,32,32,]),'ultedit':([20,21,81,82,],[33,33,33,33,]),'autor':([20,21,81,82,],[34,34,34,34,]),'lastbuilddate':([20,21,81,82,],[35,35,35,35,]),'guid':([20,21,81,82,],[36,36,36,36,]),'ttl':([20,21,81,82,],[37,37,37,37,]),'opcimag':([83,],[89,]),'height':([83,],[90,]),'width':([83,90,],[91,99,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sigma","S'",1,None,None,None),
  ('sigma -> aperturaxml aperturarss','sigma',2,'p_sigma','main.py',12),
  ('aperturaxml -> APERTURA_XML VERSION_XML ENCODING_VERSION CIERRE_XML','aperturaxml',4,'p_aperturaxml','main.py',19),
  ('aperturarss -> APERTURA_RSS VERSION_RSS canal CIERRE_RSS','aperturarss',4,'p_aperturarss','main.py',24),
  ('canal -> APERTURA_CHANNEL titulo LINK desc item CIERRE_CHANNEL','canal',6,'p_canal_basico','main.py',29),
  ('canal -> APERTURA_CHANNEL titulo desc LINK item CIERRE_CHANNEL','canal',6,'p_canal_basico2','main.py',33),
  ('canal -> APERTURA_CHANNEL titulo LINK desc opc item CIERRE_CHANNEL','canal',7,'p_canal_opcionales','main.py',37),
  ('canal -> APERTURA_CHANNEL titulo desc LINK opc item CIERRE_CHANNEL','canal',7,'p_canal_opcionales2','main.py',41),
  ('item -> APERTURA_ITEM titulo LINK desc CIERRE_ITEM','item',5,'p_item','main.py',45),
  ('item -> APERTURA_ITEM titulo desc LINK CIERRE_ITEM','item',5,'p_item2','main.py',49),
  ('item -> APERTURA_ITEM titulo LINK desc CIERRE_ITEM item','item',6,'p_item_recursivo','main.py',52),
  ('item -> APERTURA_ITEM titulo desc LINK CIERRE_ITEM item','item',6,'p_item_recursivo2','main.py',56),
  ('item -> APERTURA_ITEM titulo LINK desc opc CIERRE_ITEM','item',6,'p_item_opcionales','main.py',60),
  ('item -> APERTURA_ITEM titulo desc LINK opc CIERRE_ITEM','item',6,'p_item_opcionales2','main.py',64),
  ('item -> APERTURA_ITEM titulo LINK desc opc CIERRE_ITEM item','item',7,'p_item_opcionales_recursivo','main.py',68),
  ('item -> APERTURA_ITEM titulo desc LINK opc CIERRE_ITEM item','item',7,'p_item_opcionales_recursivo2','main.py',71),
  ('titulo -> APERTURA_TITLE TXT CIERRE_TITLE','titulo',3,'p_titulo','main.py',75),
  ('LINK -> APERTURA_LINK URL CIERRE_LINK','LINK',3,'p_LINK','main.py',79),
  ('desc -> APERTURA_DESC TXT CIERRE_DESC','desc',3,'p_desc','main.py',83),
  ('opc -> categoria','opc',1,'p_opc1','main.py',90),
  ('categoria -> APERTURA_CAT TXT CIERRE_CAT','categoria',3,'p_categoria','main.py',93),
  ('opc -> copyright','opc',1,'p_opc2','main.py',98),
  ('copyright -> APERTURA_COPY TXT CIERRE_COPY','copyright',3,'p_copyright','main.py',101),
  ('opc -> image','opc',1,'p_opc3','main.py',106),
  ('image -> APERTURA_IMAG URL titulo LINK CIERRE_IMAG','image',5,'p_image1','main.py',109),
  ('image -> APERTURA_IMAG URL titulo LINK opcimag CIERRE_IMAG','image',6,'p_image2','main.py',114),
  ('opcimag -> height width','opcimag',2,'p_opcimag1','main.py',119),
  ('opcimag -> height','opcimag',1,'p_opcimag2','main.py',122),
  ('opcimag -> width','opcimag',1,'p_opcimag3','main.py',125),
  ('height -> APERTURA_HEIGHT NUM CIERRE_HEIGHT','height',3,'p_height','main.py',128),
  ('width -> APERTURA_WIDTH NUM CIERRE_WIDTH','width',3,'p_width','main.py',131),
  ('opc -> lenguaje','opc',1,'p_opc4','main.py',134),
  ('lenguaje -> APERTURA_LANGUAGE TXT CIERRE_LANGUAGE','lenguaje',3,'p_lenguaje','main.py',137),
  ('opc -> webmaster','opc',1,'p_opc5','main.py',141),
  ('webmaster -> APERTURA_WEBMASTER TXT CIERRE_WEBMASTER','webmaster',3,'p_WEBMASTER','main.py',144),
  ('opc -> ultedit','opc',1,'p_opc6','main.py',148),
  ('ultedit -> APERTURA_ULTEDIT TXT CIERRE_ULTEDIT','ultedit',3,'p_pubdate','main.py',151),
  ('opc -> autor','opc',1,'p_opc7','main.py',155),
  ('autor -> APERTURA_AUTOR TXT CIERRE_AUTOR','autor',3,'p_autor','main.py',158),
  ('opc -> lastbuilddate','opc',1,'p_opc8','main.py',162),
  ('lastbuilddate -> APERTURA_BD TXT CIERRE_BD','lastbuilddate',3,'p_lastbuilddate','main.py',165),
  ('opc -> guid','opc',1,'p_opc9','main.py',169),
  ('guid -> APERTURA_GUID TXT CIERRE_GUID','guid',3,'p_guid','main.py',172),
  ('opc -> ttl','opc',1,'p_opc10','main.py',176),
  ('ttl -> APERTURA_TTL TXT CIERRE_TTL','ttl',3,'p_ttl','main.py',179),
]