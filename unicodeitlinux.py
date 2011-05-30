#!/usr/bin/python
# (c) Ricardo Neves 2010

import pygtk
pygtk.require('2.0')
import gtk
from unicodeit import replace
import subprocess

def ShowPopup(txt):
    label = gtk.Label(txt)
    label.set_selectable(True)
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.connect("destroy", lambda w: gtk.main_quit())
    window.set_title("UnicodeIt")
    window.add(label)
    window.resize(100,100)
    window.show_all()

clipboard = gtk.clipboard_get("PRIMARY")
cb2 = gtk.clipboard_get()
text = clipboard.wait_for_text()
utxt = replace([text])
cb2.set_text(utxt[0])
cb2.store()

#use xdotool to tget active window and type into it:
process = subprocess.Popen(['xdotool','getactivewindow'], shell=False, stdout=subprocess.PIPE)
winid = process.communicate()[0].strip()
subprocess.Popen([r'xdotool','key','--window',winid,'ctrl+v']).wait()


#ShowPopup(winid)
#gtk.main()
