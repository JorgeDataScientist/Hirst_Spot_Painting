import colorgram


# TODO 1: Extract 6 colors from an image.
colors = colorgram.extract('img_1.png', 10)
print(colors)
print('------------------------------------')

# TODO 2: Extraer solo colores RGB
RGB_Colors = []
for color in colors:
  RGB_Colors.append(color.rgb)
print(RGB_Colors)
print('------------------------------------')

# TODO 3: Crear lista con colores RGB
RGB_Colors_2 = []
for colores in colors:
  R = colores.rgb.r
  G = colores.rgb.g
  B = colores.rgb.g
  New_RGB = (R, G, B)
  RGB_Colors_2.append(New_RGB)
print(RGB_Colors_2)
