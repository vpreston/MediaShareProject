"""
Victoria Preston
November 16, 2013
Minimum Deliverable mock up - an attempt at creating a URL sender
"""

from swampy.Gui import *

selector = []

class Sharer(Gui):

    def framework(self):
        self.title('Minumum Deliverable URLSender')
        self.col()
        en = self.en(text = 'Insert URL here')
        self.row([0,1], pady = 30)
        self.endrow()
        self.bu(text = 'Share', command = Callable(print_entry, self, en))
        
        self.bu(text = 'Update Share History', command = Callable(update, self, en))
        
        self.row([0,1], pady = 30)
        self.endrow()
        self.endcol() 
        
        
def update(gui, en):
    log = en.get()
    try:
        selector.append(log)
    except:
        selector = [log]
    mb = gui.mb()
    mb.config(text = selector[0])
    for select in selector:
        gui.mi(mb, text = select, command=Callable(set_select, mb, select))


def print_entry(gui, en):
    text = en.get() 
    follower = ' was shared with a friend!'
    message = text + follower
    item = gui.la()
    try:
        item.config(text = message)
    except:
        pass

def set_select(mb, select):
    mb.config(text = select)
    


    


g = Sharer()
g.framework()
g.mainloop()



"""
selector = [0,1,2]
        mb = self.mb(text = selector[0])
        for select in selector:
            self.mi(mb, text = select, command=Callable(set_select, mb, select))

"""
