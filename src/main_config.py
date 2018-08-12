main_mod = "KEY_3"
shift_mod = "KEY_2"
num_mod = "KEY_1"
quick_open_mod = "KEY_4"

main_mode = [
    [[shift_mod], ["@dead"]],
    [[shift_mod], ["KEY_LEFTSHIFT"]],

    [["KEY_APOSTROPHE"], ["KEY_RIGHTSHIFT"]],
    [["KEY_TAB"], ["KEY_LEFTMETA"]],
    [['KEY_GRAVE'],  ["KEY_LEFTCTRL"]],
    [["KEY_CAPSLOCK", "KEY_SEMICOLON"], ["KEY_CAPSLOCK"]],

    [[num_mod], ["@dead"]],

    # get back the tab as we remapped the key earlier
    [[num_mod, "KEY_N"], [">xdotool key Tab"]],

    # all the number back as we use this row to be our primary modifiers
    [[num_mod, "KEY_M"], ["KEY_1"]],
    [[num_mod, "KEY_COMMA"], ["KEY_2"]],
    [[num_mod, "KEY_DOT"], ["KEY_3"]],
    [[num_mod, "KEY_J"], ["KEY_4"]],
    [[num_mod, "KEY_K"], ["KEY_5"]],
    [[num_mod, "KEY_L"], ["KEY_6"]],
    [[num_mod, "KEY_U"], ["KEY_7"]],
    [[num_mod, "KEY_I"], ["KEY_8"]],
    [[num_mod, "KEY_O"], ["KEY_9"]],
    [[num_mod, "KEY_SEMICOLON"], ["KEY_0"]],

    #
    # operation of main mode: movement, edition and few quick tool
    #
    [[main_mod], ["@dead"]],
    [[main_mod, "KEY_O"], ["KEY_UP"]],
    [[main_mod, "KEY_I"], ["KEY_DOWN"]],
    [[main_mod, "KEY_U"], ["KEY_LEFT"]],
    [[main_mod, "KEY_P"], ["KEY_RIGHT"]],
    [[main_mod, "KEY_J"], ["KEY_BACKSPACE"]],
    [[main_mod, "KEY_K"], ["KEY_ENTER"]],
    [[main_mod, "KEY_H"], ["KEY_ESC"]],

    [[main_mod, "KEY_9"], ["KEY_PAGEUP"]],
    [[main_mod, "KEY_8"], ["KEY_PAGEDOWN"]],
    [[main_mod, "KEY_7"], ["KEY_HOME"]],
    [[main_mod, "KEY_0"], ["KEY_END"]],

    [[main_mod, "KEY_L"], ["KEY_MINUS"]],
    [[main_mod, "KEY_SEMICOLON"], ["KEY_EQUAL"]],

    [[main_mod, "KEY_DOT"], [">xdotool key parenleft"]],
    [[main_mod, "KEY_SLASH"], [">xdotool key parenright"]],

    [[main_mod, "KEY_RIGHTBRACE"], ['>gnome-screenshot -f ~/captures/$(date +%s).png']],
    [[main_mod, "KEY_EQUAL"], ['!reload-config']],

    [[quick_open_mod], ["@dead"]],
    [[quick_open_mod, "KEY_Q"], [">su - odoo -c 'google-chrome &'"]], #
    [[quick_open_mod, "KEY_W"], [">su - odoo -c 'firefox &'"]], #
    [[quick_open_mod, "KEY_E"], [">su - odoo -c 'code --disable-gpu /home/odoo &'"]], #
    [[quick_open_mod, "KEY_R"], [">xdg-open $HOME &"]], #
]
