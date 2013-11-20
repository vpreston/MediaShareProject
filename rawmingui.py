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
shared_source = ['http://www.wunderground.com', 'http://www.weather.com']
shared_viewer = []
point_total = 10
g = Gui()

        
def update():
    global count
    global point_total
    for log in selector:
        if log not in display:
            display.append(log)
            share_history.canvas.text([0,count], text = log)
            count -= 12
            point_total -= 1
    get_new_shares()
    points.config(text = point_total)
            
def print_entry():
    text = en.get()
    connection = friend.get() 
    follower = ' was shared with '
    message = text + follower + connection + '!'
    global selector
    if text not in selector:
        selector.append(text)
    try:
        label.config(text = message)
    except:
        pass

    
def url_display(url):
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
            link = new_shared_list.canvas.text([0,share_count], text = i, activefill = 'blue')
            link.bind('<Double-1>', onObjectClick)
            share_count -= 12

def onObjectClick(event):
    global point_total
    point_total += 1
    index = event.widget.find_closest(event.x, event.y)
    access = shared_viewer[index[0] - 1]
    url_display(access)
    
    


#General set-up
g.title('Minumum Deliverable URLSender')

g.row()

g.col()

g.la(text = 'Welcome to musicswAPPer')
g.bu(text = 'Update Data', command = update)  
g.row([0,1], pady = 10)
g.endrow()
g.la(text = 'Share a link!')
friend = g.en(text = 'Who do you want to share with?')
en = g.en(text = 'Insert URL here')
g.bu(text = 'Share', command = print_entry)
label = g.la()

g.row([0,1], pady = 10)
g.endrow()

g.la(text = 'Share History')
share_history = g.sc(width = 500, height = 300)
share_history.canvas.configure(confine = False, scrollregion = (0,0,1000,1000)) 
 
g.endcol() 

g.col()
g.ca(height = 100, width = 50)
g.endcol()

g.col()

g.la(text = 'New Shares from Friends')
new_shared_list = g.sc(width = 500, height = 100)
new_shared_list.canvas.configure(confine = False, scrollregion = (0,0,1000,1000))

g.row([0,1], pady = 30)
g.endrow()

g.la(text = 'Link Preview')
canvas = g.sc(width = 500, height = 300)
canvas.canvas.configure(confine = False, scrollregion = (0,0,2000, 2000))

points = g.la()

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
