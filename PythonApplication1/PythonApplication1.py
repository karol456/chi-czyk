# coding=utf-8
import pygame
import pygame.locals

pygame.init()  # funkcja ładująca moduły pyGame'a odpowiedzialne m.in. za dźwięk czy grafikę


class Board(object):
    """
    Plansza do gry. Odpowiada za rysowanie okna gry.
    """

    def __init__(width, height):
        """
        Konstruktor planszy do gry. Przygotowuje okienko gry.
        """


okno = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Chińczyk')

while True:
    pygame.draw.rect(okno, (0, 0, 0), (0, 0, 288, 288))
    pygame.draw.rect(okno, (0, 150, 0), (1, 1, 286, 286))
    pygame.draw.rect(okno, (0, 0, 0), (49, 49, 190, 190))
    pygame.draw.rect(okno, (255, 255, 255), (50, 50, 188, 188))

    #pygame.draw.ellipse(okno, (0, 150, 0), (60, 60, 45, 45))
    #pygame.draw.ellipse(okno, (0, 150, 0), (115, 60, 45, 45))
    #pygame.draw.ellipse(okno, (0, 150, 0), (60, 115, 45, 45))
    #pygame.draw.ellipse(okno, (0, 150, 0), (115, 115, 45, 45))

    pygame.draw.rect(okno, (0, 0, 0), (288, 0, 144, 144))

    pygame.draw.rect(okno, (0, 0, 0), (431, 0, 288, 288))
    pygame.draw.rect(okno, (255, 0, 0), (432, 1, 286, 286))
    pygame.draw.rect(okno, (0, 0, 0), (480, 49, 190, 190))
    pygame.draw.rect(okno, (255, 255, 255), (481, 50, 188, 188))

    #pygame.draw.ellipse(okno, (255, 0, 0), (435, 60, 45, 45))
    #pygame.draw.ellipse(okno, (255, 0, 0), (490, 60, 45, 45))
    #pygame.draw.ellipse(okno, (255, 0, 0), (435, 115, 45, 45))
    #pygame.draw.ellipse(okno, (255, 0, 0), (490, 115, 45, 45))

    pygame.draw.rect(okno, (255, 255, 255), (288, 1, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (336, 1, 47, 47))  # 1
    pygame.draw.rect(okno, (255, 255, 255), (384, 1, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 49, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 49, 47, 47))  # 2
    pygame.draw.rect(okno, (255, 0, 0), (384, 49, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 97, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 97, 47, 47))  # 3
    pygame.draw.rect(okno, (255, 255, 255), (384, 97, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 145, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 145, 47, 47))  # 4
    pygame.draw.rect(okno, (255, 255, 255), (384, 145, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 193, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 193, 47, 47))  # 5
    pygame.draw.rect(okno, (255, 255, 255), (384, 193, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 241, 47, 47))
    pygame.draw.rect(okno, (255, 0, 0), (336, 241, 47, 47))  # 6
    pygame.draw.rect(okno, (255, 255, 255), (384, 241, 47, 47))

    pygame.draw.rect(okno, (0, 0, 0), (0, 288, 144, 144))

    pygame.draw.rect(okno, (255, 255, 255), (1, 288, 47, 47))  ##########
    pygame.draw.rect(okno, (0, 150, 0), (49, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (97, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (145, 288, 47, 47))  # lewa
    pygame.draw.rect(okno, (255, 255, 255), (193, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (241, 288, 47, 47))  ##########  1
    pygame.draw.rect(okno, (255, 255, 255), (431, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (479, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (527, 288, 47, 47))  # prawa
    pygame.draw.rect(okno, (255, 255, 255), (575, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (623, 288, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (671, 288, 47, 47))  ##########

    pygame.draw.rect(okno, (255, 255, 255), (1, 336, 47, 47))  ##########
    pygame.draw.rect(okno, (0, 150, 0), (49, 336, 47, 47))
    pygame.draw.rect(okno, (0, 150, 0), (97, 336, 47, 47))
    pygame.draw.rect(okno, (0, 150, 0), (145, 336, 47, 47))  # lewa
    pygame.draw.rect(okno, (0, 150, 0), (193, 336, 47, 47))
    pygame.draw.rect(okno, (0, 150, 0), (241, 336, 47, 47))  ##########  2
    pygame.draw.rect(okno, (0, 0, 255), (431, 336, 47, 47))
    pygame.draw.rect(okno, (0, 0, 255), (479, 336, 47, 47))
    pygame.draw.rect(okno, (0, 0, 255), (527, 336, 47, 47))  # prawa
    pygame.draw.rect(okno, (0, 0, 255), (575, 336, 47, 47))
    pygame.draw.rect(okno, (0, 0, 255), (623, 336, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (671, 336, 47, 47))  ##########

    pygame.draw.rect(okno, (255, 255, 255), (1, 384, 47, 47))  ##########
    pygame.draw.rect(okno, (255, 255, 255), (49, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (97, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (145, 384, 47, 47))  # lewa
    pygame.draw.rect(okno, (255, 255, 255), (193, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (241, 384, 47, 47))  ##########  3
    pygame.draw.rect(okno, (255, 255, 255), (431, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (479, 384, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (527, 384, 47, 47))  # prawa
    pygame.draw.rect(okno, (255, 255, 255), (575, 384, 47, 47))
    pygame.draw.rect(okno, (0, 0, 255), (623, 384, 47, 49))
    pygame.draw.rect(okno, (255, 255, 255), (671, 384, 47, 47))  ##########

    pygame.draw.rect(okno, (0, 0, 0), (0, 431, 288, 288))
    pygame.draw.rect(okno, (255, 255, 0), (1, 432, 286, 286))
    pygame.draw.rect(okno, (0, 0, 0), (49, 480, 190, 190))
    pygame.draw.rect(okno, (255, 255, 255), (50, 481, 188, 188))

    #pygame.draw.ellipse(okno, (120, 0, 255), (60, 433, 45, 45))
    #pygame.draw.ellipse(okno, (120, 0, 255), (115, 433, 45, 45))
    #pygame.draw.ellipse(okno, (120, 0, 255), (60, 483, 45, 45))
    #pygame.draw.ellipse(okno, (120, 0, 255), (115, 483, 45, 45))

    pygame.draw.rect(okno, (0, 0, 0), (431, 431, 288, 288))
    pygame.draw.rect(okno, (0, 0, 255), (432, 432, 286, 286))
    pygame.draw.rect(okno, (0, 0, 0), (480, 480, 190, 190))
    pygame.draw.rect(okno, (255, 255, 255), (481, 481, 188, 188))

    #pygame.draw.ellipse(okno, (0, 0, 255), (445, 440, 45, 45))
    #pygame.draw.ellipse(okno, (0, 0, 255), (495, 440, 45, 45))
    #pygame.draw.ellipse(okno, (0, 0, 255), (445, 495, 45, 45))
    #pygame.draw.ellipse(okno, (0, 0, 255), (495, 495, 45, 45))

    pygame.draw.rect(okno, (255, 255, 255), (288, 431, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 431, 47, 47))  # 1
    pygame.draw.rect(okno, (255, 255, 255), (384, 431, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 479, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 479, 47, 47))  # 2
    pygame.draw.rect(okno, (255, 255, 255), (384, 479, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 527, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 527, 47, 47))  # 3
    pygame.draw.rect(okno, (255, 255, 255), (384, 527, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 575, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 575, 47, 47))  # 4
    pygame.draw.rect(okno, (255, 255, 255), (384, 575, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (288, 623, 47, 47))
    pygame.draw.rect(okno, (255, 255, 0), (336, 623, 47, 47))  # 5
    pygame.draw.rect(okno, (255, 255, 255), (384, 623, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (288, 671, 47, 47))
    pygame.draw.rect(okno, (255, 255, 255), (336, 671, 47, 47))  # 6
    pygame.draw.rect(okno, (255, 255, 255), (384, 671, 47, 47))

    pygame.draw.rect(okno, (0, 0, 0), (288, 288, 144, 144))

    pygame.draw.line(okno, (255, 255, 255), (288, 288), (430, 430))
    pygame.draw.line(okno, (255, 255, 255), (288, 430), (431, 288))

    pygame.draw.line(okno, (255, 255, 0), (286, 430), (429, 430))
    #pygame.draw.line(okno, (255, 255, 0), (291, 429), (428, 429))
    #pygame.draw.line(okno, (255, 255, 0), (292, 428), (427, 428))
    #pygame.draw.line(okno, (255, 255, 0), (293, 427), (426, 427))
    #pygame.draw.line(okno, (255, 255, 0), (294, 426), (425, 426))
    #pygame.draw.line(okno, (255, 255, 0), (295, 425), (424, 425))
    #pygame.draw.line(okno, (255, 255, 0), (296, 424), (423, 424))
    #pygame.draw.line(okno, (255, 255, 0), (297, 423), (422, 423))
    #pygame.draw.line(okno, (255, 255, 0), (298, 422), (421, 422))
    #pygame.draw.line(okno, (255, 255, 0), (299, 421), (420, 421))
    #pygame.draw.line(okno, (255, 255, 0), (300, 420), (419, 420))
    #pygame.draw.line(okno, (255, 255, 0), (301, 419), (418, 419))

    do{
	pygame.draw.line(okno(255,255,0), (286,430), (429,430));
	d++;
	e--;
	g++;
	h--;
}while(d!=wartosc docelowa && e!=wartosc docelowa && f!=wartosc docelowa && g!=wartosc docelowa);



    pygame.display.update()

    class ChinczykGame(object):  # łączy wszystkie elementy w całośc
        def __init__(self, width, height):
            pygame.init()
            self.board = Board(width, height)
            # zegar którego użyjemy do kontrolowania szybkości rysowania
            # kolejnych klatek gry
            self.fps_clock = pygame.time.Clock()


    def run(self):
        """
        Główna pętla programu
        """
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.board.draw()
            self.fps_clock.tick(30)


    def handle_events(self):
        """
        Obsługa zdarzeń systemowych, tutaj zinterpretujemy np. ruchy myszką
        :return True jeżeli pygame przekazał zdarzenie wyjścia z gry
        """
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                return True

# Ta część powinna być zawsze na końcu modułu (ten plik jest modułem)
# chcemy uruchomić naszą grę dopiero po tym jak wszystkie klasy zostaną zadeklarowane
if __name__ == "__main__":
    game = ChinczykGame(800, 400)
    game.run()
board = Board(800, 400)
board.draw()