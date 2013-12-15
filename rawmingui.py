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
from getpass import *
from pymongo import MongoClient

#establish verification database
client = MongoClient('mongodb://sofdes:sofdes@dharma.mongohq.com:10075/mediashareproject')
db = client.mediashareproject

#global variables, these things don't log data, but just help us display it
count = 1
share_count = 1
username = ''


users = db.users
users.remove()
users.insert({'user':'hey', 'password':'there'})



#login credentials
def main():
    """
    Launches login system everytime the script is run
    """
    global username

    def newusergui():
        """
        for anyone who needs to register, this adds them to the database system
        """
        def close():
            g.quit()
            
        def newuser():
            global username
            for user in users.find():
                for info in user:
                    print info
                    print user[info]
                    if user[info]==newusername.get():
                        label.config(text="That username is already in use.")
                        return
            if newpassword.get()==repeatnewpassword.get():
                users.insert({'user':newusername.get(), 'password': newpassword.get()})
                db.add_user(newusername.get(), newpassword.get())
                label.config(text="Thank you for signing up!")
                username = newusername.get()
                close()
                launch()
            else:
                label.config(text="Your passwords don't match! Please try again")
            
        usernamelabel=g.la(text='Username:')
        newusername=g.en()
        newpasswordlabel=g.la(text='Password:')
        newpassword=g.en(show='*')
        repeatpasswordlabel=g.la(text='Re-enter Password')
        repeatnewpassword=g.en(show='*')
        button=g.bu(text="Let's get started!",command=newuser)
        label=g.la()
        

    def logingui():
        """
        this launches the general sign-in gui for those who have registered
        """
        
        def close():
            global username
            for user in users.find():
                    if password.get()==user['password'] and usernameentry.get() == user['user']:
                        label.config(text= "You are now logged in!")
                        username = usernameentry.get()
                        g.quit()
                        launch()
                        return True 
                    else:
                        label.config(text= "We do not recognize your username or password, please try again.")
                    
        usernamelabel=g.la(text = "MusicSwAPPer Username:  ")
        usernameentry = g.en() 
        passwordlabel=g.la("MusicSwAPPer Password:  ")
        password = g.en(show = '*')
        button=g.bu(text="Let's get started!",command=close)
        label=g.la()

            
    g=Gui()
    g.title('Launch MusicSwAPPer')
    signuporlogin = g.la(text = 'Please Sign-In or Sign-Up!')
    g.row()
    login = g.bu(text = 'Sign in', command=logingui)
    sign = g.bu(text = 'Sign up', command=newusergui)
    g.endrow()

    g.mainloop()


def launch():
    """
    launches the 'real' gui system, the one we interact with
    """
    #names new databases within instance, TODO: Potentially add a logged history database for full history of link views
    share_hist = db.share_hist
    display = db.display
    point_total = db.point_total
    shared_source = db.shared_source
    shared_viewer = db.shared_viewer
    point_total = db.point_total
    
    point_total.remove()
   

    #clears the databases upon running script, remove these lines in hysteretic tests
    #IMPORTANT: leave the shared_viewer.remove()

    shared_viewer.remove()
   
    def initialize():
        """
        upon running the script, gets data from the database and updates the gui displays
        """

        global count
        global share_count
        global username
        try:
            for thing in point_total.find():
                print 'try'
                amount = thing['points']
            points.config(text = str(amount))
        except:
            point_total.insert({'points':10})
            for thing in point_total.find():
                print 'except'
                print thing
                amount = thing['points']
            points.config(text = str(amount))
        for thing in display.find():
            print 'in display'
            print thing
            share_history.canvas.text([0,count], text = thing['friend'] + ' ' + thing['share'] + ' ' + str(thing['date']))
            count -= 12
        for thing in shared_viewer.find():
            link = new_shared_list.canvas.text([0,share_count], text = str(thing[username]['link']), activefill = 'blue')
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
                print 'this is added to display', log
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
        global username
        res = []
        text = en.get()
        connection = friend.get()
        for user in users.find():
            res.append(user['user'])
        if connection not in res:
            label.config(text = 'Sorry, user not in our records')
            return 
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
                    shared_source.insert({connection:{'link': text, 'friend':username}})
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
        x=os.path.dirname(os.path.realpath(__file__))
        player.set_property('uri', 'file://%s/playingvid.mp4'%(x))
        player.set_state(gst.STATE_PLAYING)

        bus = player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect('sync-message::element', on_sync_message, window_id)

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
        global username
        for i in shared_viewer.find():
                    print i
        for i in shared_source.distinct(username):
            if i['friend'] not in shared_viewer.distinct('friend') and i['link'] not in shared_viewer.distinct('link'):
                add_link(i)
                link = new_shared_list.canvas.text([0,share_count], text = str(i['link']), activefill = 'blue')
                link.bind('<Double-1>', onObjectClick)
                share_count -= 12

    def onObjectClick(event):
        """
        allows us to double click on a link and show it, as well as remove it from the list of need to view links
        """
        global username
        for thing in point_total.find():
            existing = thing['points']
            point_total.update({'points': existing}, {'$set': {'points':existing+1}})
            points.config(text = str(existing + 1))
        index = event.widget.find_closest(event.x, event.y)
        i = shared_viewer.find()
        access = i[index[0] - 1]
        link = access['link']
        url_display(link)
        shared_source.remove({username: {'link':access['link'], 'friend':access['friend']}})


    #General set-up
    gui = Gui()
    gui.title('Minumum Deliverable URLSender')

    gui.row()

    gui.col()

    gui.la(text = 'Welcome to musicswAPPer')
    gui.bu(text = 'Refresh', command = update)  
    gui.row([0,1], pady = 10)
    gui.endrow()
    gui.la(text = 'Share a link!')
    friend = gui.en(text = 'Who do you want to share with?')
    en = gui.en(text = 'Insert URL here')
    gui.bu(text = 'Share', command = print_entry)
    label = gui.la()

    gui.row([0,1], pady = 10)
    gui.endrow()

    gui.la(text = 'Share History')
    share_history = gui.sc(width = 500, height = 300)
    share_history.canvas.configure(confine = False, scrollregion = (0,0,1000,1000)) 
     
    gui.endcol() 

    gui.col()
    gui.ca(height = 100, width = 50)
    gui.endcol()

    gui.col()

    gui.la(text = 'New Shares from Friends')
    new_shared_list = gui.sc(width = 500, height = 100)
    new_shared_list.canvas.configure(confine = False, scrollregion = (0,0,1000,1000))

    gui.row([0,1], pady = 30)
    gui.endrow()

    gui.la(text = 'Link Preview')
    canvas = gui.ca(width = 500, height = 300, bg='black')
    canvas.configure(confine = False, scrollregion = (0,0,2000, 2000))

    points = gui.la()


    gui.endcol()

    gui.endrow()
    initialize()
    gui.mainloop()
    

if __name__ == '__main__':
    main()
