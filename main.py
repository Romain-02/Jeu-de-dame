import pygame
import random
import time
pygame.init()

pygame.display.set_caption('Jeu de dame')
screen = pygame.display.set_mode((1372, 950))
bouton = pygame.image.load('bouton bleu.png')
carre_vert = pygame.image.load('carre vert.png')
carre_vert = pygame.transform.scale(carre_vert, (98, 95))
rond_bleu = pygame.image.load('rond bleu.png')
rond_bleu = pygame.transform.scale(rond_bleu, (45, 45))
bouton1 = pygame.transform.scale(bouton, (500, 200))
bouton2 = pygame.transform.scale(bouton, (501, 200))
ecran_gris = pygame.image.load('écran gris.jpg')
ecran_gris = pygame.transform.scale(ecran_gris, (1000, 1000))
ecran_jaune = pygame.image.load('fond jaune.jpg')
ecran_jaune = pygame.transform.scale(ecran_jaune, (1000, 1000))
ecran_gris2 = pygame.transform.scale(ecran_gris, (98, 95))
background = pygame.image.load('Jeu-de-Dames_01.png')
jeton_rouge = pygame.image.load('jeton rouge.png')
jeton_rouge = pygame.transform.scale(jeton_rouge, (150, 150))
jeton_rouge2 = pygame.transform.scale(jeton_rouge, (95, 95))
jeton_noir = pygame.image.load('jeton noir.png')
jeton_noir = pygame.transform.scale(jeton_noir, (150, 150))
jeton_noir2 = pygame.transform.scale(jeton_noir, (95, 95))
jeton_rouge3 = pygame.image.load('jeton rouge2.png')
jeton_rouge4 = pygame.transform.scale(jeton_rouge3, (95, 95))
jeton_noir3 = pygame.image.load('jeton noir2.png')
jeton_noir4 = pygame.transform.scale(jeton_noir3, (95, 95))
background = pygame.transform.scale(background, (972, 950))
police = pygame.font.SysFont("monospace", 25)
compteur_rouge = 0
compteur_noir  = 0
compt_rouge = police.render(str(compteur_noir), 1, (0, 0, 255))
compt_r = pygame.transform.scale(compt_rouge, (60, 110))
compt_noir = police.render(str(compteur_noir), 1, (0, 0, 255))
compt_n = pygame.transform.scale(compt_noir, (60, 110))
matrice = [[0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0, 2, 0], [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0], [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]
dico_coord = {'y0' :0, 'y1' : 97, 'y2' : 194, 'y3' : 291, 'y4' : 389, 'y5' : 486, 'y6' : 583, 'y7' : 680, 'y8' : 778, 'y9' : 875,
              'x0' : 0, 'x1' : 95, 'x2' : 190, 'x3' : 285, 'x4' : 380, 'x5' : 475, 'x6' : 570, 'x7' : 665, 'x8' : 760, 'x9' : 855}
dico_inverse = {}
for key in dico_coord.keys():
    dico_inverse[str(dico_coord[key])] = key
dico_carre = {'x0' : 0, 'x1' : 98, 'x2' : 196, 'x3' : 294, 'x4' : 392, 'x5' : 490, 'x6' : 588, 'x7' : 686, 'x8' : 784, 'x9' : 882,
             'y0' : 0, 'y1' : 95, 'y2' : 190, 'y3' : 285, 'y4' : 380, 'y5' : 475, 'y6' : 570, 'y7' : 665, 'y8' : 760, 'y9' : 855}
dico_inverse_c1 = {}
dico_inverse_c2 = {}
for key in dico_carre.keys():
    if key[0] == 'x':
        dico_inverse_c1[str(dico_carre[key])] = key
    else:
        dico_inverse_c2[str(dico_carre[key])] = key
class Jeton():
    def __init__(self, coul, rect = (0, 0, 0, 0), en_jeu = True, num = 0):
        self.coul = coul
        if self.coul == 1:
            self.image = jeton_rouge2
        elif self.coul == 2:
            self.image = jeton_noir2
        elif self.coul == 3:
            self.image = jeton_rouge4
        else:
            self.image = jeton_noir4
        self.rect = rect
        self.coord = (rect[0], rect[1])
        self.en_jeu = en_jeu
        self.num = num

class Jeu():
    def __init__(self, jetons, matrice = [[0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2, 0, 2], [2, 0, 2, 0, 2, 0, 2, 0, 2, 0], [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0], [0, 0, 0, 0, 0 ,0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]):
        self.jetons = jetons
        self.matrice = matrice

def déplacement_possible(cord, matrice):
    déplacements = []
    x = cord[0]
    y = cord[1]
    coul = matrice[y][x]
    if coul == 1 or coul == 3:
        a = '013'
    else:
        a = '024'
    if coul == 1:  #rouge
        if x == 0:
            if matrice[y-1][x+1] == 0:
                déplacements.append((y - 1, x + 1))
        elif x == 9:
            if matrice[y-1][x-1] == 0:
                déplacements.append((y - 1, x - 1))
        else:
            if matrice[y - 1][x + 1] == 0:
                déplacements.append((y - 1, x + 1))
            if matrice[y - 1][x - 1] == 0:
                déplacements.append((y - 1, x - 1))
    elif coul == 2:
        if x == 0:
            if matrice[y+1][x+1] == 0:
                déplacements.append((y + 1, x + 1))
        elif x == 9:
            if matrice[y+1][x-1] == 0:
                déplacements.append((y + 1, x - 1))
        else:
            if matrice[y + 1][x + 1] == 0:
                déplacements.append((y + 1, x + 1))
            if matrice[y + 1][x - 1] == 0:
                déplacements.append((y + 1, x - 1))
    else:
        if coul == 3:
            coul = 1
        elif coul == 4:
            coul = 2
        x1 = x
        y1 = y
        x += 1
        y += 1
        while x < 10 and y < 10 and matrice[y][x] != coul and not (str(matrice[y][x]) not in a and str(matrice[y-1][x-1]) not in a):
            if matrice[y][x] == 0:
                déplacements.append((y, x))
            x += 1
            y += 1
        x = x1 + 1
        y = y1 - 1
        while x < 10 and y > -1 and matrice[y][x] != coul and not (str(matrice[y][x]) not in a and str(matrice[y+1][x-1]) not in a):
            if matrice[y][x] == 0:
                déplacements.append((y, x))
            x += 1
            y -= 1
        x = x1 - 1
        y = y1 - 1
        while y > -1 and x > -1 and matrice[y][x] != coul and not (str(matrice[y][x]) not in a and str(matrice[y+1][x+1]) not in a):
            if matrice[y][x] == 0:
                déplacements.append((y, x))
            x -= 1
            y -= 1
        x = x1 - 1
        y = y1 + 1
        while x > -1 and y < 10 and matrice[y][x] != coul and not (str(matrice[y][x]) not in a and str(matrice[y-1][x+1]) not in a):
            if matrice[y][x] == 0:
                déplacements.append((y, x))
            x -= 1
            y += 1
        x = x1
        y = y1
    b = déplacements_prendre_jeton((cord[0], cord[1]), matrice)
    for coord in b:
        déplacements.append(coord)
    return déplacements

def déplacements_prendre_jeton(cord, matrice):
    déplacements = []
    x = cord[0]
    y = cord[1]
    coul = matrice[y][x]
    if coul == 1 or coul == 3:
        a = '013'
    else:
        a = '024'
    if coul == 1 or coul == 2:
        if x < 8 and y < 8:
            if str(matrice[y+1][x+1]) not in a and matrice[y+2][x+2] == 0:
                déplacements.append(((y+2, x+2), (y+1, x+1)))
        if y > 1 and x < 8:
            if str(matrice[y-1][x+1]) not in a and matrice[y-2][x+2] == 0:
                déplacements.append(((y-2, x+2), (y-1, x+1)))
        if x > 1 and y < 8:
            if str(matrice[y+1][x-1]) not in a and matrice[y+2][x-2] == 0:
                déplacements.append(((y+2, x-2), (y+1, x-1)))
        if y > 1 and x > 1:
            if str(matrice[y-1][x-1]) not in a and matrice[y-2][x-2] == 0:
                déplacements.append(((y-2, x-2), (y-1, x-1)))
    else:
        x1 = x
        y1 = y
        while x < 8 and y < 8 and not (str(matrice[y+2][x+2]) not in a and str(matrice[y+1][x+1]) not in a):
            if str(matrice[y+1][x+1]) not in a and matrice[y+2][x+2] == 0:
                déplacements.append(((y+1, x+1), ('+', '+')))
            x += 1
            y += 1
        x = x1
        y = y1
        while x < 8 and y > 1 and not (str(matrice[y-2][x+2]) not in a and str(matrice[y-1][x+1]) not in a):
            if str(matrice[y-1][x+1]) not in a and matrice[y-2][x+2] == 0:
                déplacements.append(((y-1, x+1), ('-', '+')))
            x += 1
            y -= 1
        x = x1
        y = y1
        while y > 1 and x > 1 and not (str(matrice[y-2][x-2]) not in a and str(matrice[y-1][x-1]) not in a):
            if str(matrice[y-1][x-1]) not in a and matrice[y-2][x-2] == 0:
                déplacements.append(((y-1, x-1), ('-', '-')))
            x -= 1
            y -= 1
        x = x1
        y = y1
        while x > 1 and y < 8 and not (str(matrice[y+2][x-2]) not in a and str(matrice[y+1][x-1]) not in a):
            if str(matrice[y+1][x-1]) not in a and matrice[y+2][x-2] == 0:
                déplacements.append(((y+1, x-1), ('+', '-')))
            x -= 1
            y += 1
        x = x1
        y = y1
    return déplacements

def déplacer_jeton(cord1, cord2, matrice, compteurs):
    change2 = False
    coul = matrice[cord1[1]][cord1[0]]
    temporaire = déplacement_possible(cord1, matrice)
    coord_3 = []
    coord_2 = []
    coord_1 = []
    z = (cord1[1], cord1[0])
    for elt in temporaire:
        if type(elt[0]) == int:
            coord_1.append(elt)
        elif type(elt[1][1]) == str:
            coord_3.append(elt)
        else:
            coord_2.append(elt)
    if cord2 in coord_1:
        if len(coord_3) != 0:
            for cord3 in coord_3:
                x = cord3[0][0]
                y = cord3[0][1]
                while x < 9 and y < 9 and x > 0 and y > 0:
                    x = x + int(cord3[1][0] + '1')
                    y = y + int(cord3[1][1] + '1')
                    if (x, y) == cord2 and not change2:
                        compteurs = compteur((cord3[0][0],cord3[0][1]), matrice, compteurs[0], compteurs[1])
                        matrice[cord1[1]][cord1[0]] = 0
                        matrice[cord3[0][0]][cord3[0][1]] = 0
                        matrice[cord2[0]][cord2[1]] = coul
                        z = (cord2[0], cord2[1])
                        change2 = True
        if not change2:
            matrice[cord1[1]][cord1[0]] = 0
            matrice[cord2[0]][cord2[1]] = coul
            z = (cord2[0], cord2[1])
    elif len(coord_2) != 0 and not change2:
        if type(coord_2[0][0]) == int:
            if cord2 in coord_2[0]:
                matrice[coord_2[0][0]][coord_2[0][1]] = coul
                matrice[cord1[1]][cord1[0]] = 0
                compteurs = compteur((coord_2[1][0], coord_2[1][1]), matrice, compteurs[0], compteurs[1])
                matrice[coord_2[1][0]][coord_2[1][1]] = 0
                z = (coord_2[0][0], coord_2[0][1])
        else:
            for c in coord_2:
                if cord2 in c:
                    matrice[c[0][0]][c[0][1]] = coul
                    compteurs = compteur((c[1][0], c[1][1]), matrice, compteurs[0], compteurs[1])
                    matrice[cord1[1]][cord1[0]] = 0
                    matrice[c[1][0]][c[1][1]] = 0
                    z = (c[0][0], c[0][1])
    matrice = mettre_dame(z, matrice)
    return (matrice, compteurs)

def cases_possibles(cord, matrice):
    temporaire = déplacement_possible(cord, matrice)
    coord_1 = []
    for elt in temporaire:
        if type(elt[0]) == int:
            coord_1.append(elt)
        elif type(elt[1][1]) != str:
            coord_1.append(elt[0])
    return coord_1

def compteur(coord, matrice, comp_r, comp_n):
    if matrice[coord[0]][coord[1]] == 1:
        comp_n += 1
    elif matrice[coord[0]][coord[1]] == 2:
        comp_r += 1
    elif matrice[coord[0]][coord[1]] == 3:
        comp_n += 2
    else:
        comp_r += 2
    return (comp_r, comp_n)

def prendre_possible(matrice, coord):
    dep = déplacement_possible(coord, matrice)
    for d in dep:
        if type(d[0]) == tuple and type(d[1][1]) == int:
            return True
    return False

def mettre_dame(pion, matrice):
    if matrice[pion[0]][pion[1]] == 1:
        if pion[0] == 0:
            matrice[pion[0]][pion[1]] = 3
    elif matrice[pion[0]][pion[1]] == 2:
        if pion[0] == 9:
            matrice[pion[0]][pion[1]] = 4
    return matrice

def liste_coord(matrice, coul):
    tab = []
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == coul:
                tab.append((i, j))
    return tab

def random_coord(liste):
    liste2 = []
    for _ in range(5):
        random.shuffle(liste)
    for i in range(9, -1, -1):
        for l in liste:
            if l[0] == i:
                liste2.append(l)
    return liste2


def affichage_mat(matrice):
    for ligne in matrice:
        print(ligne)
        print(end="")

def cherhcer_coord(jeton):
    return (dico_inverse[str(jeton.rect.x)], dico_inverse[str(jeton.rect.y)])

def deplacer_bot(matrice, compteurs):
    time.sleep(0.1)
    change = False
    pion = liste_coord(matrice, 2)
    while len(pion) != 0 and not change:
        pion = random_coord(pion)
        (j, i) = pion.pop()
        if change:
            return (matrice, compteurs)
        #avoir une dame
        if len(cases_possibles((i, j), matrice)) == 1 and cases_possibles((i, j), matrice)[0] == 9 and change == False:
            (matrice, compteurs) = (déplacer_jeton((i,j), cases_possibles((i, j), matrice), matrice, compteurs)[0], déplacer_jeton((i,j), cases_possibles((i, j), matrice), matrice, compteurs)[1])
            change = True
        else:
            for c in cases_possibles((i, j), matrice):
                if c[0] == 9 and change == False:
                    (matrice, compteurs) = (déplacer_jeton((i,j), c, matrice, compteurs)[0], déplacer_jeton((i,j), c, matrice, compteurs)[1])
                    change = True
    if not change:
        (change, matrice, compteurs, aa) = bot_prendre(matrice, compteurs)
    #protéger un pion
    if not change:
        pion = liste_coord(matrice, 2)
        while len(pion) != 0 and not change:
            pion = random_coord(pion)
            (j, i) = pion.pop()
            if change:
                return (matrice, compteurs)
            if matrice[i][j] == 1 and not change:  # si c'est un pion noir
                for elt in déplacement_possible((i, j), matrice):
                        if type(elt[0]) == tuple and type(elt[1][1]) == int:
                            for x in range(len(matrice)):
                                for y in range(len(matrice)):
                                    if matrice[x][y] == 2 and (elt[1][0], elt[1][1]) in cases_possibles((x, y), matrice) and not change:
                                        (matrice, compteurs) = (déplacer_jeton((elt[1][0], elt[1][1]), (x, y), matrice, compteurs)[0], déplacer_jeton((elt[1][0], elt[1][1]), (x, y), matrice, compteurs)[1])
                                        change = True
    #avancé un pion au hasard
    if not change:
        pion = liste_coord(matrice, 2)
        while len(pion) != 0 and not change:
            pion = random_coord(pion)
            (j, i) = pion.pop()
            if change:
                return (matrice, compteurs)
            if matrice[i][j] == 2 and not change:
                if len(cases_possibles((i, j), matrice)) >= 1:
                    if len(cases_possibles((i, j), matrice)) == 1:
                        (matrice, compteurs) = déplacer_jeton((i, j), cases_possibles((i, j), matrice)[0], matrice, compteurs)
                        change = True
                    else:
                        (matrice, compteurs) = déplacer_jeton((i, j), cases_possibles((i, j), matrice)[0], matrice, compteurs)
                        change = True
    return (matrice, compteurs, aa)

def bot_prendre(matrice, compteurs):
    aa = False
    change = False
    pion = liste_coord(matrice, 2)
    while len(pion) != 0 and not change:
        pion = random_coord(pion)
        (j, i) = pion.pop()
        if change:
            return (matrice, compteurs)
            # prendre un pion
        if matrice[i][j] == 2 and not change:  # si c'est un pion noir
            for elt in déplacement_possible((i, j), matrice):
                if type(elt[0]) == tuple and type(elt[1][1]) == int:
                    n_case = elt[0]
                    matrice = déplacer_jeton((i, j), n_case, matrice, compteurs)[0]
                    while prendre_possible(matrice, (n_case[1], n_case[0])):
                        for elt in déplacement_possible((n_case[1], n_case[0]), matrice):
                            if type(elt[0]) == tuple and type(elt[1][1]) == int:
                                a_case = (n_case[1], n_case[0])
                                n_case = elt[0]
                                for jetons in Jeton_game:
                                    if jetons.en_jeu:
                                        screen.blit(jetons.image, jetons.rect)
                                time.sleep(0.1)
                                matrice = déplacer_jeton(a_case, n_case, matrice, compteurs)[0]
                    change = True
                    aa = True
    return (change, matrice, compteurs, aa)

carrés = []
c = 0
d = 0
for i in range(10):
    for j in range (10):
        rect2 = ecran_gris2.get_rect()
        rect2.x = c
        rect2.y = d
        carrés.append((ecran_gris2, rect2))
        c += 98
    d += 95
    c = 0

Jeton_game = []
Jeu = Jeu(Jeton_game, matrice)
running = True
jeton_der = []
compteur_rouge = 0
compteur_noir  = 0
Partie_bot = False
Partie_2 = False
Interface = True
Interface2 = False
play = pygame.image.load('play.png')
play_rect = play.get_rect()
play_rect.x = 400
play_rect.y = 400
bouton1_rect = bouton1.get_rect()
bouton2_rect = bouton2.get_rect()
bouton1_rect.x = 786
bouton1_rect.y = 373
bouton2_rect.x = 100
bouton2_rect.y = 373
background2 = pygame.transform.scale(background, (1523, 1356))
ronds = []
aa = False
click = False
tour_nb = 0
if random.randint(1, 2) == 2:
    tour = [0, 1]
    tour_nb = 1
else:
    tour = [0, 2]
    tour_nb = 2

while running:
    if Interface:
        screen.blit(background2, (0, 0))
        texte1 = 'Jouer contre l\'ordinateur'
        texte2 = 'Jouer avec un ami'
        if not click:
            screen.blit(play, (play_rect))
        else:
            texte_a = police.render(str(texte1), 1, (255, 255, 0))
            texte_a2 = police.render(str(texte2), 1, (255, 255, 0))
            texte_a = pygame.transform.scale(texte_a, (350, 72))
            texte_a2 = pygame.transform.scale(texte_a2, (275, 72))
            screen.blit(bouton1, (786, 373))
            screen.blit(bouton2, (100, 373))
            screen.blit(texte_a, (165, 431))
            screen.blit(texte_a2, (884, 431))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not click:
                    if play_rect.collidepoint(event.pos):
                        click = True
                elif bouton1_rect.collidepoint(event.pos):
                    Interface = False
                    Partie_2 = True
                    click = False
                elif bouton2_rect.collidepoint(event.pos):
                    Interface = False
                    Partie_bot = True
                    click = False
    if Partie_2:
        if tour[1] == 1:
            tour = ('Au tour des noirs', 1)
        else:
            tour = ('Au tour des rouges', 2)
        compt_rouge = police.render(str(compteur_rouge), 0, (0, 0, 255))
        compt_r = pygame.transform.scale(compt_rouge, (60, 110))
        compt_noir = police.render(str(compteur_noir), 0, (0, 0, 255))
        compt_n = pygame.transform.scale(compt_noir, (60, 110))
        Jeton_game = []
        tab = []
        affiche_tour = police.render(tour[0], 0, (0, 0, 255))
        affiche_tour = pygame.transform.scale(affiche_tour, (380, 40))
        for i in range(len(Jeu.matrice)):
            for j in range(len(Jeu.matrice[i])):
                if Jeu.matrice[i][j] != 0:
                    tab.append(((dico_coord['y' + str(j)], dico_coord['x' + str(i)]), Jeu.matrice[i][j]))
        i = 0
        for i in range(len(tab)):
            Jeton_game.append(Jeton(tab[i][1]))
            rect = Jeton_game[i].image.get_rect()
            rect.x = tab[i][0][0]
            rect.y = tab[i][0][1]
            i += 1
            Jeton_game[-1].rect = rect
            Jeton_game[-1].coord = (rect[0], rect[1])
        for carré in carrés:
            screen.blit(carré[0], carré[1])
        screen.blit(ecran_jaune, (500, 0))
        screen.blit(background, (0, 0))
        screen.blit(compt_r, (1225, 660))
        screen.blit(compt_n, (1225, 220))
        screen.blit(jeton_rouge, (1062, 199))
        screen.blit(jeton_noir, (1062, 637))
        screen.blit(affiche_tour, (980, 500))
        if jeton_der != []:
            ronds = []
            screen.blit(carre_vert, (jeton_der.coord[0], jeton_der.coord[1]))
            dep = déplacement_possible((int(dico_inverse[str(jeton_der.coord[0])][1]), int(dico_inverse[str(jeton_der.coord[1])][1])), Jeu.matrice)
            for elt in dep:
                if type(elt[0]) == int:
                    ronds.append(elt)
                elif not type(elt[1][1]) == str:
                    ronds.append(elt[0])
        for r in ronds:
            screen.blit(rond_bleu, (dico_carre['x' + str(r[1])] + 22.5, dico_carre['y' + str(r[0])]+25))
        for jetons in Jeton_game:
            if jetons.en_jeu:
                screen.blit(jetons.image, jetons.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for jetons in Jeton_game:
                    if jetons != jeton_der and jetons.coul != tour[1]:
                        if jetons.rect.collidepoint(event.pos):
                            jeton_der = jetons
                if jeton_der != [] and not jeton_der.rect.collidepoint(event.pos):
                    for carré in carrés:
                        if carré[1].collidepoint(event.pos) and (int(dico_inverse_c2[str(carré[1][1])][1:]), int(dico_inverse_c1[str(carré[1][0])][1:])) in cases_possibles((int(dico_inverse[str(jeton_der.coord[0])][1]), int(dico_inverse[str(jeton_der.coord[1])][1])), Jeu.matrice):
                            (Jeu.matrice, (compteur_rouge, compteur_noir)) = déplacer_jeton((int(dico_inverse[str(jeton_der.coord[0])][1]), int(dico_inverse[str(jeton_der.coord[1])][1])), (int(dico_inverse_c2[str(carré[1][1])][1:]), int(dico_inverse_c1[str(carré[1][0])][1:])), Jeu.matrice, (compteur_rouge, compteur_noir))
                            ronds = []
                            if tour[1] == 1:
                                tour = ('Au tour des rouges', 2)
                            else:
                                tour = ('Au tour des noirs', 1)
                            if compteur_rouge == 20 or compteur_noir == 20:
                                Partie_2 = False
                                Interface2 = True
                            jeton_der = []
    if Partie_bot:
        time.sleep(0.01)
        compteurs = (0, 0)
        compt_rouge = police.render(str(20 - len(liste_coord(Jeu.matrice, 2))), 0, (0, 0, 255))
        compt_r = pygame.transform.scale(compt_rouge, (60, 110))
        compt_noir = police.render(str(20 - len(liste_coord(Jeu.matrice, 1))), 0, (0, 0, 255))
        compt_n = pygame.transform.scale(compt_noir, (60, 110))
        Jeton_game = []
        tab = []
        for i in range(len(Jeu.matrice)):
            for j in range(len(Jeu.matrice[i])):
                if Jeu.matrice[i][j] != 0:
                    tab.append(((dico_coord['y' + str(j)], dico_coord['x' + str(i)]), Jeu.matrice[i][j]))
        i = 0
        for i in range(len(tab)):
            Jeton_game.append(Jeton(tab[i][1]))
            rect = Jeton_game[i].image.get_rect()
            rect.x = tab[i][0][0]
            rect.y = tab[i][0][1]
            i += 1
            Jeton_game[-1].rect = rect
            Jeton_game[-1].coord = (rect[0], rect[1])
        for carré in carrés:
            screen.blit(carré[0], carré[1])
        screen.blit(ecran_jaune, (500, 0))
        screen.blit(background, (0, 0))
        screen.blit(compt_r, (1225, 660))
        screen.blit(compt_n, (1225, 220))
        screen.blit(jeton_rouge, (1062, 199))
        screen.blit(jeton_noir, (1062, 637))
        if tour_nb == 1 and not aa:
            tour = ('Au tour des rouges', 1)
        if tour_nb == 2 or aa:
            tour = ('Attendez pour jouer', 2)
        affiche_tour = police.render(tour[0], 0, (0, 0, 255))
        affiche_tour = pygame.transform.scale(affiche_tour, (380, 40))
        screen.blit(affiche_tour, (980, 500))
        if jeton_der != [] and jeton_der != 'test' and tour[1] == 1:
            screen.blit(carre_vert, (jeton_der.coord[0], jeton_der.coord[1]))
            dep = déplacement_possible((int(dico_inverse[str(jeton_der.coord[0])][1]), int(dico_inverse[str(jeton_der.coord[1])][1])), Jeu.matrice)
            for elt in dep:
                if type(elt[0]) == int:
                    ronds.append(elt)
                elif not type(elt[1][1]) == str:
                    ronds.append(elt[0])
        for r in ronds:
            screen.blit(rond_bleu, (dico_carre['x' + str(r[1])] + 22.5, dico_carre['y' + str(r[0])]+25))
        for jetons in Jeton_game:
            if jetons.en_jeu:
                screen.blit(jetons.image, jetons.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if aa:
                jeton_der = 'test'
                time.sleep(0.5)
                (change, matrice, compteurs, aa) = bot_prendre(matrice, compteurs)
                jeton_der = []
            elif tour[1] == 2:
                print(jeton_der)
                jeton_der = 'test'
                time.sleep(6)
                print(jeton_der)
                (Jeu.matrice, (compteur_rouge, compteur_noir), aa) = deplacer_bot(Jeu.matrice, (compteur_rouge, compteur_noir))
                tour = ((), 0)
                tour_nb = 1
            elif event.type == pygame.MOUSEBUTTONDOWN and tour[0] == 'Au tour des rouges':
                print(jeton_der)
                for jetons in Jeton_game:
                    if jeton_der == []  or jetons.coord != jeton_der.coord and jetons.coul == 1:
                        if jetons.rect.collidepoint(event.pos):
                            jeton_der = jetons
                            ronds = []
                    elif jeton_der != [] and jeton_der != 'test' and jetons.coord == jeton_der.coord and jetons.coul == 1:
                        if jetons.rect.collidepoint(event.pos):
                            jeton_der = []
                            ronds = []
                if jeton_der != [] and jeton_der != 'test' and not jeton_der.rect.collidepoint(event.pos) and jetons.coul == 1:
                    for carré in carrés:
                        if carré[1].collidepoint(event.pos) and (int(dico_inverse_c2[str(carré[1][1])][1:]), int(dico_inverse_c1[str(carré[1][0])][1:])) in cases_possibles((int(dico_inverse[str(jeton_der.coord[0])][1]), int(dico_inverse[str(jeton_der.coord[1])][1])), Jeu.matrice):
                            (Jeu.matrice, (compteur_rouge, compteur_noir)) = déplacer_jeton((int(dico_inverse[str(jeton_der.coord[0])][1]), int(dico_inverse[str(jeton_der.coord[1])][1])), (int(dico_inverse_c2[str(carré[1][1])][1:]), int(dico_inverse_c1[str(carré[1][0])][1:])), Jeu.matrice, (compteur_rouge, compteur_noir))
                            ronds = []
                            tour = ((), 0)
                            tour_nb = 2
                            affichage_mat(Jeu.matrice)
                            if compteur_rouge == 20 or compteur_noir == 20:
                                Partie_bot = False
                                Interface2 = True
                            jeton_der = []
        if jeton_der == 'test':
            jeton_der = []
    if Interface2:
        screen.blit(background2, (0, 0))
        texte = 'La partie est finie'
        texte_a = police.render(str(texte), 0, (0, 0, 255))
        texte_a = pygame.transform.scale(texte_a, (60, 110))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Interface = False
                Partie_bot = True



    pygame.display.flip()

pygame.quit()

