# Персонажи:
define i = Character('Игорь', color="#4B0082",what_prefix = "{b}{i}")
define n = Character('Настя', color="#00BFFF",what_prefix = "{b}{i}")
define a = Character('Артем', color="#C0C0C0",what_prefix = "{b}{i}")
define d = Character("Даниэла", color="#D8BFD8",what_prefix = "{b}{i}")
define a = Character('Ариадна', color="#00BFFF",what_prefix = "{b}{i}")
#Музыка и звуки 
define audio.beginning = "audio/beginning.ogg" #начало
define audio.heart = "audio/heart.mp3" #выбор



# Игра начинается здесь:
label start:

    play music beginning #начальная музыка

    scene bg black # черный экран

    "{cps=60}В этой игре ты сможешь почувствовать себя студентом, попавшим в временую петлю. {/cps}" 
    "{cps=60}На протяжении всей игры у вас будет право выбора, {w} от которого будет зависить дальнейший сюжет.{/cps}"
    "{cps=60}Так же персонажи в этой игре могут запоминать ваши действия, так что...{/cps}"
    stop music fadeout 1
    "{cps=60}Делайте выбор с умом.{/cps}"

    
    play music heart #музыка выбора
    menu:
        "{sc} {color=#FF0000}Начать игру?{/color}{/sc} " 
        "Да":
            jump choice_1
        "Нет":
            jump end_1

    return
    play music beginning
label choice_1: #Первый выбор
    "Молодец"
    i "Ку"
    return

label end_1:
    "Плохой выбор"
    return