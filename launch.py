import tkinter as tk
import FormantSynth
import engIpa
import textSpeech
window = tk.Tk()

fS = tk.Button(window, text="Formant Synth", fg="red", command=lambda: FormantSynth.run())
eI = tk.Button(window, text="Phonetic Spelling", fg="blue", command=lambda: engIpa.run())
tS = tk.Button(window, text="TTS", fg="green", command=lambda: textSpeech.run())
fS.place(x=100,y=100)
eI.place(x=200,y=100)
tS.place(x=350,y=100)
window.title('Synthesis Suite')
window.geometry("600x600+10+20")
window.mainloop()