import pygame 
from pygame.locals import *
from sys import exit
from random import randint 
import os

os.system('cls')

pygame.init()

# Musica

musica = pygame.mixer.music.load("..\Jogo-Cobrinha-Enzo-Dourado\projeto-little-snake/assets\music\Castlevania - Vampire Killer (Courtyard).mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Barulho Colisão

som_colisao = pygame.mixer.Sound("..\Jogo-Cobrinha-Enzo-Dourado\projeto-little-snake/assets\music\smw_kick.wav")
som_colisao.set_volume(0.6)


# Barulho Morte

morte = pygame.mixer.Sound("..\Jogo-Cobrinha-Enzo-Dourado\projeto-little-snake/assets\music\Super Mario Bros - game over song.wav")
morte.set_volume(0.1)

# Janela

larg = 1366
alt = 768

tela = pygame.display.set_mode((larg, alt))

# Título

pygame.display.set_caption('Jogo da Cobrinha')

# Configs Snake
    # Posição
x_cobra = int(larg / 2)
y_cobra = int(alt / 2)

    # Tamanhos
tamanho_cobra = 15
altura_cobra = 15

# Configs maçã
    # Posição
    
x_maca = randint(66, 1300)
y_maca = randint(68, 700)

# Configs maçã dourada
    # Posição

x_maca_dourada = randint(66, 1300)
y_maca_dourada = randint(68, 700)

# Configs maçã preta
    # Posição

x_maca_preta = randint(66, 1300)
y_maca_preta = randint(68, 700)

# Configs bomb
    # Posição

x_bomba = randint(66, 1300)
y_bomba = randint(68, 700)



# Controle de velocidade

timer = pygame.time.Clock()

# Controle Movimentação
velocidade = 3.5
x_controle = velocidade
y_controle = 0

# Pontuação

pontos = 0
mostrar_maca_dourada = False
mostrar_maca_preta = False
mostrar_bomba = False

# Fontes
# Pontos (txt)
font = pygame.font.SysFont('arial', 40, True, False)
# Game over (txt)
font_over = pygame.font.SysFont('arial', 100, True, False)
# Pause (txt)
font_pause = pygame.font.SysFont('arial', 100, True, False)
# Opições (txt)
font_opt = pygame.font.SysFont('arial', 35, True, False)
# Opições Img (txt)
font_opt_img = pygame.font.SysFont('arial', 15, True, False)
# Créditos (txt)
font_credito = pygame.font.SysFont('arial', 20, True, False)

# Lista cobra

lista_cobra = []

comprimento_inical = 5

morreu = False

pausado = False

# img_cobra = pygame.image.load('..\Senai-Python\Outros\PyGame\Jogo_02-Cobrinha\img\cobrinha_rosto_01.png')
# img_cobra = pygame.transform.scale(img_cobra, (tam_snake, alt_snake))

# Maçãs e bomba
img_maca = pygame.image.load("..\Jogo-Cobrinha-Enzo-Dourado\projeto-little-snake/assets\img\maca_vermelha_formatada.png")
img_maca_dourada = pygame.image.load('..\Jogo-Cobrinha-Enzo-Dourado\projeto-little-snake/assets\img\maca_dourada.png')
img_maca_preta = pygame.image.load('..\Jogo-Cobrinha-Enzo-Dourado\projeto-little-snake/assets\img\maca_preta_formatada.png')
img_bomba = pygame.image.load('..\Jogo-Cobrinha-Enzo-Dourado\projeto-little-snake/assets\img/bomba.png')

# Tamanhos maçãs e bomba
img_maca = pygame.transform.scale(img_maca, (27, 27))
img_maca_dourada = pygame.transform.scale(img_maca_dourada, (27, 27))
img_maca_preta = pygame.transform.scale(img_maca_preta, (27, 27))
img_bomba = pygame.transform.scale(img_bomba, (40, 40))
# Fundo

grama_fundo = pygame.image.load('..\Jogo-Cobrinha-Enzo-Dourado\projeto-little-snake/assets\img\grama_02.jpg') # Carrega a imagem da url
grama = pygame.transform.scale(grama_fundo, (larg, alt)) # Ajusta a imagem ao tamanho da tela [MUDAR PARA grama_meu_not]

# Movimentação
    # Direita
def direita():
    global x_controle, y_controle

    if event.key == K_d or event.key == K_RIGHT:
        if x_controle == -velocidade:
            pass
        else:
            x_controle = velocidade
            y_controle = 0

    # Esquerda
def esquerda():
     global x_controle, y_controle

     if event.key == K_a or event.key == K_LEFT: 
        if x_controle == velocidade:
            pass 
        else:
            x_controle = -velocidade
            y_controle = 0
    
    # Cima
def cima():
    global x_controle, y_controle

    if event.key == K_w or event.key == K_UP:
        if y_controle == velocidade:
            pass
        else:
            x_controle = 0
            y_controle = -velocidade
    # Baixo
def baixo():
    global x_controle, y_controle

    if event.key == K_s or event.key == K_DOWN:
        if y_controle == -velocidade:
            pass
        else:
            x_controle = 0
            y_controle = velocidade 
                    

# Criação da Cobra

def aumenta_cobra(lista_cobra):
    for xEy in lista_cobra:
        # xEy = [x, y]
        pygame.draw.rect(tela, (0, 0, 255), (xEy[0], xEy[1], tamanho_cobra, altura_cobra))
        
# Perdeu Jogo

def game_over():
    global morreu, ret_over, over_formatado, game_over_opt, opt_formatado, ret_opt
    global mostrar_maca_dourada, mostrar_maca_preta, mostrar_bomba
    global game_over

    # Parar música de fundo e tocar som de morte
    pygame.mixer.music.stop()
    morte.play()

    # Fonte e mensagem
  
    game_over_msg = '¡GAME OVER!'
    game_over_opt = '"R" = Jogar Novamente || "B" = Sair.'
    over_formatado = font_over.render(game_over_msg, True, (255, 255, 255))
    opt_formatado = font_opt.render(game_over_opt, True, (255, 255, 255))
    ret_over = over_formatado.get_rect()
    ret_opt = opt_formatado.get_rect()
    morreu = True

    while morreu:
        tela.fill((55, 255, 55))
        tela.blit(grama, (0, 0))

        # Desenha a cobra
        aumenta_cobra(lista_cobra)
        pygame.draw.rect(tela, (0, 0, 255), (x_cobra, y_cobra, tamanho_cobra, altura_cobra))

        # Desenha itens especiais visíveis
        tela.blit(img_maca, (x_maca - 10, y_maca - 10))
        if pontos % 6 == 0 and pontos != 0:
            aparecer_golden_apple()

        if pontos % 10 == 0 and pontos != 0 and not mostrar_maca_dourada and not mostrar_bomba:
            golden_apple_and_bomb_and_black()

        if mostrar_maca_dourada:
            tela.blit(img_maca_dourada, (x_maca_dourada - 10, y_maca_dourada - 10))

        # Pontuação
        texto_pontos = font.render(f'Pontos: {pontos}', True, (255, 255, 255))
        tela.blit(texto_pontos, ((larg // 2) - 70, 40))

        # Tela escurecida
        overlay = pygame.Surface((larg, alt), pygame.SRCALPHA)
        overlay.fill((220, 0, 0, 180))  
        tela.blit(overlay, (0, 0))

        # Mensagem central
        ret_over.center = (larg // 2, alt // 2 - 70)
        tela.blit(over_formatado, ret_over)

        ret_opt.center = (larg // 2, alt // 2 + 50)
        tela.blit(opt_formatado, ret_opt)

        # Créditos
        texto_credito = font_credito.render('Enzo Rodrigues Dourado || Senai - Python', True, (255,255, 255))
        pos_credito = texto_credito.get_rect(center=(larg // 2, alt - 50))
        tela.blit(texto_credito, pos_credito)

        # Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    reiniciar()
                elif event.key == K_b:
                    pygame.quit()
                    exit()

        pygame.display.update()


# Reiniciar jogo

def reiniciar():
    global pontos, comprimento_inical, velocidade, x_cobra, y_cobra, x_maca, y_maca, x_maca_dourada, y_maca_dourada, list_head, lista_cobra, morreu, morte, musica, mostrar_maca_dourada, mostrar_maca_preta, x_maca_preta, y_maca_preta, x_controle, y_controle
    
    pontos = 0
    comprimento_inical = 5
    
    velocidade = 3.5
    
    x_cobra = int(alt / 2)
    y_cobra = int(alt / 2)
    
    x_controle = velocidade
    y_controle = 0
    
    x_maca = randint(66, 1300)
    y_maca = randint(68, 700)

    mostrar_maca_dourada = False
    mostrar_maca_preta = False

    x_maca_dourada = randint(66, 1300)
    y_maca_dourada = randint(68, 700)

    x_maca_preta = randint(66, 1300)
    y_maca_preta = randint(68, 700)
    
    list_head = []
    lista_cobra = []
    
    morreu = False
    
    morte.stop()
    pygame.mixer.music.stop() 
    pygame.mixer.music.play(-1)


# Comer Maçã

def comer_apple():
    global x_maca, y_maca, pontos, comprimento_inical, som_colisao

    x_maca = randint(66, 1300)
    y_maca = randint(68, 700)

    pontos = pontos + 1
    comprimento_inical = comprimento_inical + 1
    som_colisao.play()

# Aumentar Velocidade

def aumentar_velocidade():
    global velocidade
    if pontos > 20:
        velocidade = 5.5

    if pontos > 30:
        velocidade = 7

    if pontos > 50:
        velocidade = 9.5

    if pontos > 70:
        velocidade =  15  

    if pontos >= 90:
        velocidade = 20

# Comer Maçã dourada

def comer_golden_apple():
    global x_maca_dourada, y_maca_dourada, pontos, comprimento_inical, mostrar_maca_dourada

    x_maca_dourada = randint(66, 1300)
    y_maca_dourada = randint(68, 700)

    pontos += 3
    comprimento_inical += 5
    som_colisao.play()

    mostrar_maca_dourada = False

# Comer Maçã preta

def comer_black_apple():
    global x_maca_preta, y_maca_preta, pontos, comprimento_inical, mostrar_maca_preta

    x_maca_preta = randint(66, 1300)
    y_maca_preta = randint(68, 700)

    pontos += 15
    comprimento_inical += 20
    som_colisao.play()

    mostrar_maca_preta = False

# Criar maçã dourada

def aparecer_golden_apple():
    global maca_dourada, mostrar_maca_dourada

    tela.blit(img_maca_dourada, (x_maca_dourada - 10, y_maca_dourada - 10))
    maca_dourada = pygame.Rect(x_maca_dourada - 10, y_maca_dourada - 10, 15, 15)

    mostrar_maca_dourada = True

# Cria maçã dourada e bomba
def golden_apple_and_bomb_and_black():
    global maca_dourada, maca_preta, bomba

    tela.blit(img_maca_dourada, (x_maca_dourada - 10, y_maca_dourada - 10))
    maca_dourada = pygame.Rect(x_maca_dourada - 10, y_maca_dourada - 10, 15, 15)

    tela.blit(img_bomba, (x_bomba - 10, y_bomba - 10))
    bomba = pygame.Rect(x_bomba - 10, y_bomba - 10, 15, 15)
    
    

    tela.blit(img_maca_preta, (x_maca_preta - 10, y_maca_preta - 10))
    maca_preta = pygame.Rect(x_maca_preta - 10, y_maca_preta - 10, 15, 15)


def pause():
    global pausado, lista_cobra, x_cobra, y_cobra, tamanho_cobra, altura_cobra, pontos # Cobra / Jogo
    global maca_dourada, maca_preta, bomba # bomba e maçãs
    global x_maca, y_maca, x_maca_dourada, y_maca_dourada, x_maca_preta, y_maca_preta # Maçãs posições
    global x_bomba, y_bomba # Posição bomba
    global mostrar_maca_dourada, mostrar_maca_preta, mostrar_bomba # Mostrar bomba e maçãs

    while pausado and not morreu:
        tela.fill((55, 255, 55))
        tela.blit(grama, (0, 0))

        # Cobra parada na tela
        aumenta_cobra(lista_cobra)
        pygame.draw.rect(tela, (0, 0, 255), (x_cobra, y_cobra, tamanho_cobra, altura_cobra))

        # Maçãs na tela
        tela.blit(img_maca, (x_maca - 10, y_maca - 10))
        if pontos % 6 == 0 and pontos != 0:
            aparecer_golden_apple()

        if pontos % 10 == 0 and pontos != 0 and not mostrar_maca_dourada and not mostrar_bomba:
            golden_apple_and_bomb_and_black()


        if mostrar_maca_dourada:
            tela.blit(img_maca_dourada, (x_maca_dourada - 10, y_maca_dourada - 10))
            
        # Pontuação visível
        msg = f'Points: {pontos}'
        formated_msg = font.render(msg, True, (255, 255, 255))
        tela.blit(formated_msg, (600, 40))

        # Escurecer tela
        overlay = pygame.Surface((larg, alt), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 140))  # Transparência
        tela.blit(overlay, (0, 0))

        # Texto "PAUSADO
        texto_pausado = font_pause.render("¡PAUSADO!", True, (255, 255, 255))
        pos_texto = texto_pausado.get_rect(center=(larg // 2, alt // 2 - 100))
        tela.blit(texto_pausado, pos_texto)

        # Instruções
        texto_instrucao = font_opt.render(f"ESC = Continuar || B = Sair", True, (255, 181, 41))
        pos_instrucao = texto_instrucao.get_rect(center=(larg // 2, (alt // 2) + 30))
        tela.blit(texto_instrucao, pos_instrucao)

        # Imagens
        # Maca
        pos_img_maca = img_maca.get_rect(center=(larg // 2 - 150, alt // 2 + 100))
        tela.blit(img_maca, pos_img_maca)
        # Maca dourada
        pos_img_maca_dourada = img_maca_dourada.get_rect(center=(larg // 2 - 150, alt // 2 + 150))
        tela.blit(img_maca_dourada, pos_img_maca_dourada)
        # Maca preta    
        pos_img_maca_preta = img_maca_preta.get_rect(center=(larg // 2 - 150, alt // 2 + 200))
        tela.blit(img_maca_preta, pos_img_maca_preta)
        # Bomba
        pos_img_bomba = img_bomba.get_rect(center=(larg // 2 - 150, alt // 2 + 250))
        tela.blit(img_bomba, pos_img_bomba)
        # Texto
        # Maca img
        texto_maca = font_opt_img.render(f"= Maçã || + 1 Ponto", True, (255, 255, 255))
        pos_texto_maca = texto_maca.get_rect(center=(larg // 2 - 60, (alt // 2) + 100))
        tela.blit(texto_maca, pos_texto_maca)

        # Maca Dourada img
        texto_maca_dourada = font_opt_img.render(f"= Maçã Dourada || + 3 Ponto", True, (255, 255, 255))
        pos_texto_maca_dourada = texto_maca_dourada.get_rect(center=(larg // 2 - 30, (alt // 2) + 150))
        tela.blit(texto_maca_dourada, pos_texto_maca_dourada)

        # Maca preta img
        texto_maca_preta = font_opt_img.render(f"= Maçã Preta || + 15 Ponto", True, (255, 255, 255))
        pos_texto_maca_preta = texto_maca_preta.get_rect(center=(larg // 2 - 37, (alt // 2) + 200))
        tela.blit(texto_maca_preta, pos_texto_maca_preta)

        # Bomba img
        texto_bomba = font_opt_img.render(f"= Bomba || Game Over!", True, (255, 255, 255))
        pos_texto_bomba = texto_bomba.get_rect(center=(larg // 2 - 47, (alt // 2) + 250))
        tela.blit(texto_bomba, pos_texto_bomba)

        texto_credito = font_credito.render('Enzo Rodrigues Dourado || Senai - Python', True, (255,255, 255))
        pos_credito = texto_credito.get_rect(center=(larg // 2, alt - 50))
        tela.blit(texto_credito, pos_credito)

        pygame.mixer.music.stop() 
        pygame.display.update()

        # Captura eventos enquanto pausado
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pausado = False
                    pygame.mixer.music.play(-1)
                elif event.key == K_b:
                    pygame.quit()
                    exit()



    
# =============================================================================================================================#
# =============================================================================================================================#
# =================================================================================================================#

# Loop Principal

while True:
    # Tela (fundo)
    tela.fill((55, 255, 55))
    tela.blit(grama, (0, 0))

    # FPS
    timer.tick(60)

    # Mensagem (Pontos)
    msg = f'Points: {pontos}'
    formated_msg = font.render(msg, True, (255, 255, 255))
    
    # Loop eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not morreu:
                pausado = not pausado
        
        if pausado and not morreu:
            pause()

        if event.type == KEYDOWN: 
            esquerda()
            direita()
            cima()
            baixo()
        
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
                    
    cobra = pygame.draw.rect(tela, (0, 0, 255), (x_cobra, y_cobra, tamanho_cobra, altura_cobra))
    cobra = pygame.Rect(x_cobra - 10, y_cobra - 10, 40, 40)
    
    tela.blit(img_maca, (x_maca, y_maca))
    apple = pygame.Rect(x_maca , y_maca , 15, 15)

        
    if cobra.colliderect(apple):
        comer_apple()

    aumentar_velocidade()

    if pontos % 6 == 0 and pontos != 0:
        aparecer_golden_apple()

        if cobra.colliderect(maca_dourada):
            comer_golden_apple()
        else:
            mostrar_maca_dourada = False

    if pontos % 10 == 0 and pontos != 0 and not mostrar_maca_dourada and not mostrar_bomba:
        golden_apple_and_bomb_and_black()
        
        if cobra.colliderect(maca_dourada):
            comer_golden_apple()
        else:
            mostrar_maca_dourada = False

        if cobra.colliderect(maca_preta):
            comer_black_apple()
        else:
            mostrar_maca_preta = False

        if cobra.colliderect(bomba):
            game_over() 
    
        # Essa Lista armazena todas as posições que a cobra passa 
    list_head = []
    list_head.append(x_cobra)
    list_head.append(y_cobra)
    
    
    lista_cobra.append(list_head)
    
    if lista_cobra.count(list_head) > 1:
        game_over()
        
    # Ao colidir com as bordas, morre            
    if x_cobra > larg or x_cobra < 0 or y_cobra > alt or y_cobra < 0:
        game_over()
     
    
    if (len(lista_cobra) > comprimento_inical):
        del lista_cobra[0]
    
    
    aumenta_cobra(lista_cobra)
    
    tela.blit(formated_msg, (600, 40))
    pygame.display.flip()
