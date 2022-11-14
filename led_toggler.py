from tkinter import*
import tkinter.font 
from gpiozero import LED
import RPi.GPIO 
RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BCM) 

## hardware
redLed = LED (14)
greenLed = LED (15)
blueLed = LED (18)

## GUI DEFINITIONS ##
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font. Font(family = 'Helvetica', size = 12, weight = "bold")
count = IntVar()

### EVENT FUNCTIONS ### 
def redledToggle():
    if redLed.is_lit:
        redLed.off()
        redledButton["text"] = "Turn RED LED on"
    else:
        redLed.on()
        redledButton["text"] = "Turn RED LED off"
        greenLed.off()
        greenledButton["text"] = "Turn GREEN LED on"
        blueLed.off()
        blueledButton["text"] = "Turn BLUE LED on"

def greenledToggle():
    if greenLed.is_lit:
        greenLed.off()
        greenledButton["text"] = "Turn GREEN LED on"
    else:
        greenLed.on()
        greenledButton["text"] = "Turn GREEN LED off"
        redLed.off()
        redledButton["text"] = "Turn RED LED on"
        blueLed.off()
        blueledButton["text"] = "Turn BLUE LED on"

def blueledToggle():
    if blueLed.is_lit:
        blueLed.off()
        blueledButton["text"] = "Turn BLUE LED on"
    else:
        blueLed.on()
        blueledButton["text"] = "Turn BLUE LED off"
        redLed.off()
        redledButton["text"] = "Turn RED LED on"
        greenLed.off()
        greenledButton["text"] = "Turn GREEN LED on"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

### WIDGETS ###
redledButton = Button (win, text = 'Turn RED LED On', font = myFont, command = redledToggle, bg = 'red', height = 1, width = 24)
redledButton.grid (row=0, column=1)
 
greenledButton = Button (win, text = 'Turn GREEN LED On', font = myFont, command = greenledToggle, bg = 'green', height = 1, width = 24)
greenledButton.grid (row=1, column=1)

blueledButton = Button (win, text = 'Turn BLUE LED On', font = myFont, command = blueledToggle, bg = 'blue', height = 1, width = 24)
blueledButton.grid (row=2, column=1)

exitButton = Button (win, text = 'Exit', font = myFont, command = close, bg = 'orange', height = 1, width = 6)
exitButton.grid (row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close) # exit cleanly

win.mainloop() # Loop forever
