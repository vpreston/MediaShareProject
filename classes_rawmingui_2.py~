"""
Victoria Preston
November 16, 2013
Minimum Deliverable mock up - an attempt at creating a URL sender
"""

#series of imports
from swampy.Gui import *
import urllib
from bs4 import *
import string
import pymongo
import datetime

class Model(object):

    from pymongo import MongoClient
    
    def __init__(self, client=MongoClient(),count=1,share_count=1,g=Gui()):
        self.count=count
        self.share_count=share_count
        self.g=g
        self.client=client
        #initialize database
        self.db = self.client.test_database

        #names new databases within instance, TODO: Potentially add a logged history database for full history of link views
        self.share_hist = self.db.share_hist
        self.display = self.db.display
        self.point_total = self.db.point_total
        self.shared_source = self.db.shared_source
        self.shared_viewer = self.db.shared_viewer

        #clears the databases upon running script, remove these lines in hysteretic tests, TODO: create an initial initializer upon the first runtime to set default values like points, or default views
        self.share_hist.remove()
        self.display.remove()
        self.point_total.remove()
        self.shared_viewer.remove()
        self.shared_source.remove()
        self.point_total.insert({'points':10})
        self.shared_source.insert([{'friend': 'Alex', 'link': 'http://www.wunderground.com'},{'friend': 'Mark', 'link':'http://www.weather.com'}])

class Controller(object):

    def __init__(self, model):
        """
        upon running the script, gets data from the database and updates the gui displays
        """
        for thing in model.display.find():
            share_history.canvas.text([0,model.count], text = thing['friend'] + ' ' + thing['share'] + ' ' + str(thing['date']))
            model.count -= 12
        for thing in model.point_total.find():
            amount = thing['points']
        points.config(text = str(amount))
        for thing in model.shared_viewer.find():
            link = new_shared_list.canvas.text([0,model.share_count], text = str(thing['link']), activefill = 'blue')
            link.bind('<Double-1>', onObjectClick)
            model.share_count -= 12
    

    def update(self,model):
        #TODO: Make some of the updating automatic perhaps?  This could also be renamed the refresh button!
        """
        when the update button is pushed, this looks at the database, and will print things not already in the display, as well as log displayed data (meaning that if the gui closes before update is pressed, the data is still saved, and will be displayed the next time update will be pressed)
        """
        for log in model.share_hist.find():
            if log not in model.display.find():
                model.display.insert(log)
                self.share_history.canvas.text([0,count], text = log['friend'] + ' ' + log['share'] + ' ' + str(log['date']))
                model.count -= 12
                for thing in model.point_total.find():
                    existing = thing['points']
                    model.point_total.update({'points': existing}, {'$set': {'points':existing-1}})
                    points.config(text = str(existing-1))
        self.get_new_shares()    
   
    def print_entry(self,model):
        """
        Allows shares to be made, will check to make sure nothing is a repeat, will log the data.  Interactive with the user.
        """
        text = en.get()
        connection = friend.get() 
        follower = ' was shared with '
        message = text + follower + connection + '!'
        if  count == 1:
            model.share_hist.insert({'friend':connection,'share':text, 'date': datetime.datetime.utcnow()})
            label.config(text = message)
            model.count -= 12
        else:
            instance_count = 0
            for instance in model.share_hist.find():
                if text == instance['share'] and connection == instance['friend']:
                    label.config(text = 'That is a repeat!')
                    return
                instance_count += 1
            if instance_count == share_hist.count():
                model.share_hist.insert({'friend':connection,'share':text, 'date': datetime.datetime.utcnow()})
                label.config(text = message)

#possibly class View here?

    def url_display(self,url):
        """
        Shows a links html text
        """
        site = urllib.urlopen(url)
        zsource = site.read()
        soup = BeautifulSoup(zsource)
        displayer = soup.get_text()
        canvas.canvas.delete(ALL)
        canvas.canvas.text([0,1],anchor = 'nw', justify = 'left', text = displayer)
        site.close()

    def add_link(self,new_link,model):
        """
        adds a link to the shared_viewer display 
        """
        return model.shared_viewer.insert(new_link)

    def get_new_shares(self):
        """
        will update the recieved, or shared_viewer display
        """
        for i in model.shared_source.find():
            if i not in model.shared_viewer.find():
                add_link(i)
                link = new_shared_list.canvas.text([0,share_count], text = str(i['link']), activefill = 'blue')
                link.bind('<Double-1>', onObjectClick)
                model.share_count -= 12

    def onObjectClick(self,event):
        """
        allows us to double click on a link and show it, as well as remove it from the list of need to view links
        """
        for thing in model.point_total.find():
            existing = thing['points']
            model.point_total.update({'points': existing}, {'$set': {'points':existing+1}})
            points.config(text = str(existing + 1))
        index = event.widget.find_closest(event.x, event.y)
        i = model.shared_viewer.find()
        access = i[index[0] - 1]
        link = access['link']
        self.url_display(link)
        model.shared_viewer.remove(access)
        model.shared_source.remove(access)
    
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
    


initialize()
#launch the gui
g.mainloop()

