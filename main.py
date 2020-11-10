##Cristopher Jose Rodolfo Barrios Solis
##18207

from rayT.math import V3
from rayT.utils import Color
from rayT.ray import RT
from rayT.envmap import Envmap
from rayT.Texture import Material, Light, AmbientLight, Texture
from rayT.geometry import Sphere, Plane, Cube, Cylinder, Pyramid

# colorsitos
light = Color(80, 80, 120)
sky = Color(77,166,255)
GREY = Color(54, 69, 79)

# texturas
awita = Material(diffuse=light, albedo=(0, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)
piedra = Material(texture=Texture('./new/sunset.bmp'))
madera = Material(texture=Texture('./new/madera.bmp'))
cremita = Material(texture=Texture('./new/Sep.bmp'))
cesped = Material(texture=Texture('./new/cesped.bmp'))

# Darle play al reloj
import time
start_time = time.time()

# Render
rndr = RT(768, 432)
rndr.envmap = Envmap('./new/cielito.bmp')
rndr.light = Light(position=V3(0, 2, 0.2), intensity=1.5)
rndr.ambient_light = AmbientLight(strength = 0.1)
rndr.background_color = sky

rndr.scene = [
#arbol
    # Pyramid([V3(11.5, 0.5, -11), V3(14.5, 0.5, -11),  V3(11.8, 0.8, -11.5), V3(12, 3.4, -11.5), ], cesped),
    # Cylinder(14.15, 1.8, V3(12, 1, -10), madera),

    #laguito con awa de uwu
    Plane( V3(0, 0, -10), V3(0,1, 0.05), awita),

    # ceped verde
    Cube(V3(-11, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-10.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-10, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-9.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-9, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-8.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-8, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-7.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-7, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-6.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-6, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-5.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-4.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-4, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-3.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-3, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-2.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-2, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-1.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-1, 0.25, -9.25), 0.5, cesped),
    Cube(V3(-0.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(0, 0.25, -9.25), 0.5, cesped),
    Cube(V3(0.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(1, 0.25, -9.25), 0.5, cesped),
    Cube(V3(1.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(2, 0.25, -9.25), 0.5, cesped),
    Cube(V3(2.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(3, 0.25, -9.25), 0.5, cesped),
    Cube(V3(3.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(4, 0.25, -9.25), 0.5, cesped),
    Cube(V3(4.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(5.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(6, 0.25, -9.25), 0.5, cesped),
    Cube(V3(6.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(7, 0.25, -9.25), 0.5, cesped),
    Cube(V3(7.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(8, 0.25, -9.25), 0.5, cesped),
    Cube(V3(8.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(9, 0.25, -9.25), 0.5, cesped),
    Cube(V3(9.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(10, 0.25, -9.25), 0.5, cesped),
    Cube(V3(10.5, 0.25, -9.25), 0.5, cesped),
    Cube(V3(11, 0.25, -9.25), 0.5, cesped),
    Cube(V3(11.5, 0.25, -9.25), 0.5, cesped),

    Cube(V3(-11, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-10.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-10, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-9.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-9, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-8.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-8, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-7.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-7, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-6.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-6, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-5.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-4.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-4, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-3.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-3, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-2.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-2, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-1.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-1, 0.50, -9.25), 0.5, cesped),
    Cube(V3(-0.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(0, 0.50, -9.25), 0.5, cesped),
    Cube(V3(0.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(1, 0.50, -9.25), 0.5, cesped),
    Cube(V3(1.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(2, 0.50, -9.25), 0.5, cesped),
    Cube(V3(2.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(3, 0.50, -9.25), 0.5, cesped),
    Cube(V3(3.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(4, 0.50, -9.25), 0.5, cesped),
    Cube(V3(4.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(5.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(6, 0.50, -9.25), 0.5, cesped),
    Cube(V3(6.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(7, 0.50, -9.25), 0.5, cesped),
    Cube(V3(7.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(8, 0.50, -9.25), 0.5, cesped),
    Cube(V3(8.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(9, 0.50, -9.25), 0.5, cesped),
    Cube(V3(9.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(10, 0.50, -9.25), 0.5, cesped),
    Cube(V3(10.5, 0.50, -9.25), 0.5, cesped),
    Cube(V3(11, 0.50, -9.25), 0.5, cesped),
    Cube(V3(11.5, 0.50, -9.25), 0.5, cesped),


    Cube(V3(-11, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-10.5, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-10, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-9.5, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-9, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-8.5, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-8, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-7.5, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-7, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-6.5, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-6, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-5.5, -0.25, -9.25), 0.5, cesped),
    Cube(V3(-5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(-4.5,- 0.25, -9.25), 0.5, cesped),

    Cube(V3(-1,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(-0.5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(0,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(0.5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(1,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(1.5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(2,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(2.5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(3,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(3.5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(4,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(4.5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(5.5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(6,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(6.5, - 0.25, -9.25), 0.5, cesped),
    Cube(V3(7, - 0.25, -9.25), 0.5, cesped),
    Cube(V3(7.5,- 0.25, -9.25), 0.5, cesped),
    Cube(V3(8, - 0.25, -9.25), 0.5, cesped),
    Cube(V3(8.5, - 0.25, -9.25), 0.5, cesped),
    Cube(V3(9, - 0.25, -9.25), 0.5, cesped),
    Cube(V3(9.5, - 0.25, -9.25), 0.5, cesped),
    Cube(V3(10, - 0.25, -9.25), 0.5, cesped),
    Cube(V3(10.5, - 0.25, -9.25), 0.5, cesped),
    Cube(V3(11, - 0.25, -9.25), 0.5, cesped),
    Cube(V3(11.5, - 0.25, -9.25), 0.5, cesped),


    Cube(V3(-11, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-10.5, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-10, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-9.5, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-9, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-8.5, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-8, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-7.5, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-7, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-6.5, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-6, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-5.5, -0.50, -9.25), 0.5, cesped),
    Cube(V3(-5,- 0.50, -9.25), 0.5, cesped),
    Cube(V3(-4.5,- 0.50, -9.25), 0.5, cesped),

    Cube(V3(-11, -0.75, -9.25), 0.5, cesped),
    Cube(V3(-10.5, -0.75, -9.25), 0.5, cesped),
    Cube(V3(-10, -0.75, -9.25), 0.5, cesped),
    Cube(V3(-9.5, -0.75, -9.25), 0.5, cesped),
    Cube(V3(-9, -0.75, -9.25), 0.5, cesped),
    Cube(V3(-8.5, -0.75, -9.25), 0.5, cesped),
    Cube(V3(-8, -0.75, -9.25), 0.5, cesped),
    Cube(V3(-7.5, -0.75, -9.25), 0.5, cesped),


## casita11111111111111

########Columna
    Cube(V3(-5, 0.75, -9.25), 0.5, madera),
    Cube(V3(-5, 1.25, -9.25), 0.5, madera),
    Cube(V3(-5, 1.75, -9.25), 0.5, madera),
    Cube(V3(-5, 2.25, -9.25), 0.5, madera),
    Cube(V3(-5, 2.75, -9.25), 0.5, madera),



#########Segundopiso
    Cube(V3(-5.50, 2.75, -9.25), 0.5, madera),
    Cube(V3(-6.00, 2.75, -9.25), 0.5, madera),
    Cube(V3(-6.50, 2.75, -9.25), 0.5, madera),
    Cube(V3(-7.00, 2.75, -9.25), 0.5, madera),

    Cube(V3(-4.50, 2.75, -9.25), 0.5, madera),
    Cube(V3(-4.00, 2.75, -9.25), 0.5, madera),
    Cube(V3(-3.50, 2.75, -9.25), 0.5, madera),
    Cube(V3(-3.00, 2.75, -9.25), 0.5, madera),
    Cube(V3(-2.50, 2.75, -9.25), 0.5, madera),
    Cube(V3(-2.00, 2.75, -9.25), 0.5, madera),


#########Columna
    Cube(V3(-1.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(-1.50, 1.25, -9.25), 0.5, madera),
    Cube(V3(-1.50, 1.75, -9.25), 0.5, madera),
    Cube(V3(-1.50, 2.25, -9.25), 0.5, madera),
    Cube(V3(-1.50, 2.75, -9.25), 0.5, madera),


    Cube(V3(-4.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(-4.00, 0.75, -9.25), 0.5, madera),
    Cube(V3(-3.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(-3.00, 0.75, -9.25), 0.5, madera),
    Cube(V3(-2.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(-2.00, 0.75, -9.25), 0.5, madera),

    Cube(V3(-5.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(-6.00, 0.75, -9.25), 0.5, madera),
    Cube(V3(-6.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(-7.00, 0.75, -9.25), 0.5, madera),

#########Columna
    Cube(V3(-7.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(-7.50, 1.25, -9.25), 0.5, madera),
    Cube(V3(-7.50, 1.75, -9.25), 0.5, madera),
    Cube(V3(-7.50, 2.25, -9.25), 0.5, madera),
    Cube(V3(-7.50, 2.75, -9.25), 0.5, madera),

#########triangule
##izquierda
    Cube(V3(-5, 3.25, -9.25), 0.5, madera),
    Cube(V3(-4.50, 3.75, -9.25), 0.5, madera),
    Cube(V3(-4.00, 4.25, -9.25), 0.5, madera),
    Cube(V3(-3.50, 4.75, -9.25), 0.5, madera),

    Cube(V3(-1.50, 3.25, -9.25), 0.5, madera),
    Cube(V3(-2.00, 3.75, -9.25), 0.5, madera),
    Cube(V3(-2.50, 4.25, -9.25), 0.5, madera),
    Cube(V3(-3.00, 4.75, -9.25), 0.5, madera),

######techo de piedra
    ##izquierda
    Cube(V3(-4.00, 4.75, -9.25), 0.5, piedra),
        Cube(V3(-4.50, 4.75, -9.25), 0.5, piedra),
        Cube(V3(-5.00, 4.75, -9.25), 0.5, piedra),
        Cube(V3(-5.50, 4.75, -9.25), 0.5, piedra),
        Cube(V3(-6.00, 4.75, -9.25), 0.5, piedra),
        Cube(V3(-6.50, 4.75, -9.25), 0.5, piedra),
        Cube(V3(-7.00, 4.75, -9.25), 0.5, piedra),
        Cube(V3(-7.50, 4.75, -9.25), 0.5, piedra),
    Cube(V3(-4.50, 4.25, -9.25), 0.5, piedra),
        Cube(V3(-5.00, 4.25, -9.25), 0.5, piedra),
        Cube(V3(-5.50, 4.25, -9.25), 0.5, piedra),
        Cube(V3(-6.00, 4.25, -9.25), 0.5, piedra),
        Cube(V3(-6.50, 4.25, -9.25), 0.5, piedra),
        Cube(V3(-7.00, 4.25, -9.25), 0.5, piedra),
        Cube(V3(-7.50, 4.25, -9.25), 0.5, piedra),
    Cube(V3(-5.00, 3.75, -9.25), 0.5, piedra),
        Cube(V3(-5.50, 3.75, -9.25), 0.5, piedra),
        Cube(V3(-6.00, 3.75, -9.25), 0.5, piedra),
        Cube(V3(-6.50, 3.75, -9.25), 0.5, piedra),
        Cube(V3(-7.00, 3.75, -9.25), 0.5, piedra),
        Cube(V3(-7.50, 3.75, -9.25), 0.5, piedra),
    Cube(V3(-5.50, 3.25, -9.25), 0.5, piedra),
        Cube(V3(-6.00, 3.25, -9.25), 0.5, piedra),
        Cube(V3(-6.50, 3.25, -9.25), 0.5, piedra),
        Cube(V3(-7.00, 3.25, -9.25), 0.5, piedra),
        Cube(V3(-7.50, 3.25, -9.25), 0.5, piedra),

    ##derecha
    Cube(V3(-2.50, 4.75, -9.25), 0.5, piedra),
    Cube(V3(-2.00, 4.25, -9.25), 0.5, piedra),
    Cube(V3(-1.50, 3.75, -9.25), 0.5, piedra),
    Cube(V3(-1.00, 3.25, -9.25), 0.5, piedra),

    ##rellenito
    Cube(V3(-3.50, 4.25, -9.25), 0.5, cremita),
    Cube(V3(-3.00, 4.25, -9.25), 0.5, cremita),

    Cube(V3(-4.00, 3.75, -9.25), 0.5, cremita),
    Cube(V3(-3.50, 3.75, -9.25), 0.5, cremita),
    Cube(V3(-3.00, 3.75, -9.25), 0.5, cremita),
    Cube(V3(-2.50, 3.75, -9.25), 0.5, cremita),

    Cube(V3(-4.50, 3.25, -9.25), 0.5, cremita),
    Cube(V3(-4.00, 3.25, -9.25), 0.5, cremita),
    Cube(V3(-3.50, 3.25, -9.25), 0.5, cremita),
    Cube(V3(-3.00, 3.25, -9.25), 0.5, cremita),
    Cube(V3(-2.50, 3.25, -9.25), 0.5, cremita),
    Cube(V3(-2.00, 3.25, -9.25), 0.5, cremita),

    ##cuadro de abajo
    Cube(V3(-4.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(-4.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(-3.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(-3.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(-2.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(-2.00, 2.25, -9.25), 0.5, cremita),

    Cube(V3(-4.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(-4.00, 1.75, -9.25), 0.5, cremita),
    Cube(V3(-3.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(-3.00, 1.75, -9.25), 0.5, cremita),
    Cube(V3(-2.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(-2.00, 1.75, -9.25), 0.5, cremita),

    Cube(V3(-4.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(-4.00, 1.25, -9.25), 0.5, cremita),
    Cube(V3(-3.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(-3.00, 1.25, -9.25), 0.5, cremita),
    Cube(V3(-2.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(-2.00, 1.25, -9.25), 0.5, cremita),

    ## el otro cuadrito de abajo
    Cube(V3(-5.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(-6.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(-6.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(-7.00, 2.25, -9.25), 0.5, cremita),

    Cube(V3(-5.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(-6.00, 1.75, -9.25), 0.5, cremita),
    Cube(V3(-6.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(-7.00, 1.75, -9.25), 0.5, cremita),

    Cube(V3(-5.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(-6.00, 1.25, -9.25), 0.5, cremita),
    Cube(V3(-6.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(-7.00, 1.25, -9.25), 0.5, cremita),

## casita22222222222222
###########columna111
    Cube(V3(6, 0.75, -9.25), 0.5, madera),
    Cube(V3(6, 1.25, -9.25), 0.5, madera),
    Cube(V3(6, 1.75, -9.25), 0.5, madera),
    Cube(V3(6, 2.25, -9.25), 0.5, madera),
    Cube(V3(6, 2.75, -9.25), 0.5, madera),
        Cube(V3(6, 3.25, -9.25), 0.5, madera),
        Cube(V3(6, 3.75, -9.25), 0.5, madera),

    Cube(V3(5.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(5.50, 1.25, -9.25), 0.5, madera),
    Cube(V3(5.50, 1.75, -9.25), 0.5, madera),
    Cube(V3(5.50, 2.25, -9.25), 0.5, madera),
        Cube(V3(5.50, 2.75, -9.25), 0.5, madera),
        Cube(V3(5.50, 2.75, -9.25), 0.5, madera),

##########techito
    Cube(V3(6, 4.25, -9.25), 0.5, madera),
    Cube(V3(5.50, 4.75, -9.25), 0.5, madera),
    Cube(V3(5.00, 5.25, -9.25), 0.5, madera),

    Cube(V3(2.50, 4.25, -9.25), 0.5, madera),
    Cube(V3(3.00, 4.75, -9.25), 0.5, madera),
    Cube(V3(3.50, 5.25, -9.25), 0.5, madera),



    #####viga
    Cube(V3(5.00, 2.75, -9.25), 0.5, madera),
    Cube(V3(4.50, 2.75, -9.25), 0.5, madera),
    Cube(V3(4.00, 2.75, -9.25), 0.5, madera),
    Cube(V3(3.50, 2.75, -9.25), 0.5, madera),
    Cube(V3(3.00, 2.75, -9.25), 0.5, madera),
    Cube(V3(2.50, 2.75, -9.25), 0.5, madera),

    Cube(V3(5.50, 3.75, -9.25), 0.5, madera),
    Cube(V3(5.00, 3.75, -9.25), 0.5, madera),
    Cube(V3(4.50, 3.75, -9.25), 0.5, madera),
    Cube(V3(4.00, 3.75, -9.25), 0.5, madera),
    Cube(V3(3.50, 3.75, -9.25), 0.5, madera),
    Cube(V3(3.00, 3.75, -9.25), 0.5, madera),
    Cube(V3(2.50, 3.75, -9.25), 0.5, madera),

    Cube(V3(2.50, 3.25, -9.25), 0.5, madera),


##########rellenos del techo y partecita de abajo
    Cube(V3(3.00, 4.25, -9.25), 0.5, cremita),
    Cube(V3(3.50, 4.25, -9.25), 0.5, cremita),
    Cube(V3(4.00, 4.25, -9.25), 0.5, cremita),
    Cube(V3(4.50, 4.25, -9.25), 0.5, cremita),
    Cube(V3(5.00, 4.25, -9.25), 0.5, cremita),
    Cube(V3(5.50, 4.25, -9.25), 0.5, cremita),

    Cube(V3(3.50, 4.75, -9.25), 0.5, cremita),
    Cube(V3(4.00, 4.75, -9.25), 0.5, cremita),
    Cube(V3(4.50, 4.75, -9.25), 0.5, cremita),
    Cube(V3(5.00, 4.75, -9.25), 0.5, cremita),

    Cube(V3(3.00, 3.25, -9.25), 0.5, cremita),
    Cube(V3(3.50, 3.25, -9.25), 0.5, cremita),
    Cube(V3(4.00, 3.25, -9.25), 0.5, cremita),
    Cube(V3(4.50, 3.25, -9.25), 0.5, cremita),
    Cube(V3(5.00, 3.25, -9.25), 0.5, cremita),
    Cube(V3(5.50, 3.25, -9.25), 0.5, cremita),

##########parte del techo
    Cube(V3(6, 4.75, -9.25), 0.5, piedra),

    ###parte del la resbaladera
    Cube(V3(6.50, 4.25, -9.25), 0.5, piedra),
    Cube(V3(7.00, 4.25, -9.25), 0.5, piedra),
    Cube(V3(7.50, 4.25, -9.25), 0.5, piedra),
    Cube(V3(8.00, 4.25, -9.25), 0.5, piedra),

    Cube(V3(2.50, 4.75, -9.25), 0.5, piedra),
    Cube(V3(2.00, 4.25, -9.25), 0.5, piedra),

    Cube(V3(7.50, 3.75, -9.25), 0.5, madera),
    Cube(V3(7.50, 3.25, -9.25), 0.5, madera),
    Cube(V3(7.50, 2.75, -9.25), 0.5, madera),
    Cube(V3(7.50, 2.25, -9.25), 0.5, madera),
    Cube(V3(7.50, 1.75, -9.25), 0.5, madera),
    Cube(V3(7.50, 1.25, -9.25), 0.5, madera),
    Cube(V3(7.50, 0.75, -9.25), 0.5, madera),

    #######lateral
    Cube(V3(6.50, 3.75, -9.25), 0.5, cremita),
    Cube(V3(6.50, 3.25, -9.25), 0.5, cremita),
    Cube(V3(6.50, 2.75, -9.25), 0.5, cremita),
    Cube(V3(6.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(6.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(6.50, 1.25, -9.25), 0.5, cremita),


    Cube(V3(7.00, 3.75, -9.25), 0.5, cremita),
    Cube(V3(7.00, 3.25, -9.25), 0.5, cremita),
    Cube(V3(7.00, 2.75, -9.25), 0.5, cremita),
    Cube(V3(7.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(7.00, 1.75, -9.25), 0.5, cremita),
    Cube(V3(7.00, 1.25, -9.25), 0.5, cremita),



##El techo de la izquierda
    Cube(V3(3.00, 3.25, -9.25), 0.5, piedra),



    #####segundotechito
    ##punta
    Cube(V3(2.50, 2.25, -9.25), 0.5, piedra),
    ##izquierda
    Cube(V3(2.00, 1.75, -9.25), 0.5, piedra),
    Cube(V3(1.50, 1.25, -9.25), 0.5, piedra),

    Cube(V3(1.50, 0.75, -9.25), 0.5, madera),


    ##derecha
    Cube(V3(3.00, 1.75, -9.25), 0.5, piedra),
    Cube(V3(3.50, 1.25, -9.25), 0.5, piedra),

    Cube(V3(3.50, 0.75, -9.25), 0.5, madera),

########relleno de la casota
    Cube(V3(3.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(3.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(4.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(4.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(5.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(5.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(6.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(6.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(7.00, 2.25, -9.25), 0.5, cremita),

    Cube(V3(3.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(4.00, 1.75, -9.25), 0.5, cremita),
    Cube(V3(4.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(5.00, 1.75, -9.25), 0.5, cremita),
    Cube(V3(5.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(6.00, 1.75, -9.25), 0.5, cremita),
    Cube(V3(6.50, 1.75, -9.25), 0.5, cremita),
    Cube(V3(7.00, 1.75, -9.25), 0.5, cremita),

    Cube(V3(4.00, 1.25, -9.25), 0.5, cremita),
    Cube(V3(4.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(5.00, 1.25, -9.25), 0.5, cremita),
    Cube(V3(5.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(6.00, 1.25, -9.25), 0.5, cremita),
    Cube(V3(6.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(7.00, 1.25, -9.25), 0.5, cremita),

    Cube(V3(4.00, 0.75, -9.25), 0.5, madera),
    Cube(V3(4.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(5.00, 0.75, -9.25), 0.5, madera),
    Cube(V3(5.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(6.00, 0.75, -9.25), 0.5, madera),
    Cube(V3(6.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(7.00, 0.75, -9.25), 0.5, madera),

    Cube(V3(6.50, 0.75, -6.25), 0.5, madera),
    Cube(V3(7.00, 0.75, -6.25), 0.5, madera),

########casitacasita
    Cube(V3(2.00, 0.75, -9.25), 0.5, cremita),
    Cube(V3(2.50, 0.75, -9.25), 0.5, cremita),
    Cube(V3(3.00, 0.75, -9.25), 0.5, cremita),

    Cube(V3(2.00, 1.25, -9.25), 0.5, cremita),
    Cube(V3(2.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(3.00, 1.25, -9.25), 0.5, cremita),

    Cube(V3(2.50, 1.75, -9.25), 0.5, cremita),


##########relleno de techo izquierda
    Cube(V3(2.00, 3.75, -9.25), 0.5, piedra),
    Cube(V3(1.50, 3.75, -9.25), 0.5, piedra),
    Cube(V3(1.00, 3.75, -9.25), 0.5, piedra),
    Cube(V3(0.50, 3.75, -9.25), 0.5, piedra),
    Cube(V3(0.00, 3.75, -9.25), 0.5, piedra),

    #arriba
    Cube(V3(1.50, 4.25, -9.25), 0.5, piedra),
    Cube(V3(1.00, 4.25, -9.25), 0.5, piedra),
    Cube(V3(0.50, 4.25, -9.25), 0.5, piedra),
    Cube(V3(0.00, 4.25, -9.25), 0.5, piedra),

    Cube(V3(0.00, 3.75, -9.25), 0.5, madera),
    Cube(V3(0.00, 3.25, -9.25), 0.5, madera),
    Cube(V3(0.00, 2.75, -9.25), 0.5, madera),
    Cube(V3(0.00, 2.25, -9.25), 0.5, madera),
    Cube(V3(0.00, 1.75, -9.25), 0.5, madera),
    Cube(V3(0.00, 1.25, -9.25), 0.5, madera),
    Cube(V3(0.00, 0.75, -9.25), 0.5, madera),

    Cube(V3(2.00, 3.25, -9.25), 0.5, cremita),
    Cube(V3(1.50, 3.25, -9.25), 0.5, cremita),
    Cube(V3(1.00, 3.25, -9.25), 0.5, cremita),
    Cube(V3(0.50, 3.25, -9.25), 0.5, cremita),
    Cube(V3(0.00, 3.25, -9.25), 0.5, cremita),

    Cube(V3(2.00, 2.75, -9.25), 0.5, cremita),
    Cube(V3(1.50, 2.75, -9.25), 0.5, cremita),
    Cube(V3(1.00, 2.75, -9.25), 0.5, cremita),
    Cube(V3(0.50, 2.75, -9.25), 0.5, cremita),
    Cube(V3(0.00, 2.75, -9.25), 0.5, cremita),

    Cube(V3(2.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(1.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(1.00, 2.25, -9.25), 0.5, cremita),
    Cube(V3(0.50, 2.25, -9.25), 0.5, cremita),
    Cube(V3(0.00, 2.25, -9.25), 0.5, cremita),

    Cube(V3(1.50, 1.75, -9.25), 0.5, madera),
    Cube(V3(1.00, 1.75, -9.25), 0.5, madera),
    Cube(V3(0.50, 1.75, -9.25), 0.5, madera),
    Cube(V3(0.00, 1.75, -9.25), 0.5, madera),

    Cube(V3(1.00, 1.25, -9.25), 0.5, cremita),
    Cube(V3(0.50, 1.25, -9.25), 0.5, cremita),
    Cube(V3(0.00, 1.25, -9.25), 0.5, cremita),

    Cube(V3(1.00, 0.75, -9.25), 0.5, madera),
    Cube(V3(0.50, 0.75, -9.25), 0.5, madera),
    Cube(V3(0.00, 0.75, -9.25), 0.5, madera),

### awa de uwu
    Plane( V3(0, 0, -10), V3(0,1, 0.05), awita),

]

rndr.finish()
print("--- Se termino en %s segundotes ---" % (time.time() - start_time))
