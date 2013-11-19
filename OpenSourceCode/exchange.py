#!/bin/env python
# -*- coding: utf-8 -*-

import sys
from StringIO import StringIO
from PyQt4 import QtCore,QtGui,uic
from lxml import etree

import exchange_ctls
import exchange_propertys


#转换qt-xml中元素为html标签
def exchange_ele(qt_ele,html_tag) :

  #如果该xml结点是 QWidget 容器,则
  if (qt_ele.tag == 'widget') and (qt_ele.get('class') == 'QWidget') :
    exchange_QWidget(qt_ele,html_tag)

  #如果是 QMainWindow 容器,则
  elif (qt_ele.tag == 'widget') and (qt_ele.get('class') == 'QMainWindow') :
    exchange_QMainWindow(qt_ele,html_tag)

  #如果该xml结点是layout容器,则
  elif qt_ele.tag == 'layout' :
    exchange_layout(qt_ele,html_tag)

  #如果是 layout/item
  elif qt_ele.tag == 'item' :
    exchange_ele(qt_ele[0],html_tag)

  #如果是控件
  elif qt_ele.tag == 'widget' :
    ele_weight = exchange_ctls.get_tag_widget(qt_ele)
    html_tag.append(ele_weight)

  #如果是填充体
  elif qt_ele.tag == 'spacer' :
    ele_weight = get_tag_spacer(qt_ele)
    html_tag.append(ele_weight)

  #其它
  else :
    print 'exchange_ele error : unknown tag : ' + qt_ele.tag




def get_tag_spacer(qt_ele) :
  html_tag = etree.Element('span')
  spacer_size = {'width':'0','height':'0'}
  #取方向
  orientation = ''.join(qt_ele.xpath('property[@name="orientation"]/enum/text()'))
  #取size_type
  size_type   = ''.join(qt_ele.xpath('property[@name="sizeType"]/enum/text()'))
  if 'Qt::Vertical' == orientation :
    spacer_size['width']  = ''.join(qt_ele.xpath('property[@name="sizeHint"]/size/width/text()'))
    spacer_size['height'] = ''.join(qt_ele.xpath('property[@name="sizeHint"]/size/height/text()'))
  elif 'Qt::Horizontal' == orientation :
    spacer_size['width']  = ''.join(qt_ele.xpath('property[@name="sizeHint"]/size/width/text()'))
    spacer_size['height'] = ''.join(qt_ele.xpath('property[@name="sizeHint"]/size/height/text()'))
  else : 
    print 'get_tag_spacer error : unknown orientation %s' % orientation
  html_tag.set('style','width:%spx;height:%spx'%(spacer_size['width'],spacer_size['height']))
  return html_tag

def exchange_QWidget(qt_ele,html_tag) :
  html_div_tag= etree.Element('div')
  # 取属性
  str_style = exchange_propertys.styles_to_str(exchange_propertys.get_ele_styles(qt_ele,True,'100%','100%'))
  if str_style != '' : html_div_tag.set('style',str_style )
  html_tag.append(html_div_tag)
  # 设置标题
  html_tag.xpath('/html/head/title')[0].text = ''.join(qt_ele.xpath('property[@name="windowTitle"]/string/text()'))
  #将其中所有 layout 放入 div
  for tag_tmp in qt_ele.xpath('*'):
    if tag_tmp.tag == 'layout' :
      exchange_ele(tag_tmp,html_div_tag)
    elif tag_tmp.tag == 'widget' :
      exchange_ele(tag_tmp,html_div_tag)
    # 下列元素不处理
    elif tag_tmp.tag in ('property','action') :
      pass
    else :
      print 'exchange_ele error : get unknown tag : %s' % tag_tmp.tag

def exchange_QMainWindow(qt_ele,html_tag) :
  html_div_tag= etree.Element('div')
  # 取属性
  str_style   = exchange_propertys.styles_to_str(exchange_propertys.get_ele_styles(qt_ele,True,'100%','100%'))
  if str_style != '' : html_div_tag.set('style',str_style )
  html_tag.append(html_div_tag)
  # 设置标题
  html_tag.xpath('/html/head/title')[0].text = ''.join(qt_ele.xpath('property[@name="windowTitle"]/string/text()'))
  #将其中所有 layout 放入 div
  for tag_tmp in qt_ele.xpath('*'):
    if tag_tmp.tag == 'layout' :
      exchange_ele(tag_tmp,html_div_tag)
    elif tag_tmp.tag == 'widget' :
      exchange_ele(tag_tmp,html_div_tag)
    elif tag_tmp.tag == 'property' :
      pass
    # 下列元素不处理
    elif tag_tmp.tag in ('property','action') :
      pass
    else :
      print 'exchange_ele error : get unknown tag : %s' % tag_tmp.tag


def exchange_layout(qt_ele,html_tag) :
  html_table = exchange_ctls.get_tag_layout(qt_ele)
  str_class = ''.join(qt_ele.xpath('@class'))
  #水平布局
  if str_class == 'QVBoxLayout' :
    for item in qt_ele.xpath('item') :
      html_tr = etree.Element('tr')
      html_td = etree.Element('td')
      html_tr.append(html_td)
      html_table.append(html_tr)
      exchange_ele(item,html_td)
  #垂直布局
  elif str_class == 'QHBoxLayout' :
    html_tr = etree.Element('tr')
    html_table.append(html_tr)
    for item in qt_ele.xpath('item') :
      html_td = etree.Element('td')
      html_tr.append(html_td)
      exchange_ele(item,html_td)
      #把宽度属性从子结点中取出放入td（解决table单元格中内容不能充满单元格的问题）
      if len(html_td) == 1 :
        str_styles = html_td[0].get('style')
        if str_styles is not None :
          styles = exchange_propertys.str_to_styles(str_styles)
          if styles.has_key('width') :
            html_td.set('style','width:%s;'%styles['width'])
  #网格布局 或 Form布局
  elif str_class == 'QGridLayout' or str_class == 'QFormLayout' :
    for item in qt_ele.xpath('item') :
      #取行列数，如果table中已经有该行列，则直接添加控件，没有则先分配
      row = int(item.get('row'))
      col = int(item.get('column'))
      while len(html_table) < row+1:
        html_table.append(etree.Element('tr'))
      for html_tr in html_table :
        while len(html_tr) < col+1:
          html_tr.append(etree.Element('td'))
      #向行列添加控件
      exchange_ele(item,html_table[row][col])
      #把宽度属性从子结点中取出放入td（解决table单元格中内容不能充满单元格的问题）
      if len(html_table[row][col]) == 1 :
        str_styles = html_table[row][col][0].get('style')
        if str_styles is not None :
          styles = exchange_propertys.str_to_styles(str_styles)
          if styles.has_key('width') :
            html_table[row][col].set('style','width:%s;'%styles['width'])
  #其它布局
  else :
    print 'exchange_ele error : no this layout %s' % str_class

  #如果table不为空，则添加入div
  if len(html_table) > 0 :
    html_tag.append(html_table)
  #否则随便加一个元素进去，否则定位有问题
  else :
    html_tag.append(etree.Element('p'))
