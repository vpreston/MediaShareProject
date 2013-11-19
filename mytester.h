<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>960</width>
    <height>777</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>370</y>
      <width>211</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string>Share</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>371</width>
      <height>20</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>welcome back to musicswAPPer</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>150</y>
      <width>51</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Link:</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="textEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>140</y>
      <width>361</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>200</y>
      <width>51</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Title:</string>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="plainTextEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>200</y>
      <width>361</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>270</y>
      <width>111</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Description:</string>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="plainTextEdit_2">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>290</y>
      <width>421</width>
      <height>75</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>470</y>
      <width>131</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Share History:</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>90</y>
      <width>81</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Friend:</string>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="plainTextEdit_3">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>80</y>
      <width>361</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
   <widget class="QScrollArea" name="scrollArea">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>500</y>
      <width>421</width>
      <height>171</height>
     </rect>
    </property>
    <property name="widgetResizable">
     <bool>true</bool>
    </property>
    <widget class="QWidget" name="scrollAreaWidgetContents_2">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>417</width>
       <height>167</height>
      </rect>
     </property>
     <widget class="QScrollBar" name="verticalScrollBar">
      <property name="geometry">
       <rect>
        <x>400</x>
        <y>0</y>
        <width>20</width>
        <height>171</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="QTableView" name="tableView">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>401</width>
        <height>192</height>
       </rect>
      </property>
     </widget>
    </widget>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>80</y>
      <width>151</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Shared with you:</string>
    </property>
   </widget>
   <widget class="QScrollArea" name="scrollArea_2">
    <property name="geometry">
     <rect>
      <x>510</x>
      <y>110</y>
      <width>421</width>
      <height>171</height>
     </rect>
    </property>
    <property name="widgetResizable">
     <bool>true</bool>
    </property>
    <widget class="QWidget" name="scrollAreaWidgetContents_4">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>417</width>
       <height>167</height>
      </rect>
     </property>
     <widget class="QScrollBar" name="verticalScrollBar_3">
      <property name="geometry">
       <rect>
        <x>400</x>
        <y>0</y>
        <width>20</width>
        <height>171</height>
       </rect>
      </property>
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
     </widget>
     <widget class="QTableView" name="tableView_3">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>0</y>
        <width>401</width>
        <height>192</height>
       </rect>
      </property>
     </widget>
    </widget>
   </widget>
   <widget class="QWebView" name="webView">
    <property name="geometry">
     <rect>
      <x>510</x>
      <y>380</y>
      <width>421</width>
      <height>201</height>
     </rect>
    </property>
    <property name="url">
     <url>
      <string>about:blank</string>
     </url>
    </property>
   </widget>
   <widget class="QLabel" name="label_8">
    <property name="geometry">
     <rect>
      <x>510</x>
      <y>350</y>
      <width>151</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Link Look:</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>818</x>
      <y>290</y>
      <width>111</width>
      <height>31</height>
     </rect>
    </property>
    <property name="text">
     <string>Old History</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>600</y>
      <width>111</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Points Left:</string>
    </property>
   </widget>
   <widget class="QLCDNumber" name="lcdNumber">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>630</y>
      <width>101</width>
      <height>71</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>670</x>
      <y>600</y>
      <width>111</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Media Share:</string>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="plainTextEdit_4">
    <property name="geometry">
     <rect>
      <x>670</x>
      <y>630</y>
      <width>261</width>
      <height>75</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>960</width>
     <height>28</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <customwidgets>
  <customwidget>
   <class>QWebView</class>
   <extends>QWidget</extends>
   <header>QtWebKit/QWebView</header>
  </customwidget>
 </customwidgets>
 <resources/>
 <connections/>
</ui>
