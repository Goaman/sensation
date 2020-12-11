# import asyncio
import re
import subprocess
import sys
import importlib
import argparse

import evdev
from evdev import AbsInfo, InputDevice, UInput, categorize, ecodes as e

from tools import isalambda

parser = argparse.ArgumentParser(prog='sensation')
parser.add_argument('--debug',
                    action='store_true',
                    help='log usefull information for debugging purpose')
parser.add_argument('-c', '--config-file',
                    metavar='<config.py>',
                    help='set your own python config file')
parser.add_argument('input_id',
                    help='the input id of your "/dev/input/eventX"')
parsed_args = parser.parse_args()

if parsed_args.config_file:
    import importlib.util
    spec = importlib.util.spec_from_file_location("main_config", parsed_args.config_file)
    main_config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_config)
else:
    import main_config
modeAwesome = main_config.main_mode

capup = False
powermode = False
awesomemode = True

key_states = {}
special_key = {}

print("grabbing and listening device /dev/input/event" + parsed_args.input_id)
dev = InputDevice('/dev/input/event' + parsed_args.input_id)
ui = UInput()
dev.grab()

def up_all_keys():
    for key, is_kup in key_states.items():
        if is_kup:
            ui.write(e.EV_KEY, e.ecodes[key], 0)
            ui.syn()

# TODO: should be encapsulated by a 'resolver'
for event in dev.read_loop():
    if event.type == e.EV_KEY:
        if parsed_args.debug:
            print("event keycode",categorize(event).keycode)
        kevent = categorize(event)

        # set the keystate for later check if a particular key is pressed or not

        if isinstance(kevent.keycode, list):
            event_codes = kevent.keycode
        else:
            event_codes = [kevent.keycode]
        if event.value == 1:
            for event_code in event_codes:
                key_states[event_code] = True
        elif event.value == 0:
            for event_code in event_codes:
                key_states[event_code] = False

        # hard code capslock+key_a and capslock+key_s to easily switch on/off the remapping
        if kevent.keycode == 'KEY_CAPSLOCK':
            # down
            if event.value == 1:
                capup = True
            # up
            elif event.value == 0:
                capup = False
        else:
            # skiWrite is set to true when a 'custom' modifier key is 'ON'
            skip_write = False

            if kevent.keycode == 'KEY_A' and event.value == 1 and capup == True:
                powermode = not powermode
            elif kevent.keycode == 'KEY_S' and event.value == 1 and capup == True:
                awesomemode = not awesomemode
                skip_write = True

            if not awesomemode and not skip_write:
                ui.write_event(event)
                ui.syn()
                skip_write = False
                continue

            if powermode:
                continue

            for item in modeAwesome:
                # TODO: refactor this nasty way of configuring mapping
                road = item[0]
                actions = item[1]

                modif_keys = road[:-1]
                key = road[-1]

                # check if all the modifier keys are set
                modif_ok = True
                for modif_key in modif_keys:
                    if re.match(r"^@", modif_key) and (not modif_key in special_key or special_key[modif_key]):
                        modif_ok = False
                        break
                    elif not modif_key in key_states or key_states[modif_key] == False:
                        modif_ok = False
                        break
                    up_all_keys()

                does_key_match = any(event_key == key for event_key in event_codes)
                if modif_ok and does_key_match:
                    skip_write = True
                    if isalambda(actions[0]):
                        actions[0]()
                    else:
                        match_shell = re.match(r"^>(.*)", actions[0])
                        if re.match(r"^@", actions[0]):
                            if event.value == 1:
                                special_key[actions[0]] = True
                            elif event.value == 0:
                                special_key[actions[0]] = False
                        elif re.match(r"^!reload-config", actions[0]):
                            print("reloading config")
                            try:
                                importlib.reload(main_config)
                                modeAwesome = main_config.main_mode
                            except Exception as ex:
                                print("error while trying to reload configuration:")
                                print(ex)
                        elif match_shell:
                            if event.value == 1 or event.value == 2:
                                subprocess.call(match_shell[1], shell=True)
                        else:
                            # TODO: remove logging in some condition to avoid keylogging
                            if parsed_args:
                                print("write key %s with value %s" % (actions[0], event.value))
                            ui.write(e.EV_KEY, e.ecodes[actions[0]], event.value)
                            ui.syn()

                # allow a key to trigger up back otherwise, a remapping keep repeating
                elif event.value == 0 and not skip_write and does_key_match:
                    if re.match(r"^KEY", actions[0]):
                        ui.write(e.EV_KEY, e.ecodes[actions[0]], event.value)
                        ui.syn()


            if not skip_write:
                ui.write_event(event)
                ui.syn()

ui.close()
