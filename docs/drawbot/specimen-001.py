# RENDER THIS DOCUMENT WITH DRAWBOT: http://www.drawbot.com
from drawBot import *
import math

#[W]IDTH,[H]EIGHT,[M]ARGIN,[F]RAMES
W,H,M,F = 1024,512,64,64

# DRAWS A GRID
def grid():
    stroke(0.2)
    strokeWidth(1)
    rect(M, M, W-(M*2), H-(M*2))
    stpX, stpY = 0, 0
    incX, incY = M/2, M/2
    for x in range(29):
        polygon((M+stpX, M),
                (M+stpX, H-M))
        stpX += incX
    for y in range(13):
        polygon((M, M+stpY),
                (W-M, M+stpY))
        stpY += incY

# REMAP INPUT RANGE TO VF AXIS RANGE
# (E.G. SINE WAVE(-1,1) to WGHT(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan  = inputMax  - inputMin   # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)

# NEW PAGE
def new_page():
    newPage(W, H)
    #frameDuration(1/24)
    fill(0)
    rect(-2, -2, W+2, H+2)

# MAIN
# for axis, data in listFontVariations().items(): print((axis, data))
new_page()
font("fonts/ttf/Wallingford.ttf")
grid() # Toggle for grid view
fill(1)
stroke(None)
fontSize(M*2.6)
text("Free education for all", (M*1, M*5))
text("No tuition fees!", (M*1, M*3))
text("the Stranger", (M*1, M*1))
saveImage("docs/drawbot/specimen-001.gif")
print("Drawbot: Done :-)")
