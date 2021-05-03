<h1> Protecting your privacy using an ESP32, an IR sensor and a python script </h1>

![alt text](https://github.com/Roadeo/esp32-ir-door-sensor/blob/main/images/setup.PNG)

This project, which I personally call the "never-gonna-catch-me-in-the-act-ever-again project", aims to secure the privacy of countless individuals around the world with an affordable and easily customizable setup. It uses easily available hardware along with simple software components.

<h2> Requirements </h2>

<h3> Hardware </h3>

* ESP-32 (although any microcontroller with Wi-Fi should do the job pretty well)
* IR sensor (ideally you would use a reed switch here, but this works fine too)

<h3> Software </h3>

* The Arduino IDE (to write the program to the ESP-32)
* Python
	* Requests module
	* pyautogui module
	* json module
<hr>

<h2> Steps </h2>

* We'll focus on the hardware part first. Connect the ESP-32 with the IR sensor. Google should give you enough details to do this. After setting up the connections, write the code in esp32-ir-sensor.ino to the ESP-32 using the Arduino IDE. Remember to change the values for the IR sensor pin number in the code if you have connected it differently, along with the SSID and password for your Wi-FI. If everything goes well, you should be able to see the output of the IR sensor at the URL http://<IP_address_of_ESP32>/door_status.

* Next, stick the ESP-32 along with IR sensor close to the door you need to monitor. If you can get one of those small square shaped breadboards with the glue already applied underneath, this step becomes much more easier. Position the IR sensor so that its signal is LOW when the door is open and HIGH when the door is closed. Refer the image in this README to get an idea of how I did it.

* That's it for the hardware part. Next download the switch-desktop-and-mute.py file to your computer where you do your private work. The script is designed to work in Windows 10. To mute the volume, I used an executable file called NirCmd. You can download it here https://www.nirsoft.net/utils/nircmd.html (I think the file is safe since lots of people use it and also because VirusTotal said so). Download the exe and move it to your Windows folder so that you can call it easily from the command line.

* And we're done. Next time you do your private business on your computer, run the script in the background. It will check the status of your door and switch desktop and mute if someone comes barging in invading your privacy.

* To make running this even simpler. Create a batch script which executes the python file. Then create a shortcut for it in Windows Desktop and make it start in minimized mode. Finally, add a keyboard shortcut to it and it will be really easy to get the whole thing working.
