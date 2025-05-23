#--------------------------------------------------------
# Direcionamento do projeto
#--------------------------------------------------------
# 1ª Fase: Cor 
# Formas: quadrado triangulo e circulo
# 2ª Fase: Forma geometrica 
# Formas: quadrado triangulo circulo retangulo e losango
# 3ª Fase: Número e cor 
# Formas: quadrado triangulo circulo e numeros
#--------------------------------------------------------
# Trechos delimitados hashs serão separados em outros ar-
# quivos
#--------------------------------------------------------
import pygame # Verificar as funções/métodos utilizadas dessa biblioteca
import random
import time
import pyautogui # Verificar as funções/métodos utilizadas dessa biblioteca

pygame.init()

# Configuração de janela, fonte e "objetivo"
screen_size = pyautogui.size() # Tuple que contem as proporções da tela utilizada
WIDTH, HEIGHT = screen_size[0], screen_size[1]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Teste de Atenção") #!
font = pygame.font.SysFont(None, 32)
#--------------------------------------------------------
# Cores e formas: Devemos aumentar lista de cores
def color_gen(a, b, c):
    return (a, b, c)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255), # R, G, B
COLORS = [
    color_gen(255, 0, 0),
    color_gen(255, 255, 0),
    color_gen(255, 0, 255),
    color_gen(0, 255, 255),
    color_gen(0, 0, 255),
]

# Lista de formas geométricas
SHAPES = [ 
    'circle', 
    'square', 
    'triangle'
] 
#--------------------------------------------------------

# Variaveis de controle
circle_count = square_count = triangle_count = keypress_count = 0 # Contagem inicial dos elementos
total_shapes = 40 # Contagem de formas que irão aparecer
shape_display_time = 1.0 #Duração que cada forma geometrica vai aparecer na tela

# Funções -----------------------------------------------
def display_text(text): # Essa função exibe o textos, se tiver paciencia, pode ver um jeito melhor de fazer
    screen.fill(BLACK) # Isso aqui é necessário pra "apagar" as coisas que estão atras, se quiser pode alterar também
    defined_text = font.render(text, True, WHITE) # Pq esse true????
    screen.blit(defined_text, (WIDTH // 2 - defined_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    time.sleep(5)

def draw_shape(shape): # Será melhor que possamos utilizar uma função mais generalista, excluindo a necessidade de usar strings pra definir as formas
    screen.fill(BLACK)

    if shape == 'circle':
        pygame.draw.circle(screen, color, (WIDTH // 2, HEIGHT // 2), 100, 1) # Prestar atenção no formato

    elif shape == 'square':
        pygame.draw.rect(screen, color, pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 200), 1)

    elif shape == 'triangle':
        points = [ # Pontos que definem a forma do poligono, nesse caso, um triangulo
                (WIDTH // 2, HEIGHT // 2 - 100),
                (WIDTH // 2 - 100, HEIGHT // 2 +100),
                (WIDTH // 2 + 100, HEIGHT // 2 + 100)
        ]
        pygame.draw.polygon(screen, color, points, 1)
    pygame.display.flip()
#--------------------------------------------------------

display_text("Indique qual cor mais se repete") # tela inicial

for _ in range(total_shapes):
    color = random.choice(COLORS) # Escolhe aleatóriamente uma forma dentro do array que as define
    shape = random.choice(SHAPES) # Escolhe aleatóriamente uma forma dentro do array que as define

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

display_text(f"Aperto: {keypress_count} | Círculos: {circle_count} | Quadrados: {square_count} | Triangulos: {triangle_count}") #Tela final
pygame.quit()
