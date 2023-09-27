import pygame 
import random
from imagenes import *
from data_preguntados import lista
from variables_preguntados import *

def correcta(letra:str):
    if letra == right:
        return True
    else:
        return False

def pregunta():
    text_pregunta = font.render(lista[contador2]["pregunta"], True, (60, 130, 225))
    screen.blit(text_pregunta,(110,160))

def opcion_1(boton):
    if not boton and correcta(letra_1):
        if 1 in choice:
            screen.blit(imagen3,(200,255))
        else:
            screen.blit(imagen5,(200,255))    
    elif not boton and 1 in choice and not correcta(letra_1):        
        screen.blit(imagen4,(200,255))
    else:
        screen.blit(imagen2,(200,255))
    text_opcion_1 = font_opciones.render(lista[contador2][letra_1], True, (60, 130, 225))    
    screen.blit(text_opcion_1,(250,290))    

def opcion_2(boton):    
    if not boton and correcta(letra_2):
        if 2 in choice:
            screen.blit(imagen3,(200,355))
        else:
            screen.blit(imagen5,(200,355)) 
    elif not boton and 2 in choice and not correcta(letra_2):        
        screen.blit(imagen4,(200,355))
    else:
        screen.blit(imagen2,(200,355))
    text_opcion_2 = font_opciones.render(lista[contador2][letra_2], True, (60, 130, 225))
    screen.blit(text_opcion_2,(250,390))

def opcion_3(boton):
    if not boton and correcta(letra_3):        
        if 3 in choice:
            screen.blit(imagen3,(200,455))
        else:
            screen.blit(imagen5,(200,455)) 
    elif not boton and 3 in choice and not correcta(letra_3):
        screen.blit(imagen4,(200,455))
    else:
        screen.blit(imagen2,(200,455))
    text_opcion_3 = font_opciones.render(lista[contador2][letra_3], True, (60, 130, 225))    
    screen.blit(text_opcion_3,(250,490))

def funcion_boton(letra,tries):
    global acierto
    global intentos_restantes
    global score
    if correcta(letra):
        incorrecta.stop()
        sonido_correcta.set_volume(0.4)
        sonido_correcta.play()
        score += 10
        acierto = True
    elif tries == 2:
        incorrecta.stop()
        incorrecta.set_volume(0.4)
        incorrecta.play()
        intentos_restantes -= 1
    else:
        incorrecta.stop()
        incorrecta_2.set_volume(0.4)
        incorrecta_2.play()
        intentos_restantes -= 1

def boton_musica():
    if musica == True:
        screen.blit(imagen_musica_on,(740,30))
    if musica == False:
        screen.blit(imagen_musica_off,(740,30))

def reset_timer():
    global contador
    contador = 4

def limpiar():
    global boton_1 
    boton_1 = True
    global boton_2 
    boton_2 = True
    global boton_3 
    boton_3 = True
    global acierto 
    acierto = False
    global intentos_restantes
    intentos_restantes = 2
    global choice 
    choice = []
    reset_timer()

def mezclar():
    global letra_1
    global letra_2
    global letra_3
    global right 
    right = lista[contador2]["correcta"]
    random.shuffle(letras)
    letra_1 = letras[0]
    letra_2 = letras[1]
    letra_3 = letras [2]

def siguiente_pregunta(boton):
    screen.blit(imagen_siguiente,(610,460))
    if boton:
        sonido_botones_general()
        limpiar()
        global boton_siguiente 
        boton_siguiente = False
        global contador2
        contador2 += 1
        mezclar()

def reset(boton):
    screen.blit(imagen_reset,(610,520))
    if boton:
        sonido_botones_general()
        limpiar()
        global contador2
        contador2 = 0
        global score
        global mejor_score
        if score > mejor_score:
            mejor_score = score
        score = 0
        global lista
        random.shuffle(lista)
        mezclar()
        global boton_reset
        boton_reset = False

def mostrar_score():
    screen.blit(imagen_score,(265,20))
    text_score = font_score.render(str(score), True, (38, 33, 76))
    screen.blit(text_score,(440,33))

def boton_modo():
    if modo_timer:
        screen.blit(imagen_sin_tiempo,(10,460))
    else:
        screen.blit(imagen_con_tiempo,(10,460))

def boton_timer(timer):
    if timer and contador <= 3:
        screen.blit(imagen_timer,(80,260))
        text_timer = font_score.render(str(contador),True,(218,2,5))
        screen.blit(text_timer,(120,280))

def funcion_timer(timer):
    global lista
    global contador2
    if timer:
        global contador
        global acierto
        global boton_siguiente
        global intentos_restantes
        if acierto or intentos_restantes == 0 or contador == 0:
            boton_siguiente = True
        else:
            contador -= 1

def sonido_botones_general():
    nueva_pregunta_audio.set_volume(0.4)
    nueva_pregunta_audio.play(maxtime=1500)

pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Preguntados")
running = True

tick = pygame.USEREVENT + 0
pygame.time.set_timer(tick,1000)

##### AUDIO #####
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("Dire Straits - Walk Of Life.mp3")
incorrecta = pygame.mixer.Sound("incorrecta.mp3")
incorrecta_2 = pygame.mixer.Sound("tonto.mp3")
sonido_correcta = pygame.mixer.Sound("correcta.mp3")
nueva_pregunta_audio = pygame.mixer.Sound("nueva_pregunta_audio.mp3")

##### FUENTES #####
font = pygame.font.SysFont("Elephant",20)
font_opciones = pygame.font.SysFont("Elephant", 30)
font_score = pygame.font.SysFont("Elephant", 40)

##### VALORES DE INICIO #####
sonido_fondo.set_volume(0.3)
sonido_fondo.play(-1)
modo_timer = False
random.shuffle(lista)
mezclar()
right = lista[0]["correcta"]
reset_timer()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(event.pos)
            if posicion_click[0] > 200 and posicion_click[0] < 600 and posicion_click[1] > 265 and posicion_click[1] < 345:
                if boton_1:
                    boton_1 = False
                    choice.append(1)
                    funcion_boton(letra_1,intentos_restantes)
            elif posicion_click[0] > 200 and posicion_click[0] < 600 and posicion_click[1] > 365 and posicion_click[1] < 445:
                if boton_2:
                    choice.append(2)
                    boton_2 = False
                    funcion_boton(letra_2,intentos_restantes)
            elif posicion_click[0] > 200 and posicion_click[0] < 600 and posicion_click[1] > 465 and posicion_click[1] < 545:
                if boton_3:
                    choice.append(3)
                    boton_3 = False
                    funcion_boton(letra_3,intentos_restantes)
            elif posicion_click[0] > 740 and posicion_click[0] < 790 and posicion_click[1] > 30 and posicion_click[1] < 80:
                musica = not musica
                if musica == True:
                    sonido_fondo.set_volume(0.3)
                    sonido_fondo.play(-1)
                if musica == False:
                    sonido_fondo.stop()
            elif posicion_click[0] > 615 and posicion_click[0] < 785 and posicion_click[1] > 465 and posicion_click[1] < 505:
                boton_siguiente = True
            elif posicion_click[0] > 615 and posicion_click[0] < 785 and posicion_click[1] > 525 and posicion_click[1] < 565:
                boton_reset = True
            elif posicion_click[0] > 10 and posicion_click[0] < 190 and posicion_click[1] > 460 and posicion_click[1] < 510:
                modo_timer = not modo_timer
                boton_reset = True
        if event.type == tick:
            funcion_timer(modo_timer)
    
    screen.blit(imagen_screen,(0,0))   
    screen.blit(imagen,(75,100))
    
    pregunta()
    opcion_1(boton_1)
    opcion_2(boton_2)
    opcion_3(boton_3)
    if contador2 == len(lista) - 1:
        boton_siguiente = False
    siguiente_pregunta(boton_siguiente)
    reset(boton_reset)
    mostrar_score()
    boton_musica()
    boton_modo()
    boton_timer(modo_timer)
    if acierto or intentos_restantes == 0 or contador == 0:
        boton_1 = False
        boton_2 = False
        boton_3 = False
    
    pygame.display.flip()

pygame.quit()