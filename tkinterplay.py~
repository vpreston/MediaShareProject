"""
import cv2
cap = cv2.VideoCapture("playingvid.mp4")
cv2.namedWindow("input")
while(True):
    f, img = cap.read()
    cv2.imshow("input", img)
    cv2.waitKey(30)
"""
#!/usr/bin/env python

import sys, os, gobject
from Tkinter import *
import pygst
pygst.require("0.10")
import gst

# Goto GUI Class
class Prototype(Frame):
    def __init__(self, parent):
        gobject.threads_init()
        Frame.__init__(self, parent)    

        # Parent Object
        self.parent = parent
        self.parent.title("WebCam")
        self.parent.geometry("640x560+0+0")
        self.parent.resizable(width=FALSE, height=FALSE)

        # Video Box
        self.movie_window = Canvas(self, width=640, height=480, bg="black")
        self.movie_window.pack(side=TOP, expand=YES, fill=BOTH)

        # Buttons Box
        self.ButtonBox = Frame(self, relief=RAISED, borderwidth=1)
        self.ButtonBox.pack(side=BOTTOM, expand=YES, fill=BOTH)

        self.closeButton = Button(self.ButtonBox, text="Close", command=self.quit)
        self.closeButton.pack(side=RIGHT, padx=5, pady=5)

        self.gotoButton = Button(self.ButtonBox, text="Start", command=self.start_stop)
        self.gotoButton.pack(side=RIGHT, padx=5, pady=5)

        # Set up the gstreamer pipeline
        self.player = gst.element_factory_make("playbin2", "player")

        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect("message", self.on_message)
        bus.connect("sync-message::element", self.on_sync_message)

    def start_stop(self):
        if self.gotoButton["text"] == "Start":
            self.gotoButton["text"] = "Stop"
            self.player.set_property('uri', 'file://playingvid.mp4')
            self.player.set_state(gst.STATE_PLAYING)
        else:
            self.player.set_state(gst.STATE_NULL)
            self.gotoButton["text"] = "Start"

    def on_message(self, bus, message):
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.player.set_state(gst.STATE_NULL)
            self.button.set_label("Start")
        elif t == gst.MESSAGE_ERROR:
            err, debug = message.parse_error()
            print "Error: %s" % err, debug
            self.player.set_state(gst.STATE_NULL)
            self.button.set_label("Start")

    def on_sync_message(self, bus, message):
        if message.structure is None:
            return
        message_name = message.structure.get_name()
        if message_name == "prepare-xwindow-id":
            # Assign the viewport
            imagesink = message.src
            imagesink.set_property("force-aspect-ratio", True)
            imagesink.set_xwindow_id(self.movie_window.window.xid)

def main():
    root = Tk()
    app = Prototype(root)
    app.pack(expand=YES, fill=BOTH)
    root.mainloop()  


if __name__ == '__main__':
     main()
"""
#!/usr/bin/python
import gst # gstreamer
import glib
import sys

class Playbin2:
    def __init__(self):
        self.idle = True # not playing at the moment
        # create a playbin2 pipe
        self.player = gst.element_factory_make("playbin2", "player")
        # connect a signal handler to it's bus
        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)

    def on_message(self, bus, message):
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.player.set_state(gst.STATE_NULL)
            self.idle = True
        elif t == gst.MESSAGE_ERROR:
            err, debug = message.parse_error()
            print >> sys.stderr, "Error: {0} {1}".format(err, debug)
            self.player.set_state(gst.STATE_NULL)
            self.idle = True
        return self.idle

    def play(self, stream):
        # abort previous play if still busy
        if not self.idle:
            print >> sys.stderr, 'audio truncated'
            self.player.set_state(gst.STATE_NULL)
        self.player.set_property("uri", stream)
        self.player.set_state(gst.STATE_PLAYING)
        self.idle = False # now playing

# a test program for our basic gstreamer class
# plays a standard system sound than hangs in message pump loop
# use Ctrl-C to get out
if __name__ == "__main__":
    Playbin2().play("File:///home/victoria/MediaShareProject/playingvid.mp3")
    glib.MainLoop().run() 
    """
