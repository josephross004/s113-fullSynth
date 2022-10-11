import dearpygui.dearpygui as dpg
import FormantSynth
import engIpa
import textSpeech
dpg.create_context()


with dpg.window(tag="Primary Window"):
    # When creating items within the scope of the context
    # manager, they are automatically "parented" by the
    # container created in the initial call. So, "window"
    # will be the parent for all of these items.

    button1 = dpg.add_button(label="Formant Phoneme Synthesizer", callback=lambda: FormantSynth.run())
    button2 = dpg.add_button(label="English Phonetic Spelling", callback=lambda: engIpa.run())
    button3 = dpg.add_button(label="Multilingual Speech Synthesizer", callback=lambda: textSpeech.run())

with dpg.font_registry():
    with dpg.font("unifont.ttf", 16) as unifont:
        dpg.add_font_range(0x0250, 0x02ff)
        dpg.add_font_range(0x1D00, 0x1D7F)
        dpg.add_font_range(0x1D80, 0x1DBF)
        dpg.add_font_range(0x02B0, 0x02FF)
        dpg.add_font_range(0x0300, 0x036F)
    dpg.bind_font(unifont)

with dpg.theme() as red_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (127,0,51), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)

with dpg.theme() as green_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (0,127,51), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)

with dpg.theme() as blue_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (51,0,78), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 0, category=dpg.mvThemeCat_Core)

dpg.bind_item_theme(button1, red_theme)
dpg.bind_item_theme(button2, green_theme)
dpg.bind_item_theme(button3, blue_theme)



dpg.create_viewport(title='Speech Synthesis Suite', width=1000, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
'''
fS = tk.Button(window, text="Formant Synth", fg="red", command=lambda: FormantSynth.run())
eI = tk.Button(window, text="Phonetic Spelling", fg="blue", command=lambda: engIpa.run())
tS = tk.Button(window, text="TTS", fg="green", command=lambda: textSpeech.run())
fS.place(x=100,y=100)
eI.place(x=200,y=100)
tS.place(x=350,y=100)
window.title('Synthesis Suite')
window.geometry("600x600+10+20")
window.mainloop()
'''
dpg.destroy_context()