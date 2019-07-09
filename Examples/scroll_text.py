import NeoMat_Text
pin = "A5"
width = 8
height = 8
color = [50,50,0 ]

mat = NeoMat_Text.Matrix(pin, width, height, color)

mat.scroll("Banana")
