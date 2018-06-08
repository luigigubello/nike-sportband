# Nike+ Sportband Reverse Engineering

## Premise

In April, 2018, Nike finished to support some old products, so it is no longer possible to download data from old running watches, such as Nike + Sportband.

I still use Nike+ Sportband and I am a Linux user, so I looked for an alternative solution. I have found two old open source projects (~2011), written in C/C ++, for Linux users. These two projects are a complete reverse engineering of the Nike+ Sportband protocol.

The first project <a href="#link_1">[1]</a> allows to download data in hex format and convert it in clear text. The second project <a href="#link_2">[2]</a> is a complete reverse engineering of the protocol: it is possible to change nickname, time, weight, other information and extract the data of the runs in hex format, but it does not read them in clear text.

Using the PyUSB <a href="#link_3">[3]</a> I have translated these two codes into Python to extract data from my Sportband. This work is not finished, but I have decided to publish the code written so far. <i>This is good failure</i>.

##### Useful links
* <a id="link_1" href="http://knz-blue.cocolog-nifty.com/memo/2010/06/nike-sportband.html">Nike+ SportBand log analizer for Linux</a>

* <a id="link_2" href="https://sourceforge.net/projects/comsport/">Comsport</a>

* <a id="link_3" href="http://pyusb.github.io/pyusb/">PyUSB</a>

* <a href="https://github.com/Jurph/sportwatch">Hacking the Nike+ sportwatch</a>

* <a href="https://www.os3.nl/_media/2013-2014/courses/ccf/smartwatches-hristo-leendert.pdf">[PDF] Information retrieval from a TomTom Nike+ smart watch</a>

* <a href="http://dmitry.gr/?r=05.Projects&proj=05.%20Nike%20plus%20iPod">Nike+iPod reverse engineering (protocol too)</a>

* <a href="https://www.evilsocket.net/2015/01/29/nike-fuelband-se-ble-protocol-reversed/">Nike+ FuelBand SE BLE Protocol Reversed</a>

## How it works

To download data from Nike+ Sportband on Windows I had to use Nike + Connect. It downloaded the data and uploaded it to my own Nike profile. Now the online service is offline, so Nike+ Connect doesn't work.
The only useful features of Sportband are:
* date
* time
* weight

So I worked on these features, the Python code can:
* read and set the weight
* set date and time, by reading the date of the computer
* extracts data in hex format

For now the Python code can not:
* reset the device
* read the dumped data

This last feature is the most important, it is possible to use the project <a href="#link_1">[1]</a> to read the data. The developer did an awesome reverse engineering work!
I hope to finish this script soon.

The script is written in Python <b>2.7.x</b>.



