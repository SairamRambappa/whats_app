# whatsapp_scripts
##Scripts to monitor target's online status

#####Prerequisite :

1. Chrome browser.
2. Python with packages - selenium.


Items included :

1. Script to monitor the target online status.
2. Chrome webdriver.

Important things to remember : 
1. Make sure the contact is atleast in the top 5 people of your recent contacts ( Mandatory ) .
2. Save the target name as simple as you can , if possible without spaces ( not mandatory ) 


Description:

1. Run the script on any terminal , this will open up a chrome browser , please scan the QR code and enter the target's name 

```Command : python monitor_whatsapp.py <interval> <duration>```

For example if you wanna monitor jack for 2 hours and check the status every 5 min, 
          ``` python monitor_whatsapp.py 5 2 ```

2. Please dont close the terminal and the chrome browser that the script opened.
3. Once the script finishes , we will get a csv file with name,time,status information.	  
                          


