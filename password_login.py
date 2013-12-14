from swampy.Gui import *
from getpass import *

d={}

def newuser():
    if newusername.get() in d:
        label.config(text="That username is already in use.")
    elif newpassword.get()==repeatnewpassword.get():
        d[newusername.get()]=newpassword.get()
        label.config(text="Thank you for signing up!")
    else:
        label.config(text="Your passwords don't match! Please try again")

def login():
    username=raw_input("MusicSwAPPer Username:  ")
    password=getpass("MusicSwAPPer Password:  ")
    if password==d[username]:
        return "You are now logged in!"
    else:
        return "We do not recognize your username or password, please try again."

signupgui=Gui()
signupgui.title('MusicSwAPPer Sign Up')
usernamelabel=signupgui.la(text='Username:')
newusername=signupgui.en()
newpasswordlabel=signupgui.la(text='Password:')
newpassword=signupgui.en(show='*')
repeatpasswordlabel=signupgui.la(text='Re-enter Password')
repeatnewpassword=signupgui.en(show='*')
button=signupgui.bu(text='Sign Up!',command=newuser)
label=signupgui.la()

signupgui.mainloop()

print login()