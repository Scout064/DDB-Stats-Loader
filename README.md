# DDB-Stats-Loader/DDB-Campaign-Chardata-Loader
## D&D Beyond Campaign and Character Statistics Loader  
This tool aims at enabling a DM to display Character Stats via IoT devices.  
The Project consists of two parts:  
1) a Chrome extensions  
  1a) gathers Data from DDB and sends said data to an API
2) the API (microcontroller)  
  2a) current implemetation on micropython base.    
      Needs Board with Network capabilities.  
      Code is written for piPico but could be adapted to other boards.  
  2b) Please check requirements.txt!


## To-do  
-> Add Button to start collection instead of run at load.  
-> Change config script to reload Service Worker on Save.

### CLIENT  
-> create pythonscript for SoC (i.e. Rpi) #KILLED FOR NOW  
-> create pythonscript for Microcontroller (i.e. PiPico W) #PRIMARY FOCUS
