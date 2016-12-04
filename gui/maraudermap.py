# Python2/3 Independent Code 
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import threading
from time import sleep

try:
    from tkinter import *
    from queue import *
except ImportError:
    from Tkinter import *
    from Queue import *

class MarauderMapEvent(threading.Thread):
    """Marauder Map Event Processor: Feeds Display Events to GUI""" 
    def __init__(self, q):
	    """Set the MAP parameters""" 
	    threading.Thread.__init__(self)
	    self.daemon=True
	    self.q = q

    def run(self):
	    print("Event Thread Start")
	    for i in range(10):
	      sleep(1)
	      self.q.put((i, i+1))
	      print("Event Thread Quit...")
        
class MarauderMapGui():
  """Marauder Map GUI""" 
  def __init__(self, q):
    self.q = q
    self.count=0
    self.create_widgets()
    self.run_loop()

  def create_widgets(self):
	  self.root = root = Tk()
	  root.protocol("WM_DELETE_WINDOW", self.quit_loop)
	  root.grid()
	  root.title("Marauder's MAP")
	  root.geometry("200x150")
	
	  self.nikki = nikki = Label(root)
	  nikki.grid()
	  nikki["text"] = "Nikki-Location: "

	  self.pia = pia = Label(root)
	  pia.grid()
	  pia["text"] = "Pia-Location: "
    
	  self.button_quit = button_quit = Button(root)
	  button_quit.grid()
	  button_quit["text"] = "Quit"
	  button_quit["command"] = self.quit_loop

  def run_loop(self):
    self.root.after(1000, self.updateGUI)
    print("MarauderMAPGui LoopStart")
    self.root.mainloop()
    print("MarauderMAPGui LoopQuit")
    
  def __str__(self):
    """String representation of Class"""
    return "MarauderMapGUI"
  def __repr__(self):
    return "MarauderMapGUI"

  def quit_loop(self):
	  self.root.quit()
	  self.root.destroy()
      
  def updateGUI(self):
    self.count += 1
    print("updateGUI call# {0}".format(self.count))
    if (self.q.empty() == False):
	    nikki_loc, pia_loc = self.q.get()
	    print("Nikki Loc={0}: Pia Loc={1}".format(nikki_loc,pia_loc))
	    self.nikki["text"]="Nikki-Location: " + str(nikki_loc)
	    self.pia["text"]="Pia-Location: " + str(pia_loc)
	    self.root.update()

    self.root.after(1000, self.updateGUI)
	
def main():
  q = Queue()
  me = MarauderMapEvent(q)
  me.start()
  MarauderMapGui(q)
  print("Exit Program")
    
if __name__ == "__main__":
  main()
