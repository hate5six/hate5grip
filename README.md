# hate5grip

<a href="https://www.youtube.com/watch?v=o0lLO4V0J0c" target="_blank"><img src="https://img.youtube.com/vi/o0lLO4V0J0c/maxresdefault.jpg" width="50%" height="50%"/></a>

The hate5grip is a DIY wireless camera angle switcher using a Raspberry Pi Zero that sends HTTP POST requests to a Flask server running adjacent to OBS, which simulates the pressing of keys to initiate an angle switch. The grip can be used more generally as just a wireless macro keypad as needed. Code for the remote and web server and the .stl files for 3D printing to come. For a full breakdown, step by step guide and Q+A check out the livestream tutorial I'll be hosting about this build over at patreon.com/hate5six.

<h1>Installation:</h1>

There are two scripts (tested on Python 3.9) in this repository: 

<ul>
  <li><b>hate5grip.py</b>: to run as a server on the computer running OBS</li>
  <li><b>remote.py</b>: to run on the Rapberry Pi
  </ul>
  
The following dependencies are required:
<ul>
  <li><a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">Flask</a> (for server) </li>
  <li><a href="https://pypi.org/project/keyboard/" target="_blank">Keyboard</a> (for server) </li>
  <li><a href="https://gpiozero.readthedocs.io/en/stable/" target="_blank">gpiozero</a> (for remote)</li>
  </ul> 

<h2>On Computer Running OBS</h2>
Change the variable <b>IP_ADDR</b> in <b>hate5grip.py</b> to the local area network IP of the computer. From a command prompt, run <b>python hate5grip.py</b> which will launch the server and listen for POST requests from the hate5grip remote. Minimize the console and be sure that OBS is the active window/program on the screen. In OBS, go to Settings and assign hotkeys '1', '2', '3', '4' to the appropriate Scenes. 

<h2>On Remote</h2>
SSH into the Raspberry Pi and install the gpiozero dependency. Configure the RPi to connect to the same 2.4GHz WiFi network as the computer running OBS. Change the variable <b>IP_ADDR</b> in <b>remote.py</b> to the local area network UP of the computer. Modify the crontab on the RPi to automatically run <b>remote.py</b> in the background upon boot.
