define banan = False
# Персонажи:
define i = Character('Игорь', color="#4B0082",what_prefix = "{i}")
define n = Character('Настя', color="#00BFFF",what_prefix = "{i}")
define a = Character('Артем', color="#C0C0C0",what_prefix = "{i}")
define d = Character("Даниэла", color="#D8BFD8",what_prefix = "{i}")
define a = Character('Ариадна', color="#00BFFF",what_prefix = "{i}")
#Музыка и звуки 
define audio.beginning = "audio/beginning.ogg" #начало
define audio.heart = "audio/heart.mp3" #выбор
define audio.morning = "audio/morning.ogg"#утреняя музыка
define audio.booom = "audio/booom.mp3" #взрыв 2 концовка
define audio.clock = "audio/clock.mp3" #будильник
define audio.end1 = "audio/end1.mp3" #1 концовка
define audio.banana = "audio/banana.mp3" # 3 Концовка

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
    

label end_1: #1 концовка

    stop music 
    "{cps=60}Вы решили не начинать игру.{/cps}"
    "{cps=60}Попробуйте другой выбор в следующий раз.{/cps}"
    window hide
    play sound end1
    scene poster1 with fade
    $ renpy.notify("Вы вышли на плохую концовку.") #уведомление в игре
    pause
    "Концовка : Плохой выбор"
    
   
    return


label choice_1: #Первый выбор
    play music clock
    "..."
    stop music fadeout 1
    play music morning #музыка
    "{cps=60} Игорь пытается проснуться, {w} потихоньку открывая глаза. {/cps}"
    scene bed with fade
    "{cps=60}Голова начинает гудеть, а тело болеть,{w} сегодня утро точно не доброе... {/cps}"
    "{cps=60}Может стоит отоспаться и не идти на пары? {/cps}"
    menu:
        "Спать дальше":
             jump end_2
        "Проснуться":
             jump choice_2

    return
    stop music
label end_2: #концовка 2
    scene black with fade
    "{cps=60} Игорь погрузился в сон,{w} видя сладкие сны о пышных булочках с корицей.{/cps} "
    stop music
    play sound  booom
    "{cps=60}Но внезапно,{w} мир взорвался не хуже, чем упаковка петард на китайском рынке. {/cps}"
    "{cps=60}Ослепительный белый свет, оглушительный рёв – и… ничего.{w} Абсолютно ничего.{/cps}"
    "{cps=60}Потому что Игорь, вместе с его кроватью, матрасом, да и большей частью общаги, {w} превратился в мельчайшую космическую пыль.{/cps}"
    "{cps=60}Попробуйте ещё раз{/cps}!" 
    "{cps=60} Возможно, в следующий раз булочки и поход на пару проф.деятельности спасут мир.{/cps}"

    window hide 
    play sound  booom
    scene boom with fade
    $ renpy.notify("Вы вышли на плохую концовку") #уведомление в игре
    pause
    "Концовка : Взрывной сон."
    return

label choice_2:
    i "{cps=60}(зевает) Я так плохо спал… Сколько сейчас времени? {w} (смотрит на телефон) 07:50… ЧЁРТ! {w} Я же снова опаздываю на проф.деятельность!{/cps}"
    i "{cps=60}Нужно быстро собираться.{w} Первым делом — умоюсь. {w} Надо ещё не забыть разбудить Даниэлу...{/cps}"
    i "{cps=60}Ну вот, теперь можно и к Даниэле.{/cps}"
    scene black with fade
    "{cps=60}Игорь одевается. На нем хайповые вещи от Vitmo и Balenciaga{/cps}"
    scene bed with fade
    i "{cps=60}Ну вот, теперь можно и к Даниэле.{/cps}"
    scene koridor with fade
    i "{cps=60}ашалеть,{w} кто оставил тут банан{/cps}?"
    menu:
        "Выбросить банан":
             jump choice_3
        "Пройти мимо":
             jump choice_3
             $ banan = True
    return
label end_3:#3 концовка
    scene black with fade 
    play sound banana
    "{cps=60}Один неосторожный шаг и{w} Игорь споткнулся о кожуру банана, валявшуюся посреди коридора.{/cps} "
    "{cps=60}Мир вокруг резко перевернулся. {/cps}"
    "{cps=60}Острая боль пронзила голову, когда его затылок с силой ударился о твердый пол.{/cps}"
    "{cps=60}Звезды вспыхнули перед глазами, гул заполнил уши, затем {w} — мрак..{/cps}"
    "{cps=60}Жизнь Игоря оборвалась так же внезапно, как и началась.{/cps}"
    window hide
    scene bananana with fade
    $ renpy.notify("Вы вышли на плохую концовку") #уведомление игры
    pause
    "Концовка: Нелепая смерть"
    return 
label choice_3: #3 выбор
     scene black with fade
    if banan == False:
        $ renpy.notify("Игорь выбросил банан") #уведомление в игре
    else:
        $ renpy.notify("Игорь не выбросил банан") #уведомление в игре

    scene danilka with fade 
    with vpunch
    "{cps=60}Тук-Тук-Тук...{/cps}"
    i "{cps=60}Даниэла, просыпайся! Мы опаздываем на пару!!!{/cps}"
    "..."
    "Тишина"
    i "{cps=60}Она что, уже ушла на пары… {w} БЕЗ МЕНЯ?!{/cps}"
    with vpunch
    "Стучит сильнее"
    i "{cps=60}Дани…{/cps}"
    d "{cps=60}УЖЕ ОДЕВАЮСЬ!{/cps}"
    i "{cps=60}Фух…{w} Пойду пока умоюсь, а ты собирайся быстрее!{/cps}"
    scene koridor with fade
    i "{cps=60}И о чём я вообще думаю, Даниэля никогда бы не ушла на пары без меня,{w} она же моя {b}лучшая подруга{b}...{/cps}"
    if banan == True:
        jump end_3
    else:
        $ renpy.notify("Игорь не упал на банан") #уведомление в игре
    scene ymalka with fade
    "{cps=60}Игорь подходит к зеркалу, видит отражение… {w} и своего преподавателя Александра.{/cps}"
    i "{cps=60}А… что…?{/cps}"
    "протирает глаза, преподаватель не исчезает"
    return