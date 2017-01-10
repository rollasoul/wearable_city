# wiringPi fpr Python has to be installed to run this code (manual build): https://github.com/WiringPi/WiringPi-Python
# for Pi Zero: reroute the GPIOS following the tutorial on adafruit (https://learn.adafruit.com/adding-basic-audio-ouput-to-raspberry-pi-zero/pi-zero-pwm-audio)
# for Pi Zero: you have to rewire the GPIOS with the following command after booting: gpio_alt -p 18 -f 5

# smart street site
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys
import json
import re
from selenium import webdriver
import time
from urllib import urlretrieve
import urlparse
import urllib2

# Server
import socket
import sys

# Servo Control
import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period_in = 0.015
delay_period_out = 0.02
delay_break = 1

# scrape data from smart street page
driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
driver.get("http://www.eliko.ee/smartcity/") 
time.sleep(3)
noise = driver.find_element_by_id("noise").text
cars = driver.find_element_by_id("cars").text

for item in noise.split("\n"):
  if "dB" in item:
    print item.strip()
    noise = item.strip()
driver.close()

print noise

# server and servo listen                                                
while True:
        # adjust servo to heartrate
    for pulse in range(50, 150, 1):
      wiringpi.pwmWrite(18, pulse)
      time.sleep(delay_period_in * 60 / output) 
    for pulse in range(150, 50, -1):
      wiringpi.pwmWrite(18, pulse)
      time.sleep(delay_period_out * 60 / output)
    time.sleep(delay_break * 60 / output)

