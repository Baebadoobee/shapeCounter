# Nota.: Salvar resultados em um .txt separado
# Nota.: Ajustar seção "número e cor"
# Nota.: Ajustar tamanho da caixa de texto
# Nota.: Adicionar tela com o nome das cores e formas
# Nota.: Verificar rodada de treino da terceira etapa
# Nota.: Salvar o programa de maneira portavel

import pygame
import random
import time
import pyautogui
from moviepy import VideoFileClip
from pygame import mixer
from collections import Counter

# Configurações Globais
class Config:
    SCREEN_SIZE = pyautogui.size()
    WIDTH, HEIGHT = SCREEN_SIZE
    COLORS = {
        'vermelho': (255, 0, 0),
        'amarelo': (255, 255, 0),
        'rosa': (255, 0, 255),
        'cinza': (100, 100, 100),
        'azul': (0, 0, 255),
        'verde': (0, 255, 0),
        'branco': (255, 255, 255)
    }
    COLOR_NAMES = list(COLORS.keys())
    SHAPES = ['circulo', 'quadrado', 'triangulo', 'losango']
    NUMBERS = [str(i) for i in range(1, 10)]
    FONT_SIZE = 60
    SHAPE_DISPLAY_TIME = 1.0
    TARGET_FPS = 60
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SPAWN_AREA_WIDTH = 400
    SPAWN_AREA_HEIGHT = 400
    SPAWN_AREA_X = (WIDTH - SPAWN_AREA_WIDTH) // 2
    SPAWN_AREA_Y = (HEIGHT - SPAWN_AREA_HEIGHT) // 2

class VideoPlayer:
    def __init__(self, screen):
        mixer.init()
        self.screen = screen
    
    def play(self, video_path, target_fps):
        try:
            clip = VideoFileClip(video_path).resized((Config.WIDTH, Config.HEIGHT))
            clock = pygame.time.Clock()
            start_time = pygame.time.get_ticks()
            
            running = True
            while running:
                current_time = (pygame.time.get_ticks() - start_time) / 1000
                if current_time > clip.duration:
                    break
                
                frame = clip.get_frame(current_time)
                frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                self.screen.blit(frame_surface, (0, 0))
                pygame.display.flip()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return False
                
                clock.tick(target_fps)
            
            clip.close()
            return True
        except Exception as e:
            print(f"Erro ao reproduzir vídeo: {e}")
            return False

class AttentionTest:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pygame.display.set_caption("Teste de Atenção")
        self.font = pygame.font.SysFont(None, Config.FONT_SIZE)
        self.big_font = pygame.font.SysFont(None, 72)
        self.video_player = VideoPlayer(self.screen)
        self.reset_counters()

    def get_random_position(self):
        x = random.randint(
            Config.SPAWN_AREA_X,
            Config.SPAWN_AREA_X + Config.SPAWN_AREA_WIDTH
        )
        y = random.randint(
            Config.SPAWN_AREA_Y,
            Config.SPAWN_AREA_Y + Config.SPAWN_AREA_HEIGHT
        )
        return (x, y)
    
    def reset_counters(self):
        self.color_count = {color: 0 for color in Config.COLOR_NAMES}
        self.shape_count = {shape: 0 for shape in Config.SHAPES}
        self.keypress_count = 0
        self.correct_presses = 0
    
    def display_text(self, text, color=Config.WHITE, duration=3):
        self.screen.fill(Config.BLACK)
        lines = text.split('\n')
        for i, line in enumerate(lines):
            text_surface = self.font.render(line, True, color)
            self.screen.blit(text_surface, 
                           (Config.WIDTH//2 - text_surface.get_width()//2, 
                            Config.HEIGHT//2 - (len(lines)*20)//2 + i*40))
        pygame.display.flip()
        time.sleep(duration)
    
    def input_text_screen(self, prompt):
        input_text = ""
        input_rect = pygame.Rect(Config.WIDTH//2 - 200, Config.HEIGHT//2, 400, 50)
        active = True
        
        while active:
            self.screen.fill(Config.BLACK)
            prompt_surface = self.font.render(prompt, True, Config.WHITE)
            self.screen.blit(prompt_surface, (Config.WIDTH//2 - prompt_surface.get_width()//2, Config.HEIGHT//2 - 50))
            
            pygame.draw.rect(self.screen, Config.WHITE, input_rect, 2)
            text_surface = self.font.render(input_text, True, Config.WHITE)
            self.screen.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode.lower()
        
        return input_text
    
    def draw_shape(self, shape, color_name, position, size=50):
        color = Config.COLORS[color_name] 
        x, y = position
        position = self.get_random_position()
        
        if shape == 'circulo':
            pygame.draw.circle(self.screen, color, position, size)
        elif shape == 'quadrado':
            rect = pygame.Rect(x - size, y - size, size * 2, size * 2)
            pygame.draw.rect(self.screen, color, rect)
        elif shape == 'triangulo':
            points = [(x, y - size), (x - size, y + size), (x + size, y + size)]
            pygame.draw.polygon(self.screen, color, points)
        elif shape == 'losango':
            points = [(x, y - size), (x + size, y), (x, y + size), (x - size, y)]
            pygame.draw.polygon(self.screen, color, points)
    
    def draw_number(self, number, color_name, position, size=50):
        color = Config.COLORS[color_name]
        text_surface = self.big_font.render(number, True, color)
        self.screen.blit(text_surface, (position[0] - size//2, position[0] - size//2))
    
    def run_training_phase(self, phase):
        items_to_show = 20
        rand_pos = self.get_random_position()
        center = (Config.WIDTH // 2, Config.HEIGHT // 2)
        
        for _ in range(items_to_show):
            self.screen.fill(Config.BLACK)
            
            if phase == 1:
                shape = random.choice(Config.SHAPES)
                color = random.choice(Config.COLOR_NAMES)
                self.color_count[color] += 1
                self.draw_shape(shape, color, center)
            
            elif phase == 2:
                shape = random.choice(Config.SHAPES)
                color = random.choice(Config.COLOR_NAMES)
                self.shape_count[shape] += 1
                self.draw_shape(shape, color, center)
            
            elif phase == 3:
                if random.random() > 0.7:  # 70% chance de mostrar número
                    number = random.choice(Config.NUMBERS)
                    color = 'vermelho' if random.random() > 0.7 else random.choice(Config.COLOR_NAMES)
                    self.draw_number(number, color, rand_pos)
                else:
                    shape = random.choice(Config.SHAPES)
                    color = random.choice(Config.COLOR_NAMES)
                    self.draw_shape(shape, color, rand_pos)
            
            pygame.display.flip()
            
            start_time = time.time()
            pressed = False
            while time.time() - start_time < Config.SHAPE_DISPLAY_TIME:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and not pressed and phase == 3:
                            pressed = True
                            if color == 'vermelho':
                                self.keypress_count += 1

            #time.sleep(Config.SHAPE_DISPLAY_TIME)
        
        if phase in [1, 2]:
            most_common = max(self.color_count.items(), key=lambda x: x[1])[0] if phase == 1 else \
                         max(self.shape_count.items(), key=lambda x: x[1])[0]
            prompt = "Digite a cor que mais apareceu:" if phase == 1 else "Digite a forma que mais apareceu:"
            answer = self.input_text_screen(prompt)
            
            if answer == most_common:
                self.display_text("Correto!", Config.COLORS['verde'])
            else:
                self.display_text(f"Incorreto! Era {most_common}", Config.COLORS['vermelho'])
    
    def run_main_phase(self, phase):
        items_to_show = 40
        rand_pos = self.get_random_position()
        center = (Config.WIDTH // 2, Config.HEIGHT // 2)
        
        for _ in range(items_to_show):
            self.screen.fill(Config.BLACK)
            
            if phase == 1:
                shape = random.choice(Config.SHAPES)
                color = random.choice(Config.COLOR_NAMES)
                self.color_count[color] += 1
                self.draw_shape(shape, color, center)
            
            elif phase == 2:
                shape = random.choice(Config.SHAPES)
                color = random.choice(Config.COLOR_NAMES)
                self.shape_count[shape] += 1
                self.draw_shape(shape, color, center)
            
            elif phase == 3:
                if random.random() > 0.3:  # 70% chance de mostrar número
                    number = random.choice(Config.NUMBERS)
                    color = 'azul' if random.random() > 0.7 else random.choice(Config.COLOR_NAMES)
                    self.draw_number(number, color, rand_pos)
                    
                    if color == 'azul':
                        self.correct_presses += 1
                else:
                    shape = random.choice(Config.SHAPES)
                    color = random.choice(Config.COLOR_NAMES)
                    self.draw_shape(shape, color, rand_pos)
            
            pygame.display.flip()
            
            start_time = time.time()
            pressed = False
            while time.time() - start_time < Config.SHAPE_DISPLAY_TIME:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and not pressed and phase == 3:
                            pressed = True
                            if color == 'azul':
                                self.keypress_count += 1
        
        if phase in [1, 2]:
            most_common = max(self.color_count.items(), key=lambda x: x[1])[0] if phase == 1 else \
                         max(self.shape_count.items(), key=lambda x: x[1])[0]
            prompt = "Digite a cor que mais apareceu:" if phase == 1 else "Digite a forma que mais apareceu:"
            answer = self.input_text_screen(prompt)
            
            if answer == most_common:
                self.display_text("Correto!", Config.COLORS['verde'])
            else:
                self.display_text(f"Incorreto! Era {most_common}", Config.COLORS['vermelho'])
        
        return True
    
    def run(self):
        try:
            # Intro
            if not self.video_player.play("media/intro.mp4", Config.TARGET_FPS):
                return

            # Fase 1
            if not self.video_player.play("media/first_level.mp4", Config.TARGET_FPS):
                return

            if not self.video_player.play("media/training_round.mp4", Config.TARGET_FPS):
                return
            
            self.reset_counters()
            self.run_training_phase(1)
            
            if not self.video_player.play("media/main_round.mp4", Config.TARGET_FPS):
                return
            
            self.reset_counters()
            self.run_main_phase(1)
            
            # Fase 2
            if not self.video_player.play("media/second_level.mp4", Config.TARGET_FPS):
                return

            if not self.video_player.play("media/training_round.mp4", Config.TARGET_FPS):
                return
            
            self.reset_counters()
            self.run_training_phase(2)
            
            if not self.video_player.play("media/main_round.mp4", Config.TARGET_FPS):
                return
            
            self.reset_counters()
            self.run_main_phase(2)

            # Fase 3
            if not self.video_player.play("media/training_round_alt.mp4", Config.TARGET_FPS):
                return
            
            self.reset_counters()
            self.run_training_phase(3)
            
            result_text = f"Fase 3: Você acertou {self.keypress_count} de {self.correct_presses} números vermelhos"
            self.display_text(result_text, duration=5)
            
            if not self.video_player.play("media/third_level.mp4", Config.TARGET_FPS):
                return
            
            self.reset_counters()
            self.run_main_phase(3)

            result_text = f"Fase 3: Você acertou {self.keypress_count} de {self.correct_presses} números azuis"
            self.display_text(result_text, duration=5)

            if not self.video_player.play("media/end_screen.mp4", Config.TARGET_FPS):
                return

            if not self.video_player.play("media/credit_screen.mp4", Config.TARGET_FPS):
                return
            
        finally:

            pygame.quit()

if __name__ == "__main__":
    game = AttentionTest()
    game.run()
