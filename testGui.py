import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
    with dpg.font("C:\\Windows\\Fonts\\Arial\\arial.ttf", 20) as font1:

        # add the default font range
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)

        # helper to add range of characters
        #    Options:
        #        mvFontRangeHint_Japanese
        #        mvFontRangeHint_Korean
        #        mvFontRangeHint_Chinese_Full
        #        mvFontRangeHint_Chinese_Simplified_Common
        #        mvFontRangeHint_Cyrillic
        #        mvFontRangeHint_Thai
        #        mvFontRangeHint_Vietnamese
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)

        # add specific range of glyphs
        dpg.add_font_range(0x3100, 0x3ff0)

        # add specific glyphs
        dpg.add_font_chars([0x3105, 0x3107, 0x3108])

        # remap や to %
        dpg.add_char_remap(0x3084, 0x0025)

dpg.show_font_manager()

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()