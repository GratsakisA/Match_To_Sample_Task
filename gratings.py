import numpy as np
import psychopy.visual
import psychopy.event
import psychopy.core

# Create Window
win = psychopy.visual.Window(
    size=[400,400],
    units="pix",
    fullscr=True
)

# Create Horizontal grating (Cue_Period)
horizontal_grating = psychopy.visual.GratingStim(
    win=win,
    name="horizontal_grating",
    units="pix",
    size=[200,200],
    sf=[3.0/150.0],
    mask="gauss",
    ori=90
)

# Create targetH_period

# Horizontal_grating
gratingH = psychopy.visual.GratingStim(
    win=win,
    name="gratingH",
    units="pix",
    size=[200,200],
    sf=[3.0/150.0],
    mask="gauss",
    ori=90,
    pos=[200,0]
)

# Vertical_grating
gratingV = psychopy.visual.GratingStim(
    win=win,
    name="gratingV",
    units="pix",
    size=[200,200],
    sf=[3.0/150.0],
    mask="gauss",
    ori=0,
    pos=[-200,0]
)

# Time & clock parameters
clock = psychopy.core.Clock()

n_trials = 2 # number of trials
pre_duration = 2 # duration without stimulus (seconds)
stim_duration = 3 # cueH_period (seconds)
target_duration = 8 # targetH_period (seconds)

for trial in range(n_trials):
    clock.reset()

    while clock.getTime() < pre_duration:
        win.flip()

    while clock.getTime() <= pre_duration + stim_duration:
        horizontal_grating.draw()
        horizontal_grating.phase = np.mod(clock.getTime() / 0.5, 1)
        win.flip()

    while clock.getTime() < stim_duration + target_duration:
        gratingH.draw()
        gratingV.draw()
        gratingH.phase = np.mod(clock.getTime() / 0.5, 1)
        gratingV.phase = np.mod(clock.getTime() / 0.5, 1)
        win.flip()

win.close()