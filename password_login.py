from swampy.Gui import *

d={}

def newuser(username,password1,password2):
    signupgui=Gui()
    signupgui.title('Sign Up')
    signupgui.mainloop()
    if username in d:
        return "This username is already in use! Please enter a different one"
    elif password1==password2:
        d[username]=password1
        return "Thank you for creating an account!"
    else:
        return "Your passwords don't match! Please try again"

def login(user,password):
    if password==d[user]:
        return "You are now logged in!"
    else:
        return "We do not recognize your username or password, please try again."

print newuser('acrease','kendall123','kendall123')
print login('acrease','kendall123')
print login('acrease','123kendall')        

    
