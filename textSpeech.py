import dearpygui.dearpygui as dpg
import gtts
import os



def playSound(sender,data,user_data):
    inText = dpg.get_value(user_data[0])
    language = dpg.get_value(user_data[1])
    print(language[language.find(")(")+2:len(language)-1])
    myobj = gtts.gTTS(text=inText, tld=language[language.find(")(")+2:len(language)-1], lang=language[language.find("(")+1:language.find("(")+3], slow=False)
    myobj.save("ttsplayer.wav")
    os.system("ttsplayer.wav")


def run():
    word = ""
    language_list = ["American English (en)(com)", "British English (en)(co.uk)", "Canadian English (en)(ca)", "Australian English (en)(com.au)", "Indian English (en)(co.in)", "Irish English (en)(ie)", "South African English (en)(co.za)", "Canadian French (fr)(ca)", "French (fr)(fr)", "Mandarin-China Mainland (zh-CN)(com)", "Mandarin-Taiwan (zh-TW)(com)", "Brazilian Portuguese (pt)(com.br)", "Portuguese (pt)(pt)", "Mexican Spanish (es)(com.mx)", "Spanish (es)(es)", "United States Spanish (es)(com)"]
    with dpg.window(tag="Speaker Window"):
    # When creating items within the scope of the context
    # manager, they are automatically "parented" by the
    # container created in the initial call. So, "window"
    # will be the parent for all of these items.
        lister = dpg.add_listbox(label="Languages", items = language_list, num_items=3)
        inputtxt = dpg.add_input_text(label="Word", hint="Enter a word to speak...")
        text = dpg.add_text(word)
        play = dpg.add_button(label="Play", callback=playSound, user_data=[inputtxt, lister])