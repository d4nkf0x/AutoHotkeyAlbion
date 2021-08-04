#!/bin/env python3
# Created by atbswp v0.3.1 (https://git.sr.ht/~rmpr/atbswp)
# on 30 Jul 2021
import keyboard
import pyautogui
import time
import asyncio
import threading
import dearpygui.dearpygui as dpg
import dearpygui.themes as themes
i=0
is_running = False
qs_value = True
ws_value = True
es_value = True
ds_value = True
rs_value = True
fs_value = True
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05
async def albionAutoKey():
    global is_running
    while i==0 and is_running:
        try:
            if qs_value == True:
                pyautogui.hotkey('q')
            if ws_value == True:
                pyautogui.hotkey('w')
            if es_value == True:
                pyautogui.hotkey('e')
            if ds_value == True:
                pyautogui.hotkey('d')
            if rs_value == True:
                pyautogui.hotkey('r')
            if fs_value == True:
                pyautogui.hotkey('f')
        except:
            is_running = False
            break
def check_errors():
    global is_running
    if is_running == True:
        is_running = False
    else:
        is_running = True
        asyncio.run(albionAutoKey())
def test():
    keyboard.add_hotkey('ctrl+shift+c',check_errors)
    keyboard.wait()

theme = themes.create_theme_imgui_light()
vp = dpg.create_viewport(title='Hotkey Spammer[MMORPG]', width=200, height=200,clear_color = [0,0,0,0])
with dpg.value_registry():
    q_value = dpg.add_bool_value(default_value =True)
    w_value = dpg.add_bool_value(default_value =True)
    e_value = dpg.add_bool_value(default_value =True)
    r_value = dpg.add_bool_value(default_value =True)
    d_value = dpg.add_bool_value(default_value =True)
    f_value = dpg.add_bool_value(default_value =True)
def change_values(sender,app_data,user_data):
    global qs_value,ws_value,es_value,ds_value,rs_value,fs_value
    if  sender == 1:
        qs_value = app_data
    elif sender == 2:
        ws_value = app_data
    elif sender == 3:
        es_value = app_data
    elif sender == 4:
        ds_value = app_data
    elif sender == 5:
        rs_value = app_data
    elif sender == 6:
        fs_value = app_data
    print(sender)
with dpg.window(label="Auto Hotkey Configs") as main_window:
    dpg.add_text("Hotkey Configs: ")
    dpg.add_text("Control+Shift+C to [Start]")
    dpg.add_text("Move [Mouse Pointer] to any corners of the screen")
    dpg.add_text("to [Stop]")
    dpg.add_checkbox(id=1,label="Q",source=q_value,callback=change_values)
    dpg.add_checkbox(id=2,label="W",source=w_value,callback=change_values)
    dpg.add_checkbox(id=3,label="E",source=e_value,callback=change_values)
    dpg.add_checkbox(id=5,label="R",source=r_value,callback=change_values)
    dpg.add_checkbox(id=4,label="D",source=d_value,callback=change_values)
    dpg.add_checkbox(id=6,label="F",source=f_value,callback=change_values)
dpg.set_primary_window(main_window,True)
dpg.setup_dearpygui(viewport=vp)
dpg.show_viewport(vp)
x=threading.Thread(target=test)
x.start()
dpg.start_dearpygui()
