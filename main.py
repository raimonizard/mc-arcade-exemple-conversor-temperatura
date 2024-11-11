@namespace
class SpriteKind:
    button = SpriteKind.create()
    Fondo = SpriteKind.create()
def temperature_calculator(is_centigrads: bool, graus: number):
    if is_centigrads:
        return graus * (9 / 5) + 32
    else:
        return (graus - 32) * (5 / 9)
def termometer(is_centigrads2: bool):
    global escala, medio, temperature
    if is_centigrads2:
        escala = 100
    else:
        escala = 212
    medio = scene.screen_width() / 2
    if mySprite.x != medio:
        temperature = (mySprite.x - medio) / (medio / escala)
    return temperature
def initial_position():
    global mySprite
    mySprite = sprites.create(assets.image("""
        player
    """), SpriteKind.player)
    mySprite.set_position(30, 100)
    mySprite.z = 100
    mySprite.set_bounce_on_wall(True)
    controller.move_sprite(mySprite)
def chose_init_of_measurement():
    global centigrados, fahrenheit
    scene.set_background_image(assets.image("""
        fondo_decicion_medida
    """))
    initial_position()
    centigrados = sprites.create(assets.image("""
        centigrados
    """), SpriteKind.button)
    centigrados.set_position(40, 35)
    fahrenheit = sprites.create(assets.image("""
        farenheins
    """), SpriteKind.button)
    fahrenheit.set_position(120, 35)

def on_on_overlap(sprite2, otherSprite2):
    global temperatura, otra_temperatura
    temperatura = redondear(termometer(centigrados_is_chosse))
    otra_temperatura = redondear(temperature_calculator(centigrados_is_chosse, temperatura))
    if otherSprite2 == fuego:
        mySprite.say_text("" + str(temperatura) + " Cº", 1000, False)
        respuesta.say_text("" + str(otra_temperatura) + " ºF", 1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.Fondo, on_on_overlap)

def temperature_converter(is_centigrads3: bool):
    global centigrados_is_chosse, fuego, respuesta
    game.show_long_text("Coloca a tu personaje sobre la temperatura que deseees cambiar",
        DialogLayout.BOTTOM)
    centigrados_is_chosse = is_centigrads3
    sprites.destroy(fahrenheit)
    sprites.destroy(centigrados)
    scene.set_background_color(15)
    fuego = sprites.create(assets.image("""
        fuego
    """), SpriteKind.Fondo)
    scene.set_background_image(fuego.image)
    respuesta = sprites.create(img("""
            . . f f f . . . . . . . . . . . 
                    f f f c c . . . . . . . . f f f 
                    f f c c . . c c . . . f c b b c 
                    f f c 3 c c 3 c c f f b b b c . 
                    f f b 3 b c 3 b c f b b c c c . 
                    . c b b b b b b c f b c b c c . 
                    . c b b b b b b c b b c b b c . 
                    c b 1 b b b 1 b b b c c c b c . 
                    c b b b b b b b b c c c c c . . 
                    f b c b b b c b b b b f c . . . 
                    f b 1 f f f 1 b b b b f c c . . 
                    . f b b b b b b b b c f . . . . 
                    . . f b b b b b b c f . . . . . 
                    . . . f f f f f f f . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    mySprite.z = 20
    respuesta.set_position(60, 100)
    animation.run_image_animation(respuesta,
        [img("""
                . . f f f . . . . . . . . f f f 
                        . f f c c . . . . . . f c b b c 
                        f f c c . . . . . . f c b b c . 
                        f c f c . . . . . . f b c c c . 
                        f f f c c . c c . f c b b c c . 
                        f f c 3 c c 3 c c f b c b b c . 
                        f f b 3 b c 3 b c f b c c b c . 
                        . c b b b b b b c b b c c c . . 
                        . c 1 b b b 1 b b c c c c . . . 
                        c b b b b b b b b b c c . . . . 
                        c b c b b b c b b b b f . . . . 
                        f b 1 f f f 1 b b b b f c . . . 
                        f b b b b b b b b b b f c c . . 
                        . f b b b b b b b b c f . . . . 
                        . . f b b b b b b c f . . . . . 
                        . . . f f f f f f f . . . . . .
            """),
            img("""
                . . f f f . . . . . . . . . . . 
                        f f f c c . . . . . . . . f f f 
                        f f c c . . c c . . . f c b b c 
                        f f c 3 c c 3 c c f f b b b c . 
                        f f b 3 b c 3 b c f b b c c c . 
                        . c b b b b b b c f b c b c c . 
                        . c b b b b b b c b b c b b c . 
                        c b 1 b b b 1 b b b c c c b c . 
                        c b b b b b b b b c c c c c . . 
                        f b c b b b c b b b b f c . . . 
                        f b 1 f f f 1 b b b b f c c . . 
                        . f b b b b b b b b c f . . . . 
                        . . f b b b b b b c f . . . . . 
                        . . . f f f f f f f . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . c c . . c c . . . . . . . . 
                        . . c 3 c c 3 c c c . . . . . . 
                        . c b 3 b c 3 b c c c . . . . . 
                        . c b b b b b b b b f f . . . . 
                        c c b b b b b b b b f f . . . . 
                        c b 1 b b b 1 b b c f f f . . . 
                        c b b b b b b b b f f f f . . . 
                        f b c b b b c b c c b b b . . . 
                        f b 1 f f f 1 b f c c c c . . . 
                        . f b b b b b b f b b c c . . . 
                        c c f b b b b b c c b b c . . . 
                        c c c f f f f f f c c b b c . . 
                        . c c c . . . . . . c c c c c . 
                        . . c c c . . . . . . . c c c c 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . f f f . . . . . . . . f f f . 
                        f f c . . . . . . . f c b b c . 
                        f c c . . . . . . f c b b c . . 
                        c f . . . . . . . f b c c c . . 
                        c f f . . . . . f f b b c c . . 
                        f f f c c . c c f b c b b c . . 
                        f f f c c c c c f b c c b c . . 
                        . f c 3 c c 3 b c b c c c . . . 
                        . c b 3 b c 3 b b c c c c . . . 
                        c c b b b b b b b b c c . . . . 
                        c b 1 b b b 1 b b b b f c . . . 
                        f b b b b b b b b b b f c c . . 
                        f b c b b b c b b b b f . . . . 
                        . f 1 f f f 1 b b b c f . . . . 
                        . . f b b b b b b c f . . . . . 
                        . . . f f f f f f f . . . . . .
            """)],
        200,
        True)
def redondear(núm: number):
    return Math.round(núm * 100) / 100

def on_on_overlap2(sprite, otherSprite):
    if controller.A.is_pressed():
        if otherSprite == centigrados:
            temperature_converter(True)
        elif otherSprite == fahrenheit:
            temperature_converter(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.button, on_on_overlap2)

respuesta: Sprite = None
fuego: Sprite = None
otra_temperatura = 0
centigrados_is_chosse = False
temperatura = 0
fahrenheit: Sprite = None
centigrados: Sprite = None
temperature = 0
mySprite: Sprite = None
medio = 0
escala = 0
temperatura3: List[number] = []
temperature2 = 0
temperatura2 = 0
game.show_long_text("Selecciona la unidad de medida para la Tempetatura.",
    DialogLayout.CENTER)
chose_init_of_measurement()