from re import X
from turtle import pos
import pygame
pygame.init()
from random import randint

#Pocições
x = 450
y = 450
#-----------------------------------------------------
y1 = 0
y3 = -15
y4 = -25
y5 = -30
y6 = -5 
#-----------------------------------------------------
v = 20
v1 = -100
v2 = 20
v3 = -25
v4 = -30
v5 = -35
v6 = -29
#imagens
fundo = pygame.image.load('pista.png')
pista1 = pygame.image.load('pista1.png')
#-----------------------------------------------------
carro = pygame.image.load("Lv.png")
carro3 = pygame.image.load("carro3.png")
carro4 = pygame.image.load("carro3.png")
carro5 = pygame.image.load("carro4.png")
carro6 = pygame.image.load("carro4.png")
#-----------------------------------------------------
janela = pygame.display.set_mode((800,650))
pygame.display.set_caption('Jogo de APC/211063194')

#Argumentos
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
#Comandos
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= v
    if comandos[pygame.K_DOWN]:
        y+= v
    if comandos[pygame.K_RIGHT] and x <= 620:
        x+= v
    if comandos[pygame.K_LEFT] and x >= 160:
        x-= v    
    y1 -= v1
    if (y1>=700):
        y1 = -50

#Carros aleatorios
    y3 -= v3
    y4 -= v4
    y5 -= v5
    y6 -= v6
#-----------------------------------------------------       
    if(y3>= 750):
        y3 = randint(-150,-15)
    if(y4>= 750):
        y4 = randint(-200,-25)
    if(y5>= 750):
        y5 = randint(-300,-30)
    if(y6>= 750):
        y6 = randint(-150,-5)        
#Janelas
    janela.blit(fundo,(0,0))
    janela.blit(pista1,(158,y1))
    janela.blit(carro, (x,y))
    janela.blit(carro3, (206,y3))
    janela.blit(carro4, (450,y4))
    janela.blit(carro5, (320,y5))
    janela.blit(carro6, (580,y6))
#Tela
    pygame.display.update()
pygame.quit()
