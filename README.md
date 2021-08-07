# AutoHotkeyAlbion:  
This is for auto hotkey skills and etc.

You can Edit the **AlbionAutoHotkey** File if you need modifications  
**You need to run this as root on Linux**    
**Tested on Linux only**  
**You can try on Windows too**  
**Doesn't work on mobile**
## Requirements:    
**Run These Commands:**    
#### Windows:  
**Run CMD as admin**  
Install Python:  
1. Download [Python Installer for Windows](https://www.python.org/downloads/windows/)  
2. Install  
3. Check on CMD(Admin) if python is installed:  
```bash  
python
```  
  
Install pip:  
1. Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)  
2. Goto Download folder  
```python
cd <Download_folder> #Replace <Download_folder> with the actual folder path 
```  
4. Run this command:  
```bash
python get-pip.py
```  
  
Install dependencies:  
```bash
pip install dearpygui keyboard asyncio threading pyautogui  
```  
#### Linux:  
Install Python:  
```bash  
sudo apt install python3 
```  
  
Install pip:  
```bash
sudo apt install python3-pip  
```  
  
Install dependencies:  
```bash
sudo pip install dearpygui keyboard asyncio threading pyautogui  
```  
  
## Installation:    
  
1.**Clone this repository**  
2.**Extract**  
  
## Usage:  
  
Go to extracted folder:
```bash  
cd <folder>  
```  
  
Note: replace <folder> with the actual folder name !!!  
  
Then do:  
  
Windows:  
```bash  
python AlbionAutoHotkey.py  
```  
  
Linux:  
```bash
sudo python3 AlbionAutoHotkey.py
```  
**CTRL+SHIFT+C** to **[START]**  
**Move mouse pointer** to **any of the 4 corners of the screen** to **[STOP]**  
## Explanation:  
For those who know python programming and ```bash pyautogui ``` module  
if you drag your mouse to any of the 4 corners of the screen it will send ```bash pyautogui.FailSafeException ```  
which will break the loop. I have tried using a hotkey to raise the exception but unsuccessfull so I left the methods as is  
if anyone can contribute on how to bind "CTRL+Shift+C" to end the loop you can fork the repo and contribute
  
## GUI:  
![alt text](https://github.com/d4nkf0x/AutoHotkeyAlbion/blob/main/Screenshot.png?raw=true)  
**You can select the keys you want to Spam** 
