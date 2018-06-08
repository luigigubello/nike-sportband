# Nike+ Sportband Reverse Engineering

## Premise

In April, 2018, Nike finished to support some old products, so it is no longer possible to download data from old running watches, such as Nike + Sportband.

I still use Nike+ Sportband and I am a Linux user, so I looked for an alternative solution. I have found two old open source projects (~2011), written in C/C ++, for Linux users. These two projects are a complete reverse engineering of the Nike+ Sportband protocol.

The first project <a href="#link_1">[1]</a> allows to download data in hex format and convert it in clear text. The second project <a href="#link_2">[2]</a> is a complete reverse engineering of the protocol: it is possible to change nickname, time, weight, other information and extract the data of the runs in hex format, but it does not read them in clear text.

##### Useful links
* <a id="link_1" href="http://knz-blue.cocolog-nifty.com/memo/2010/06/nike-sportband.html">Nike+ SportBand log analizer for Linux
</a>

* <a id="link_2" href="https://sourceforge.net/projects/comsport/">Comsport</a>
