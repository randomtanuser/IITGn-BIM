#Importing the required libraries. 
from psychopy import visual, core, logging, event
from datetime import datetime
from psychopy.hardware import keyboard
from psychopy import gui

#Add participant information
participant = gui.Dlg(title = "Participant info")
participant.addText('Please fill in your name:')
participant.addField('Name:')
participant.show()
if participant.OK:
    Name = participant.data[0]
print(Name)

# Set logging level and create log file with timestamp
timestamp=datetime.now().strftime("%Y%m%d-%H%M%S")
lastLog = logging.LogFile(Name +timestamp+".log", level=logging.INFO, filemode='w')
# Here the 'name' variable form the participant info is added to the name of the logfile. 

#Monitor and window specifications
mywin = visual.Window([1366, 768], monitor="New", units="deg", color = 'black',)
kb = keyboard.Keyboard()

#Intructions for the participants
Participant_Instruction = visual.TextStim(mywin, text =''' 
Welcome! 
Instructions: 
    1. You will be shown an experimental set of four shapes with colours. Please look at them carefully. 
    2. You will then be presented with another shape. You are required to ignore this. 
    3. A final image will be shown. Please report whether this image was present in the set of first four images.
    4. Press 1 for "Yes" and 2 for "No"', 
''')   
Participant_Instruction.draw()
mywin.update()
Subject_Response = event.waitKeys(keyList=['1', '2'])
print(Subject_Response)

#Initial Blank screen; to focus on the center
start = visual.TextStim(mywin, text = '+')
start.draw()
for frame in range(100):
    start.draw()
    mywin.update()
    
#Trial 1 - Plausible suffix
trial_1 = visual.TextStim(mywin, text ='''Trial 1
Ready?''')
for frame in range(150):
    trial_1.draw()
    mywin.update()
   
    
#Experimental set: introduce four image as a stimulation
redcircle = visual.ImageStim(win=mywin, image="redcircle.png", size=10, pos=[-10,-8], units="deg")
yellowspark = visual.ImageStim(win=mywin, image="yellowspark.png", size=10, pos=[-10,8], units="deg")
purpletriangle = visual.ImageStim(win=mywin, image="purpletriangle.png", size=10, pos=[10,-8], units="deg")
limehexagon = visual.ImageStim(win=mywin, image="limehexagon.png", size=10, pos=[10,8], units="deg")

# Stimulus shown for 5s, refresh rate = 50Hz
for frame in range(250):
   redcircle.draw()
   yellowspark.draw()
   purpletriangle.draw()
   limehexagon.draw()
   mywin.update()
   
   
 #Blank screen after array stimuli
start = visual.TextStim(mywin, text = '+')
start.draw()
for frame in range(100):
    start.draw()
    mywin.update()

# Showing the plausible stimuli
psuffix = visual.ImageStim(win=mywin, image="orangeoval.png", size=10, pos=[0,0], units="deg")
for frame in range(50):
    psuffix.draw()
    mywin.update()
    
#Blank screen after array stimuli
start = visual.TextStim(mywin, text = '+')
start.draw()
for frame in range(150):
    start.draw()
    mywin.update()
    
#Showing the test cue and answer
testcue = visual.ImageStim(win=mywin, image="redcircle.png", size=10, pos=[0,0], units="deg")
answer = visual.TextStim(mywin, text ='Was this image present in the first set of images?', pos=[0, 10])
for frame in range(150):
    testcue.draw()
    answer.draw()
    mywin.update()
Subject_Response = event.waitKeys(keyList=['1', '2'])
print(Subject_Response)


#Trial 2. Implausible suffix

trial_2 = visual.TextStim(mywin, text = '''Trial 2
Ready?''')
for frame in range(200):
    trial_2.draw()
    mywin.update()

start = visual.TextStim(mywin, text = '+')
start.draw()
for frame in range(150):
    start.draw()
    mywin.update()

#introduce four image as a stimulation
bluediamond = visual.ImageStim(win=mywin, image="bluediamond.png", size=10, pos=[10,8], units="deg")
yellowspark = visual.ImageStim(win=mywin, image="yellowspark.png", size=10, pos=[-10,8], units="deg")
greenpentagon = visual.ImageStim(win=mywin, image="greenpentagon.png", size=10, pos=[10,-8], units="deg")
limehexagon = visual.ImageStim(win=mywin, image="limehexagon.png", size=10, pos=[-10,-8], units="deg")


# Stimulus shown for 5s, refresh rate = 50Hz
for frame in range(250):
   bluediamond.draw()
   yellowspark.draw()
   greenpentagon.draw()
   limehexagon.draw()
   mywin.update()
    
#Blank screen after array stimuli
start = visual.TextStim(mywin, text = '+')
start.draw()
for frame in range(150):
    start.draw()
    mywin.update()

# Showing the implausible stimuli
implausiblesuffix = visual.ImageStim(win=mywin, image="lavrectangle.png", size=10, pos=[0,0], units="deg")
for frame in range(50):
    implausiblesuffix.draw()
    mywin.update()

#Blank screen after array stimuli
start = visual.TextStim(mywin, text = '+')
start.draw()
for frame in range(150):
    start.draw()
    mywin.flip()
    
#Showing the test cue and answer
testcue2 = visual.ImageStim(win=mywin, image="bluesquare.png", size=10, pos=[0,0], units="deg")
answer = visual.TextStim(mywin, text ='Was this image present in the first set of images?', pos=[0, 10])
for frame in range(150):
    testcue2.draw()
    answer.draw()
    mywin.update()
Subject_Response = event.waitKeys(keyList=['1', '2'])
print(Subject_Response)

#Trail3 - Control

trial_3 = visual.TextStim(mywin, text = '''Trial 3
Ready?''')
for frame in range(200):
    trial_3.draw()
    mywin.update()
    
    
start = visual.TextStim(mywin, text = '+')
start.draw()
for frame in range(150):
    start.draw()
    mywin.update()

#introduce four image as a stimulation
bluediamond = visual.ImageStim(win=mywin, image="bluediamond.png", size=10, pos=[-10,8], units="deg")
lavrectangle = visual.ImageStim(win=mywin, image="lavrectangle.png", size=10, pos=[10,8], units="deg")
greenpentagon = visual.ImageStim(win=mywin, image="greenpentagon.png", size=10, pos=[-10,-8], units="deg")
bluestar = visual.ImageStim(win=mywin, image="bluestar.png", size=10, pos=[10,-8], units="deg")

# Stimulus shown for 5s, refresh rate = 50Hz
for frame in range(250):
   bluediamond.draw()
   lavrectangle.draw()
   greenpentagon.draw()
   bluestar.draw()
   mywin.update()
    
#Blank screen after array stimuli
start = visual.TextStim(mywin, text = '+')
start.draw()
for frame in range(150):
    start.draw()
    mywin.update()

    
#Showing the test cue and answer
testcue2 = visual.ImageStim(win=mywin, image="bluesquare.png", size=10, pos=[0,0], units="deg")
answer = visual.TextStim(mywin, text ='Was this image present in the first set of images?', pos=[0,10])
for frame in range(150):
    testcue2.draw()
    answer.draw()
    mywin.update()
Subject_Response = event.waitKeys(keyList=['1', '2'])
print(Subject_Response)

#Thank you message
thankmsg = visual.TextStim(mywin, text = 'Thank you for your participation!')
for frame in range(150):
   thankmsg.draw()
   mywin.update()

mywin.close()
core.quit()
