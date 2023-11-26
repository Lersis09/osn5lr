from PIL import ImageDraw,Image
height = [49.466151,49.466663,49.467180,49.467700,49.468230,49.468746,49.469247,49.469760,49.470279,49.470799,49.471321,49.471846,49.472373,49.472898,49.473426,49.473949,49.474475,49.475007,49.475541,49.476079
]

latitude = [36.430233,36.430384,36.430526,36.430640,36.430751,36.430867,36.430998,36.431113,36.431234,36.431346,36.431445,36.431535,36.431627,36.431713,36.431791,36.431859,36.431920,36.431966,36.432010,36.432050
]

X =[]
Y =[]

for i in range(len(latitude)):
    X.append((((latitude[i]-36.3)*2306)/0.7))
for i in range(len(height)):
    Y.append((((50-height[i])*2555)/0.6))

image = Image.open("M-37-074.jpg")
draw = ImageDraw.Draw(image)
draw.line((X[0],Y[0], X[1],Y[1]), fill=250)
draw.line((X[1],Y[1], X[2],Y[2]), fill=250)
draw.line((X[2],Y[2], X[3],Y[3]), fill=250)
draw.line((X[3],Y[3], X[4],Y[4]), fill=250)
draw.line((X[4],Y[4], X[5],Y[5]), fill=250)
draw.line((X[5],Y[5], X[6],Y[6]), fill=250)
draw.line((X[6],Y[6], X[7],Y[7]), fill=250)
draw.line((X[7],Y[7], X[8],Y[8]), fill=250)
draw.line((X[8],Y[8], X[9],Y[9]), fill=250)
draw.line((X[9],Y[9], X[10],Y[10]), fill=250)
draw.line((X[10],Y[10], X[11],Y[11]), fill=250)
draw.line((X[11],Y[11], X[12],Y[12]), fill=250)
draw.line((X[12],Y[12], X[13],Y[13]), fill=250)
draw.line((X[13],Y[13], X[14],Y[14]), fill=250)
draw.line((X[14],Y[14], X[15],Y[15]), fill=250)
draw.line((X[15],Y[15], X[16],Y[16]), fill=250)
draw.line((X[16],Y[16], X[17],Y[17]), fill=250)
draw.line((X[17],Y[17], X[18],Y[18]), fill=250)
draw.line((X[18],Y[18], X[19],Y[9]), fill=250)
draw.text((X[0]-8, Y[0]-10),"A",(255,0,0))
draw.text((X[19]+3, Y[19]-5),"B",(255,0,0))


del draw
image.save("test.jpg","JPEG")
image.show()
