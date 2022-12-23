import socket, threading
from  threading import Thread
import json



SERVER = None
PORT  = 8000
IP_ADDRESS  = "192.168.0.111"

BUFFER_SIZE = 4096




class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1)
        keyboard =VKeyboard(on_key_up = self.key_up)
        self.label=Label(text ="Selected key : ",font_size ="50sp")

        layout.add_widget(self.label)
        layout.add_widget(keyboard)
        return layout
    def key_up(self, keyboard, keycode, *args):
        global SERVER
        if isinstance(keycode,tuple):
            keycode = keycode[1]
        self.label.text = "Selected key : "+str(keycode)
        print(str(keycode))
        SERVER.send((str(keycode)).encode('ascii'))
    
    def setup():
        global SERVER
        global PORT
        global IP_ADDRESS
        global remote_mouse
        PORT  = 8000
        IP_ADDRESS  = "192.168.0.111"
    
        try:
            SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            SERVER.connect((IP_ADDRESS, PORT))
            #start_write()
            return True
        except:
            return False

    setup_thread = threading.Thread(target=setup)                   #sending messages 
    setup_thread.start()        
    

        
if __name__== '__main__':
    MyApp().run()
    