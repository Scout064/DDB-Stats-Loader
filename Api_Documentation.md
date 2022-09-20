# API Endpoint Documentation
#### **Disclaimer:**  
The API accepts any Data in JSON DICT Format.  

## **Scope of this document:**  
The  scope of this document is to give you (further reffered to as "the user") a general understanding on how the project works, and the ability to configure it for other IoT layouts.  

## **What does this mean?**  
This means, that you could use this project as well for other digital TTRPG or TTRPG with digital helpers like D&D Beyond for D&D.  

## **What does it take?**  
The user needs to modify the API and eventualy needs to have a way of communicating the Data as valid JSON DICT to the API (i.e. a Chrome-Extension).  

## **Licensing**  
If the user modifies the source code of this Project, the user should read the LICENSE and TERMS.md file.  
The user may change the source code but will need approval of the original author of the project and may not get any financial benefit from it.  
The user is invited to share his new code to the community here, so that we may expand the usability of our Gaming Table.  
Each Table starts of as D&D Table but may be changed according to his/her/undefined request and the availability of a community module for the wished Game Type.  
As included in the initial aqquiring of such a Table we will assist in migrating the IoT Landscape to said System.  
Further support in regards of development and software issues is limited to the original D&D Application.  
Any other Layout or IoT Landscape is subject to community support.  

## API Endpoints
There are three Endpoints exposed:  
  1) http://HOST_IP "/" -> "Homepage" of the API (templates/index.html, error.html)  
  2) http://HOST_IP "/json" -> actual json endpoint called by the Chrome-Extension  (in case of issue: templates/error.html)  
  3) http://HOST_IP "/config" -> used to configure the Player to GPIO mapping  (templates/config.html, error.html)  

As the Project is based on picoweb the html template pages are located at the root fs in the "templates" folder.  
See picowebs documentation for further information.  
