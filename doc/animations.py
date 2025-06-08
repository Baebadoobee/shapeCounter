from manim import *

TITLE_FONT_SIZE = 42
MEDIUM_FONT_SIZE = 36
REGULAR_FONT_SIZE = 28

class intro(Scene):
    def construct(self):

        logo = ImageMobject("logo.png").set(width=1, heigh=1).set_y(3)
        title = Paragraph(
                "Tarefa de Atenção Seletiva e Dividida",
                "(T-ASD)",
                alignment="center",
                line_spacing=0.3,
                font_size=TITLE_FONT_SIZE
        )
        prof = Text("Orientadora: Profª Me. Lais Sousa Anias", font_size=REGULAR_FONT_SIZE)
        students = Paragraph(
                "Discentes: Udson Cerqueira de Santana",
                "Vinicius Neves da Silva Gomes",
                alignment="center",
                line_spacing=0.3,
                font_size=REGULAR_FONT_SIZE
        )

        displayed_text = VGroup(
                title,
                prof,
                students
        ).arrange(DOWN, buff=1, center=True).set_y(-1.5)

        self.play(
            Succession(
                FadeIn(logo, run_time=1),
                Wait(8),
                FadeOut(logo, run_time=1)
            ),
            Succession(
                Write(
                    displayed_text,
                    lag_ratio=0.2,
                    run_time=2
                ),
                Wait(6),
                Unwrite(
                    displayed_text,
                    lag_ratio=0.2,
                    run_time=2
                )
            ), 
        )

class training_round(Scene):
    def construct(self):

        displayed_text = Text("Rodada de treino")

        self.play(
            Succession(
                Write(displayed_text, run_time=1),
                Wait(8),
                Unwrite(displayed_text, run_time=1)
            )
        )

class main_round(Scene):
    def construct(self):

        displayed_text = Text("Rodada principal")

        self.play(
            Succession(
                Write(displayed_text, run_time=1),
                Wait(8),
                Unwrite(displayed_text, run_time=1)
            )
        )

class first_level(Scene):
    def construct(self):

        displayed_text = Text("Indique a cor que mais se repete")

        self.play(
            Succession(
                Write(displayed_text, run_time=1),
                Wait(8),
                Unwrite(displayed_text, run_time=1)
            )
        )

class second_level(Scene):
    def construct(self):

        displayed_text = Text("Indique a forma que mais se repete")

        self.play(
            Succession(
                Write(displayed_text, run_time=1),
                Wait(8),
                Unwrite(displayed_text, run_time=1)
            )
        )

class training_round_alt(Scene):
    def construct(self):

        displayed_text = Paragraph(
                "Pressione a tecla espaço toda vez que",
                "um número da cor vermelha aparecer",
                alignment="center",
                line_spacing=0.3,
                #font_size=MEDIUM_FONT_SIZE
        )

        self.play(
            Succession(
                Write(displayed_text, run_time=1),
                Wait(8),
                Unwrite(displayed_text, run_time=1)
            )
        )

class third_level(Scene):
    def construct(self):

        displayed_text = Paragraph(
                "Pressione a tecla espaço toda vez que",
                "um número da cor azul aparecer",
                alignment="center",
                line_spacing=0.3,
                #font_size=MEDIUM_FONT_SIZE
        )

        self.play(
            Succession(
                Write(displayed_text, run_time=1),
                Wait(8),
                Unwrite(displayed_text, run_time=1)
            )
        )


class end_screen(Scene):
    def construct(self):

        displayed_text = Text("Obrigado pela participação!")

        self.play(
            Succession(
                Write(displayed_text, run_time=1),
                Wait(8),
                Unwrite(displayed_text, run_time=1)
            )
        )

class credits(Scene):
    def construct(self):

        displayed_text = Paragraph(
                "Trabalho feito  em colbaração dos estudantes Vinicius",
                "Neves da Silva gomes e Udson Cerqueira de Santana",
                "estudantes do curso de Psicologia na Universidade",
                "Maria Milza - UNIMAM, a pedido da Profª Me. Lais",
                "Sousa Anias.",
                "",
                "Feito com o apoio de Vinícius da Silva Oliveira,",
                "estudante de Licenciatura em Biologia na",
                "Universidade Federal do Recõncavo da Bahia - UFRB",
                alignment="center",
                line_spacing=0.3,
                font_size=REGULAR_FONT_SIZE
        )

        self.play(
            Succession(
                Write(displayed_text, run_time=1),
                Wait(8),
                Unwrite(displayed_text, run_time=1)
            )
        )
