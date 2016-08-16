# RaspberryPiExamples
Raspberry Pi GPIO Examples


## HD44780 Display example
* Change your **pin numbers** in _Display/gpio_helper.py_
* Connect HD44780 to default ports:
  * **VSS (source supply)** _pin 1_ ==> GND
  * **VDD (drain supply)** _pin 2_ ==> +5V
  * **V0** _pin 3_ ==> GND
  * **RS** _pin 4_ ==> PIN 40
  * **R/W** _pin 5_ ==> GND
  * **E (enable)** _pin 6_ ==> PIN 38
  * **D4** ==> PIN 36
  * **D5** ==> PIN 32
  * **D6** ==> PIN 26
  * **D7** ==> PIN 24
