#Notas:
# 1ª Fase: Cor - a) ; b)
# 2ª Fase: Forma geometrica - 
#     a) ; 
#     b)
# 3ª Fase: Número e cor - a) ; b)

#Lista de formas:
# 1 - quadrado triangulo e circulo
# 2 - quadrado triangulo circulo retangulo e losango
# 4 - quadrado triangulo circulo e numeros

import pygame
import random
import time

# Configuração de janela, fonte e "objetivo"
pygame.init()
WIDTH, HEIGHT = 1366, 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Identifque qual cor mais se repete") #Lembrar de perguntar qual forma deve ser observada
font = pygame.font.SysFont(None, 32)

## Trechos delimitados por duas hashs serão separados em outros arquivos
# Cores, lembrar de alterar e definir
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SHAPES = [ # Lista de formas geométricas
    'circle', 
    'square', 
    'triangle'
] 
##

# Variaveis de controle
circle_count = square_count = triangle_count = keypress_count = 0 # Contagem inicial dos elementos
total_shapes = 40 # Contagem de formas que irão aparecer
shape_display_time = 1.0 #Duração que cada forma geometrica vai aparecer na tela

##
def text_screen(text): # Essa função exibe o textos, se tiver paciencia, pode ver um jeito melhor de fazer
    screen.fill(BLACK) # Isso aqui é necessário pra "apagar" as coisas que estão atras, se quiser pode alterar também
    defined_text = font.render(f"{text}", True, WHITE) # Pq esse true????
    screen.blit(defined_text, (WIDTH // 2 - defined_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    time.sleep(5)

def draw_shape(shape): # Padrão de desenho de formas, vou melhorar essa função. É melhor que possamos utilizar uma função mais generalista, excluindo a necessidade de usar strings pra definir as formas
    screen.fill(BLACK)

    if shape == 'circle':
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), 100, 1) # Prestar atenção no formato

    elif shape == 'square':
        pygame.draw.rect(screen, WHITE, pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 200), 1)

    elif shape == 'triangle':
        points = [ # Pontos que definem a forma do poligono, nesse caso, um triangulo
                (WIDTH // 2, HEIGHT // 2 - 100),
                (WIDTH // 2 - 100, HEIGHT // 2 +100),
                (WIDTH // 2 + 100, HEIGHT // 2 + 100)
        ]
        pygame.draw.polygon(screen, WHITE, points, 1)
    pygame.display.flip()
##

text_screen("Indique qual cor mais se repete") # tela inicial

for _ in range(total_shapes):
    shape = random.choice(SHAPES) #Escolhe aleatóriamente uma forma dentro do array que as define

    if shape == 'circle':
        circle_count += 1 
    elif shape == 'triangle':
        triangle_count += 1 
    elif shape == 'square':
        square_count += 1 
    draw_shape(shape)
    start_time = time.time()
    pressed = False

    while time.time() - start_time < shape_display_time:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #Capta o espaço do teclado
                if not pressed:
                    keypress_count += 1
                    pressed = True

# Tela final
text_screen("Aperto: {keypress_count} | Círculos: {circle_count} | Quadrados: {square_count} | Triangulos: {triangle_count}")
pygame.quit()
