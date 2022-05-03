from datetime import datetime
from tkinter import *
import threading
root = Tk()
label = Label( root, height = 10, width = 100, padx = 4, pady = 4, text="Chargement...")
label.pack()
def get_time():
	while True:
		t = datetime.today()
		label["text"] = "%s:%s:%s" % (t.hour, t.minute, t.second)

threading.Thread(target=get_time).start()
root.mainloop()
