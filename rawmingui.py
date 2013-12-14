"""
Victoria Preston
November 16, 2013
Minimum Deliverable mock up - an attempt at creating a URL sender

TODO:
- passwords/logins/setvariables for the module
- networking
- classing
- link display
- clean it up
"""

#series of imports
from swampy.Gui import *
import urllib
from bs4 import *
import string
import pymongo
import datetime
import os
import gobject
import gst

from pymongo import MongoClient
client = MongoClient()
print client

#initialize database
db = client.test_database

#names new databases within instance, TODO: Potentially add a logged history database for full history of link views
share_hist = db.share_hist
display = db.display
point_total = db.point_total
shared_source = db.shared_source
shared_viewer = db.shared_viewer

#clears the databases upon running script, remove these lines in hysteretic tests, TODO: create an initial initializer upon the first runtime to set default values like points, or default views
#IMPORTANT: leave the shared_viewer.remove()
share_hist.remove()
display.remove()
point_total.remove()
shared_viewer.remove()
shared_source.remove()
shared_source.insert([{'Victoria':{'friend': 'Alex', 'link': 'http://www.wunderground.com'}},{'Victoria':{'friend': 'Mark', 'link':'http://www.youtube.com/watch?v=kZUPCB9533Y'}}])

#login credentials, TODO: First time launch sets these
user = 'vlpreston19'
passw = 'testing'


#global variables, these things don't log data, but just help us display it
count = 1
share_count = 1
g = Gui()

def initialize():
    """
    upon running the script, gets data from the database and updates the gui displays
    """

    global count
    global share_count
    for thing in display.find():
        share_history.canvas.text([0,count], text = thing['friend'] + ' ' + thing['share'] + ' ' + str(thing['date']))
        count -= 12
    try:
        for thing in point_total.find():
            amount = thing['points']
        points.config(text = str(amount))
    except:
        point_total.insert({'points':10})
        for thing in point_total.find():
            amount = thing['points']
        points.config(text = str(amount))
    for thing in shared_viewer.find():
        link = new_shared_list.canvas.text([0,share_count], text = str(thing['Victoria']['link']), activefill = 'blue')
        link.bind('<Double-1>', onObjectClick)
        share_count -= 12
        

def update():
    #TODO: Make some of the updating automatic perhaps?  This could also be renamed the refresh button!
    """
    when the update button is pushed, this looks at the database, and will print things not already in the display, as well as log displayed data (meaning that if the gui closes before update is pressed, the data is still saved, and will be displayed the next time update will be pressed)
    """
    global count
    for log in share_hist.find():
        if log not in display.find():
            display.insert(log)
            share_history.canvas.text([0,count], text = log['friend'] + ' ' + log['share'] + ' ' + str(log['date']))
            count -= 12
            for thing in point_total.find():
                existing = thing['points']
                point_total.update({'points': existing}, {'$set': {'points':existing-1}})
                points.config(text = str(existing-1))
    get_new_shares()
    
   
def print_entry():
    """
    Allows shares to be made, will check to make sure nothing is a repeat, will log the data.  Interactive with the user.
    """
    global count
    text = en.get()
    connection = friend.get() 
    follower = ' was shared with '
    message = text + follower + connection + '!'
    if  count == 1:
        share_hist.insert({'friend':connection,'share':text, 'date': datetime.datetime.utcnow()})
        label.config(text = message)
        count -= 12
    else:
        instance_count = 0
        for instance in share_hist.find():
            if text == instance['share'] and connection == instance['friend']:
                label.config(text = 'That is a repeat!')
                return
            instance_count += 1
        if instance_count == share_hist.count():
                share_hist.insert({'friend':connection,'share':text, 'date': datetime.datetime.utcnow()})
                shared_source.insert({connection:{'link': text, 'friend':'Victoria'}})
                label.config(text = message)


def url_display(url):
    """
    Shows a links html text
    """
    myfile="playingvid.mp4"
    try:
	    os.remove(myfile)
    except OSError:
	    k=2

    os.system('youtube-dl -o playingvid.mp4 %s'%url)
    
    gobject.threads_init()
    window_id = canvas.winfo_id()

    player = gst.element_factory_make('playbin2', 'player')
    player.set_property('video-sink', None)
    player.set_property('uri', 'file:///home/victoria/playingvid.mp4')
    player.set_state(gst.STATE_PLAYING)

    bus = player.get_bus()
    bus.add_signal_watch()
    bus.enable_sync_message_emission()
    bus.connect('sync-message::element', on_sync_message, window_id)


"""	
if __name__ == '__main__':
		run_things('http://www.youtube.com/watch?v=kZUPCB9533Y')
    
    site = urllib.urlopen(url)
    zsource = site.read()
    soup = BeautifulSoup(zsource)
    displayer = soup.get_text()
    canvas.canvas.delete(ALL)
    canvas.canvas.text([0,1],anchor = 'nw', justify = 'left', text = displayer)
    site.close()
"""

def on_sync_message(bus, message, window_id):
        if not message.structure is None:
            if message.structure.get_name() == 'prepare-xwindow-id':
                image_sink = message.src
                image_sink.set_property('force-aspect-ratio', True)
                image_sink.set_xwindow_id(window_id)


def add_link(new_link):
    """
    adds a link to the shared_viewer display 
    """
    return shared_viewer.insert(new_link)

def get_new_shares():
    """
    will update the recieved, or shared_viewer display
    """
    global share_count
    for i in shared_viewer.find():
                print i
    for i in shared_source.distinct('Victoria'):
        if i['friend'] not in shared_viewer.distinct('friend') and i['link'] not in shared_viewer.distinct('link'):
            add_link(i)
            link = new_shared_list.canvas.text([0,share_count], text = str(i['link']), activefill = 'blue')
            link.bind('<Double-1>', onObjectClick)
            share_count -= 12

def onObjectClick(event):
    """
    allows us to double click on a link and show it, as well as remove it from the list of need to view links
    """
    for thing in point_total.find():
        existing = thing['points']
        point_total.update({'points': existing}, {'$set': {'points':existing+1}})
        points.config(text = str(existing + 1))
    index = event.widget.find_closest(event.x, event.y)
    i = shared_viewer.find()
    access = i[index[0] - 1]
    link = access['link']
    url_display(link)
    shared_source.remove({'Victoria': {'link':access['link'], 'friend':access['friend']}})


#General set-up
g.title('Minumum Deliverable URLSender')

g.row()

g.col()

g.la(text = 'Welcome to musicswAPPer')
g.bu(text = 'Refresh', command = update)  
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
canvas = g.ca(width = 500, height = 300, bg='black')
canvas.configure(confine = False, scrollregion = (0,0,2000, 2000))

points = g.la()

g.endcol()

g.endrow()
    


initialize()
#launch the gui
g.mainloop()

