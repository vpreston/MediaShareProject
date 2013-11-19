
#!/bin/env python
# -*- coding: utf-8 -*-

import sys
from StringIO import StringIO
from PyQt4 import QtCore,QtGui,uic
from lxml import etree


import exchange
import exchange_ctls
import exchange_connections



def set_root_tag_class(qt_ele,html_root) :
  html_root.xpath('/html/head')[0].set('class',qt_ele.text)


def exchange_root(qt_ele,html_tag) :
  for item in qt_ele.xpath('*') :
    # 
    if item.tag == 'class' :
      set_root_tag_class(item,html_tag)
    # 
    elif item.tag == 'widget' :
      exchange.exchange_ele(item,html_tag.xpath('/html/body')[0])
    # 
    elif item.tag in ('resources','connections') :
      continue
    # 
    else :
      print 'exchange_root error : unknown tag : ' + item.tag
      continue
  #
  for qt_connect in qt_ele.xpath('connections') :
    exchange_connections.exchange_connection(qt_connect,html_tag)


if __name__ == '__main__':
  if len(sys.argv) != 3 :
    print 'usage : python xxx.ui xxx.html'
    sys.exit(0)
  qt_ele   = etree.parse(open(sys.argv[1]))
  html_tag = etree.parse(StringIO('<html><head><title>null</title></head><body></body></html>'))

  exchange_root(qt_ele.getroot(),html_tag)
  #javascript
  if exchange_ctls.has_menu_bar :
    html_tag.xpath('/html/head')[0].append(etree.parse(StringIO('<script src="menu.js" type="text/javascript"> </script>')).getroot())
  f = open(sys.argv[2],'w+')
  f.write(etree.tostring(html_tag , pretty_print=True))
  f.close()
