# SPDX-FileCopyrightText: 2021 Phillip Torrone for Adafruit Industries
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-FileCopyrightText: 2022 Tom Paine
# SPDX-License-Identifier: MIT

import time
from rainbowio import colorwheel
from adafruit_circuitplayground import cp

num_pixels = 10
cp.pixels.brightness = 0.8
cp.pixels.auto_write = False
cycle_fast_delay = 0.0001
cycle_slow_delay = 1.0


def buttons_pressed():
    return cp.button_a or cp.button_b


def rainbow_cycle():
    while not buttons_pressed():
        for j in range(255):
            # Allow escape from slow delay loop
            if buttons_pressed():
                break
            for i in range(num_pixels):
                rc_index = (i * 256 // num_pixels) + j
                # print(rc_index)
                cp.pixels[i] = colorwheel(rc_index & 255)
            cp.pixels.show()
            if cp.switch:
                time.sleep(cycle_fast_delay)
            else:
                time.sleep(cycle_slow_delay)
    cp.red_led = not cp.red_led
    time.sleep(1)

def dual_cycle():
    while not buttons_pressed():
        for j in range(255):
            # Allow escape from slow delay loop
            if buttons_pressed():
                break
            for i in range(num_pixels):
                rc_index = int(i * 256 // num_pixels / 5) + j
                print(rc_index)
                cp.pixels[i] = colorwheel(rc_index & 255)
            cp.pixels.show()
            if cp.switch:
                time.sleep(cycle_fast_delay)
            else:
                time.sleep(cycle_slow_delay)

    cp.red_led = not cp.red_led
    time.sleep(1)


def single_cycle():
    while not buttons_pressed():
        for j in range(255):
            # Allow escape from slow delay loop
            if buttons_pressed():
                break
            print("single " + str(j))
            cp.pixels.fill(colorwheel(j))
            cp.pixels.show()
            if cp.switch:
                time.sleep(cycle_fast_delay)
            else:
                time.sleep(cycle_slow_delay)

    cp.red_led = not cp.red_led
    time.sleep(1)

while True:
    rainbow_cycle()
    dual_cycle()
    single_cycle()
