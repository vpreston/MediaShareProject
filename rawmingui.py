"""
Victoria Preston
November 16, 2013
Minimum Deliverable mock up - an attempt at creating a URL sender
"""

from swampy.Gui import *
import urllib
from bs4 import *
import string

selector = []
display = []
count = 1
share_count = 1
shared_source = ['http://www.wunderground.com']
shared_viewer = []
g = Gui()

        
def update():
    global count
    for log in selector:
        if log not in display:
            display.append(log)
            mb.canvas.text([0,count], text = log)
            count -= 12
    get_new_shares()
            
def print_entry():
    text = en.get() 
    follower = ' was shared with a friend!'
    message = text + follower
    global selector
    if text not in selector:
        selector.append(text)
    try:
        label.config(text = message)
    except:
        pass
    pagehtml = url_display()

    
def url_display():
    count = 0
    url = en.get()
    site = urllib.urlopen(url)
    zsource = site.read()
    soup = BeautifulSoup(zsource)
    displayer = soup.get_text()
    canvas.canvas.delete(ALL)
    canvas.canvas.text([0,1],anchor = 'nw', justify = 'left', text = displayer)
    site.close()

def add_link(new_link):
    return shared_viewer.append(new_link)

def get_new_shares():
    global share_count
    for i in shared_source:
        if i not in shared_viewer:
            add_link(i)
            new_shared_list.canvas.text([0,share_count], text = i)
            share_count -= 12



#General set-up
g.title('Minumum Deliverable URLSender')

g.row()

g.col()
en = g.en(text = 'Insert URL here')
g.row([0,1], pady = 30)
g.endrow()
g.bu(text = 'Share', command = print_entry)

mb = g.sc(width = 500, height = 100)
mb.canvas.configure(confine = False, scrollregion = (0,0,1000,1000))

g.row([0,1], pady = 30)
g.endrow()    
g.bu(text = 'Update Data', command = update)   
g.row([0,1], pady = 30)
g.endrow()

canvas = g.sc(width = 500, height = 500)
canvas.canvas.configure(confine = False, scrollregion = (0,0,2000, 2000))


label = g.la()
g.endcol() 

g.col([2, 0], pady = 30)
g.endcol()

g.col()

new_shared_list = g.sc(width = 500, height = 500)
new_shared_list.canvas.configure(confine = False, scrollregion = (0,0,1000,1000))

g.row([0,1], pady = 30)
g.endrow()
show_button = g.bu(text = 'Show link')
g.row([0,1], pady = 30)
g.endrow()
g.ca(width = 500, height = 500)
g.endcol()

g.endrow()
    



#launch the gui
g.mainloop()



"""
selector = [0,1,2]
        mb = g.mb(text = selector[0])
        for select in selector:
            g.mi(mb, text = select, command=Callable(set_select, mb, select))

"""
