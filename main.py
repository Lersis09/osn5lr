from PIL import ImageDraw,Image
height = [36.392794,36.393103,36.393430,36.393773,36.394137,36.394516,36.394908,36.395314,36.395736,36.396176,36.396634,36.397097,36.397569,36.398055,36.398552,36.399059,36.399580,36.400112
]

latitude =[49.457604,49.457265,49.456932,49.456607,49.456291,49.455983,49.455685,49.455395,49.455115,49.454843,49.454579,49.454323,49.454077,49.453840,49.453616,49.453402,49.453200,49.453005
]

X =[]
Y =[]

for i in range(len(latitude)):
    X.append((((latitude[i]-49.3)*2940)/0.7))
for i in range(len(height)):
    Y.append((((37-height[i])*2160)/0.6))

image = Image.open("M-37-74.jpg")
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
draw.text((X[0]-8, Y[0]-10),"A",(255,0,0))
draw.text((X[17]+3, Y[17]-5),"B",(255,0,0))


del draw
image.save("test.jpg","JPEG")
image.show()
