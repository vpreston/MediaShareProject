"""
Victoria Preston, Alex Crease, Mark-Robin Giolando
Beginning:November 16, 2013
Final:December 17, 2013
Development File
"""

#series of imports
from swampy.Gui import *
import string
import pymongo
import datetime
import os
import gobject
import gst
from getpass import *
from pymongo import MongoClient

#establish database access, will not allow no-users access, hosted off the MongoHQ server systems, Sandbox prototype model
client = MongoClient('mongodb://sofdes:sofdes@dharma.mongohq.com:10075/mediashareproject')
db = client.mediashareproject

#global variables, these things don't log data, but just help us display it
count = 1
share_count = 1
username = ''

#establishing the database collections, the elements which will store the data with the database
users = db.users

#login system
def main():
    """
    Launches login system everytime the script is run, users have the option of signing in, or signing up if they have not already established an account and accout information. Upon login/signup, the main application is launched
    """
    
    def newusergui():
        """
        for anyone who needs to register, this adds them to the database system
        """
        def newuser():
            global username
            for user in users.find():
                for info in user:
                    if user[info]==newusername.get():
                        label.config(text="That username is already in use.")
                        return
            if newpassword.get()==repeatnewpassword.get():
                users.insert({'user':newusername.get(), 'password': newpassword.get()})
                db.add_user(newusername.get(), newpassword.get())
                label.config(text="Thank you for signing up!")
                username = newusername.get()
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
    #names new databases that we will use now that the application is launched
    share_hist = db.share_hist
    display = db.display
    point_total = db.point_total
    shared_source = db.shared_source
    shared_viewer = db.shared_viewer

    #clears the databases upon running script
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
            for thing in point_total.distinct(username):
                amount = thing
            points.config(text = str(amount))
        except:
            point_total.insert({username:10})
            for thing in point_total.distinct(username):
                amount = thing
            points.config(text = str(amount))
        for thing in display.distinct(username):
            share_history.canvas.text([0,count], text = thing['friend'] + ' ' + thing['share'] + ' ' + str(thing['date']))
            count -= 12
        for thing in shared_viewer.find():
            link = new_shared_list.canvas.text([0,share_count], text = str(thing[username]['link']), activefill = 'blue')
            link.bind('<Double-1>', onObjectClick)
            share_count -= 12
            

    def update():
        """
        when the update button is pushed, this looks at the database, and will print things not already in the display, as well as log displayed data (meaning that if the gui closes before update is pressed, the data is still saved, and will be displayed the next time update will be pressed)
        """
        global count
        global username
        for log in share_hist.find():
            if log not in display.find():
                display.insert(log)
                share_history.canvas.text([0,count], text = log[username]['friend'] + ' ' + log[username]['share'] + ' ' + str(log[username]['date']))
                count -= 12
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
        for thing in point_total.distinct(username):
            existing = thing
            point_total.update({username: existing}, {'$inc': {username:(-1)}})
            points.config(text = str(existing-1))
        if  count == 1:
            t = datetime.datetime.now()
            if t.minute < 10:
                minute = '0'+str(t.minute)
            else:
                minute = str(t.minute)
            timestamp = str(t.month) + '/' + str(t.day) +'/' + str(t.year) + ',' +str(t.hour) + ':' + minute
            share_hist.insert({username:{'friend':connection,'share':text, 'date': timestamp}})
            shared_source.insert({connection:{'link': text, 'friend':username}})
            label.config(text = message)
            count -= 12
        else:
            instance_count = 0
            for instance in share_hist.distinct(username):
                if text == instance['share'] and connection == instance['friend']:
                    label.config(text = 'That is a repeat!')
                    return
                instance_count += 1
            if instance_count == len(share_hist.distinct(username)):
                t = datetime.datetime.now()
                if t.minute < 10:
                    minute = '0'+str(t.minute)
                else:
                    minute = str(t.minute)
                timestamp = str(t.month) + '/' + str(t.day) +'/' + str(t.year) + ',' +str(t.hour) + ':' + minute
                share_hist.insert({username:{'friend':connection,'share':text, 'date': timestamp}})
                shared_source.insert({connection:{'link': text, 'friend':username}})
                label.config(text = message)


    def url_display(url):
        """
        downloads a youtube video into a file, then plays that file within the gui space
        url - raw string url from gui input
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
        for i in shared_source.distinct(username):
            if i['link'] not in shared_viewer.distinct('link'):
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
            print thing
            existing = thing[username]
            point_total.update({username: existing}, {'$inc': {username:1}})
            points.config(text = str(existing + 1))
        index = event.widget.find_closest(event.x, event.y)
        i = shared_viewer.find()
        access = i[index[0] - 1]
        link = access['link']
        url_display(link)
        shared_source.remove({username: {'link':access['link'], 'friend':access['friend']}})


    #General set-up
    pretty = 'light cyan'

    gui = Gui()
    gui.title('MusicswAPPer')


    gui.row()
    gui.la(text = 'Welcome to the swAPP', bg = 'black', fg='cyan', justify = 'left', font = ('Times', 20, 'bold italic'), height = 2, relief = 'groove')
    gui.endrow()
    gui.row(bg=pretty)
    gui.col(bg=pretty)
    gui.bu(text = 'Refresh', fg = 'forest green', font = ('Times', 15, 'bold'), bg=pretty, activeforeground='forest green', activebackground='powder blue', command = update) 
    gui.row([0,1], pady = 10, bg=pretty)
    gui.endrow()
    gui.la(text = 'Share a link', bg = pretty, font = ('Times', 13, 'italic'), anchor = 'left', justify='left')
    friend = gui.en(text = 'Who do you want to share with?', disabledforeground = 'light gray', fg = 'black', font = ('Times', 12))
    en = gui.en(text = 'Insert URL here', font = ('Times', 12))
    gui.bu(text = 'Share', font = ('Times', 15, 'bold'), bg = pretty, fg = 'forest green', activebackground = 'powder blue', activeforeground = 'forest green', command = print_entry)
    label = gui.la(bg=pretty, font=('Times', 11))

    gui.row([0,1], pady = 10, bg=pretty)
    gui.endrow()

    gui.la(text = 'Share history', bg=pretty, font=('Times',13, 'italic'))
    share_history = gui.sc(width = 500, height = 300)
    share_history.canvas.configure(confine = False, scrollregion = (0,0,1000,1000)) 
     
    gui.endcol() 

    gui.col(bg=pretty)
    gui.ca(height = 100, width = 5, bg=pretty, bd=0)
    gui.endcol()
    gui.col(bg=pretty)
    gui.ca(height = 10, width = 5, bg=pretty, bd=0)
    gui.ca(height = 10, width = 5, bg='black',bd=0)
    gui.ca(height = 10, width = 5, bg=pretty,bd=0)
    gui.ca(height = 10, width = 5, bg='black',bd=0)
    gui.ca(height = 10, width = 5, bg=pretty,bd=0)
    gui.ca(height = 10, width = 5, bg='black',bd=0)
    gui.ca(height = 10, width = 5, bg=pretty,bd=0)
    gui.ca(height = 10, width = 5, bg='black',bd=0)
    gui.ca(height = 10, width = 5, bg=pretty,bd=0)
    gui.endcol()
    gui.col(bg=pretty)
    gui.ca(height = 100, width = 5, bg=pretty)
    gui.endcol()

    gui.col(bg=pretty)

    gui.la(text = 'New Shares from Friends', bg = pretty, font=('Times', 13, 'italic'))
    new_shared_list = gui.sc(width = 500, height = 100)
    new_shared_list.canvas.configure(confine = False, scrollregion = (0,0,1000,1000))

    gui.row([0,1], pady = 30, bg=pretty)
    gui.endrow()

    gui.la(text = 'Viewer', bg=pretty, font = ('Times', 13, 'italic'))
    canvas = gui.ca(width = 500, height = 300, bg='black')
    canvas.configure(confine = False, scrollregion = (0,0,2000, 2000))

    points = gui.la(bg=pretty)


    gui.endcol()

    gui.col(bg=pretty)
    gui.ca(height = 100, width = 5, bg=pretty)
    gui.endcol()

    gui.endrow()
    initialize()
    gui.mainloop()
    

if __name__ == '__main__':
    main()
