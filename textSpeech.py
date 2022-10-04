import tkinter as tk
import gtts
import os



def playSound(inText):
    myobj = gtts.gTTS(text=inText, lang="en", slow=False)
    myobj.save("ttsplayer.wav")
    os.system("ttsplayer.wav")

def run():
    window = tk.Tk()
    inputtxt = tk.Text(window, height = 5, width = 20)
    inputtxt.pack()
    submitButton = tk.Button(window, text = "Print", command = lambda:playSound(inputtxt.get(1.0, "end-1c")))
    submitButton.pack()
    #options for dropdown
    def show():
        tk.label.config( text = clicked.get() )
    options = [
        "English (American)",
    ]
    # datatype of menu text
    clicked = tk.StringVar()
  
    # initial menu text
    clicked.set( "Monday" )
  
    # Create Dropdown menu
    drop = tk.OptionMenu( window , clicked , *options )
    drop.pack()
    button = tk.Button( window , text = "click Me" , command = show ).pack()
    window.title('Synthesis Suite')
    window.geometry("600x600+10+20")
    window.mainloop()