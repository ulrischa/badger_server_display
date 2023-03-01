# Run Server on Pimoroni Badger 2040 w to display Text
The Pimoroni Badger 2040 was already cool, but the [wifi version](https://shop.pimoroni.com/products/badger-2040-w) is even cooler. 

Would it not be cool to have a server running on the badger? What would be possible?

To try it out I just build a simple script that runs a webserver on the pico, displays the local adress on boot and then you can send a get request to show a text you like on the display.
This setup is very basic but powerfull. You could use this get request from any other device or in your smart home setup. I use it from Node Red after a specific flow to show the status on the badger.

## How does it work?
Well there is another cool library from pimoroni here on Github that makes this a simple task: [phew!](https://github.com/pimoroni/phew)
It has all you need to set up a webserver on the raspberry pico and so also on the badger 2040 w.

## Install
1. Set up the badger as described [here](https://learn.pimoroni.com/article/getting-started-with-badger-2040-w)
2. In Thonny load the phew! library by clicking Tools -> Manage packages and searching for micropython-phew
3. Replace wifi_ssid= "XXX" and wifi_pw = "XXX" in txtsrv.py with your wifi data
3. Connect the badger with your computer. Double click examples to go in that directory. Load the script txtsrv.py and the icon-txtsrv.jpg to the badger example directory with Thonny (upload to /examples)
4. Disconnect and boot again

## Use
When badger is up and running you see a SRV icon. If you start that app the led is goes on. On the display the URL is shown where you can send the text.

## Further development
The display is very basic -> can be improved
The badger could run in access point mode if running in lan is not wanted
