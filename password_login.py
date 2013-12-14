from swampy.Gui import *
from getpass import *
import pymongo
from pymongo import MongoClient




def main():
    client = MongoClient()
    db = client.test_database

    users = db.users
    users.remove()
    print users
    users.insert({'user':'hey', 'password':'there'})
    for thing in users.find():
        print thing

    def newusergui():
        def close():
            signupgui.quit()
            
        def newuser():
            for user in users.find():
                for info in user:
                    print info
                    print user[info]
                    if user[info]==newusername.get():
                        print 'already in use'
                        label.config(text="That username is already in use.")
                        return
            if newpassword.get()==repeatnewpassword.get():
                print 'running this loop'
                users.insert({'user':newusername.get(), 'password': newpassword.get()})
                print users
                label.config(text="Thank you for signing up!")
                close()
                launch()
                return True
            else:
                label.config(text="Your passwords don't match! Please try again")
            
        usernamelabel=signupgui.la(text='Username:')
        newusername=signupgui.en()
        newpasswordlabel=signupgui.la(text='Password:')
        newpassword=signupgui.en(show='*')
        repeatpasswordlabel=signupgui.la(text='Re-enter Password')
        repeatnewpassword=signupgui.en(show='*')
        button=signupgui.bu(text="Let's get started!",command=newuser)
        label=signupgui.la()
        

    def logingui():
    
        def close():
            for user in users.find():
                for info in user:
                    if password.get()==user[info]:
                        label.config(text= "You are now logged in!")
                        signupgui.quit()
                        launch()
                        return True 
                    else:
                        label.config(text= "We do not recognize your username or password, please try again.")
                    
        usernamelabel=signupgui.la(text = "MusicSwAPPer Username:  ")
        username = signupgui.en() 
        passwordlabel=signupgui.la("MusicSwAPPer Password:  ")
        password = signupgui.en(show = '*')
        button=signupgui.bu(text="Let's get started!",command=close)
        label=signupgui.la()

            
    signupgui=Gui()
    signupgui.title('MusicSwAPPer Sign Up')
    signuporlogin = signupgui.la(text = 'Please Sign-In or Sign-Up!')
    signupgui.row()
    login = signupgui.bu(text = 'Sign in', command=logingui)
    sign = signupgui.bu(text = 'Sign up', command=newusergui)
    signupgui.endrow()

    signupgui.mainloop()

def launch():
    g = Gui()
    g.mainloop()

if __name__ == '__main__' :    
    main()
