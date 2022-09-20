# DDB-Stats-Loader/DDB-Campaign-Chardata-Loader
## D&D Beyond Campaign and Character Statistics Loader  
This tool aims at enabling a DM to display Character Stats via IoT devices.  
The Project consists of two parts:  
1) **Chrome extension**   
  1a) gathers Data from DDB and sends said data to an API
2) **API (microcontroller)**  
  2a) current implemetation on micropython base.    
      Needs Board with Network capabilities.  
      Code is written for piPico but could be adapted to other boards.  
  2b) _**Please check requirements.txt!**_

The project has been initially written for a commercial D&D / Gaming Table setup.    
It builds the Framework upon which the electronic and IoT infrastructure is built.  
**_(PLEASE SEE THE "LICENSE" FILE IF YOU WANT TO USE THIS PROJECT_)**.

## API Documentation  
This can be found [here]!(https://github.com/Scout064/DDB-Stats-Loader/blob/main/Api_Documentation.md)


## To-do  
-> Add Button to start collection instead of run at load.  
-> Change config script to reload Service Worker on Save.

### CLIENT  
-> create pythonscript for SoC (i.e. Rpi) #KILLED FOR NOW  
-> create pythonscript for Microcontroller (i.e. PiPico W) #PRIMARY FOCUS
