import pygame

imagen_screen = pygame.image.load("binary-code-rain-stock-animation-68206-1280x720.jpg")
imagen_screen = pygame.transform.scale(imagen_screen,[800,600])

imagen = pygame.image.load("boton_pregunta.png")
imagen = pygame.transform.scale(imagen,[650,150])

imagen2 = pygame.image.load("boton_opcion.png")
imagen2 = pygame.transform.scale(imagen2,[400,100])

imagen3 = pygame.image.load("boton_opcion_correcta.png")
imagen3 = pygame.transform.scale(imagen3,[400,100])

imagen4 = pygame.image.load("boton_opcion_incorrecta.png")
imagen4 = pygame.transform.scale(imagen4,[400,100])

imagen5 = pygame.image.load("boton_opcion_correcta_perdida.png")
imagen5 = pygame.transform.scale(imagen5,[400,100])

imagen_siguiente = pygame.image.load("boton_siguiente.png")
imagen_siguiente = pygame.transform.scale(imagen_siguiente,[180,50])

imagen_reset = pygame.image.load("boton_reset.png")
imagen_reset = pygame.transform.scale(imagen_reset,[180,50])

imagen_score = pygame.image.load("boton_score.png")
imagen_score = pygame.transform.scale(imagen_score,[270,75])

imagen_musica_on = pygame.image.load("musica_on.png")
imagen_musica_on = pygame.transform.scale(imagen_musica_on,[50,50])

imagen_musica_off = pygame.image.load("musica_off.png")
imagen_musica_off = pygame.transform.scale(imagen_musica_off,[50,50])

imagen_timer = pygame.image.load("timer.png")
imagen_timer = pygame.transform.scale(imagen_timer,[110,90])

imagen_con_tiempo = pygame.image.load("boton_con_tiempo.png")
imagen_con_tiempo = pygame.transform.scale(imagen_con_tiempo,[180, 50])

imagen_sin_tiempo = pygame.image.load("boton_sin_tiempo.png")
imagen_sin_tiempo = pygame.transform.scale(imagen_sin_tiempo,[180, 50])