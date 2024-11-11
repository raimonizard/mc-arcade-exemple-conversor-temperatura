namespace SpriteKind {
    export const button = SpriteKind.create()
    export const Fondo = SpriteKind.create()
}
function temperature_calculator (is_centigrads: boolean, graus: number) {
    if (is_centigrads) {
        return graus * (9 / 5) + 32
    } else {
        return (graus - 32) * (5 / 9)
    }
}
function termometer (is_centigrads2: boolean) {
    if (is_centigrads2) {
        escala = 80
    } else {
        escala = 176
    }
    medio = scene.screenWidth() / 2
    if (mySprite.x != medio) {
        temperature = (mySprite.x - medio) / (medio / escala)
    }
    return temperature
}
function initial_position () {
    mySprite = sprites.create(assets.image`player`, SpriteKind.Player)
    mySprite.setPosition(30, 100)
    mySprite.z = 100
    mySprite.setBounceOnWall(true)
    controller.moveSprite(mySprite)
}
function chose_init_of_measurement () {
    scene.setBackgroundImage(assets.image`fondo_decicion_medida`)
    initial_position()
    centigrados = sprites.create(assets.image`centigrados`, SpriteKind.button)
    centigrados.setPosition(40, 35)
    fahrenheit = sprites.create(assets.image`farenheins`, SpriteKind.button)
    fahrenheit.setPosition(120, 35)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Fondo, function (sprite2, otherSprite2) {
    temperatura = redondear(termometer(centigrados_is_chosse))
    otra_temperatura = redondear(temperature_calculator(centigrados_is_chosse, temperatura))
    if (otherSprite2 == fuego) {
        mySprite.sayText("" + temperatura + " Cº", 1000, false)
        respuesta.sayText("" + otra_temperatura + " ºF", 1000)
    }
})
function temperature_converter (is_centigrads3: boolean) {
    game.showLongText("Coloca a tu personaje sobre la temperatura que deseees cambiar", DialogLayout.Bottom)
    centigrados_is_chosse = is_centigrads3
    sprites.destroy(fahrenheit)
    sprites.destroy(centigrados)
    scene.setBackgroundColor(15)
    fuego = sprites.create(assets.image`fuego`, SpriteKind.Fondo)
    scene.setBackgroundImage(fuego.image)
    respuesta = sprites.create(img`
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
        `, SpriteKind.Player)
    mySprite.z = 20
    respuesta.setPosition(60, 100)
    animation.runImageAnimation(
    respuesta,
    [img`
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
        `,img`
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
        `,img`
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
        `,img`
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
        `],
    200,
    true
    )
}
function redondear (núm: number) {
    return Math.round(núm * 100) / 100
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.button, function (sprite, otherSprite) {
    if (controller.A.isPressed()) {
        if (otherSprite == centigrados) {
            temperature_converter(true)
        } else if (otherSprite == fahrenheit) {
            temperature_converter(false)
        }
    }
})
let respuesta: Sprite = null
let fuego: Sprite = null
let otra_temperatura = 0
let centigrados_is_chosse = false
let temperatura = 0
let fahrenheit: Sprite = null
let centigrados: Sprite = null
let temperature = 0
let mySprite: Sprite = null
let medio = 0
let escala = 0
let temperatura3: number[] = []
let temperature2 = 0
let temperatura2 = 0
game.showLongText("Selecciona la unidad de medida para la Tempetatura.", DialogLayout.Center)
chose_init_of_measurement()
