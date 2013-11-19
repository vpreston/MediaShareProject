#!/bin/env python
# -*- coding: utf-8 -*-

import sys
from StringIO import StringIO
from PyQt4 import QtCore,QtGui,uic
from lxml import etree


def exchange_connection(qt_ele,html_tag) :
  str_sender   = ''.join(qt_ele.xpath('sender/text()'))
  str_signal   = ''.join(qt_ele.xpath('signal/text()'))
  str_receiver = ''.join(qt_ele.xpath('receiver/text()'))
  str_slot     = ''.join(qt_ele.xpath('slot/text()'))
  html_sender  = html_tag.xpath('//*[id="%s"]' % str_sender)

