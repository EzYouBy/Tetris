#Un tétris avec un système de niveau,pseudo etc.
#1100 par 1400 avec 300 a gauche et a droite et 150 en bas et en haut   792(H)  sur 360(L) avec 36 par 36 chaque carreau    220 à gauche et a droite soit 800  14 en haut en en bas soit 820 first 221 14 # faire pop en 625,7 128
from time import *
import sys
import pygame
import random
from pygame.locals import *

pygame.mixer.init() #je lance la musique
pygame.mixer.music.load("musique.mp3") # import du fichier
pygame.mixer.music.play() # on joue le fichier
pygame.mixer.music.set_volume(0.6) # réglage du volume
pygame.init()

fenetre = pygame.display.set_mode((800, 820)) #défini ma fenêtre et load toutes mes images
grillejeu = pygame.image.load("images/grillerefaite.jpg")
carrebleufonce = pygame.image.load("images/carrebleufonce 1.jpg")
carrebleu = pygame.image.load("images/carrebleu1.jpg")
carrejaune = pygame.image.load("images/carrejaune1.jpg")
carreorange = pygame.image.load("images/carreorange1.jpg")
carrerouge = pygame.image.load("images/carrerouge1.jpg")
carrevert = pygame.image.load("images/carrevert1.jpg")
carreviolet = pygame.image.load("images/carreviolet1.jpg")
carreblanc = pygame.image.load("images/carreblanc.jpg")
recnext = pygame.image.load("images/recnext.jpg")
reclevel = pygame.image.load("images/reclevel.jpg")
recscore = pygame.image.load("images/recscore.jpg")
pageacceuil = pygame.image.load("images/pageacceuil.jpg")
myfont = pygame.font.SysFont("monospace", 25)
sonon = pygame.image.load("images/sonon.jpg")
sonoff = pygame.image.load("images/sonmute.jpg")
pageparametre = pygame.image.load("images/pageparametre.jpg")
clock = pygame.time.Clock()

class jeu :

        def __init__(self,plateau,x,y,postourne,posepieces,listeligne,lignecomplet,point,level,time,pieceatt,switchson):
                self.plateau = plateau
                self.x = x
                self.y = y
                self.postourne = postourne
                self.posepieces = posepieces
                self.listeligne = listeligne
                self.lignecomplet = lignecomplet
                self.point = point
                self.lvl = level
                self.time = time
                self.pieceatt = pieceatt
                self.switchson = switchson

        def classement (self): #cette fonction défini mon classement et l'actualise
            switch = 0
            with open("fichierscore.txt") as f:
                top1 = f.readlines()[0]
            with open("fichierscore.txt") as f:
                top2 = f.readlines()[1]
            with open("fichierscore.txt") as f:
                top3 = f.readlines()[2]
            with open("fichierscore.txt") as f:
                top4 = f.readlines()[3]
            with open("fichierscore.txt") as f:
                top5 = f.readlines()[4]
            f.close()
            fichierclass = open("fichierscore.txt","w")
            if self.point > int(top5,base=0):
                if self.point>int(top4,base=0):
                    if self.point>int(top3,base=0):
                        if self.point>int(top2,base=0):
                            if self.point>int(top1,base=0):
                                top1,top2,top3,top4,top5 =self.point,top1,top2,top3,top4
                                fichierclass.write(str(top1)+"\n")
                                fichierclass.write(str(top2))
                                fichierclass.write(str(top3))
                                fichierclass.write(str(top4))
                                fichierclass.write(str(top5))
                                switch = 5
                            else :
                                top2,top3,top4,top5 = self.point,top2,top3,top4
                                fichierclass.write(str(top1))
                                fichierclass.write(str(top2)+"\n")
                                fichierclass.write(str(top3))
                                fichierclass.write(str(top4))
                                fichierclass.write(str(top5))
                                switch = 4
                        else:
                            top3,top4,top5 = self.point,top3,top4
                            fichierclass.write(str(top1))
                            fichierclass.write(str(top2))
                            fichierclass.write(str(top3)+"\n")
                            fichierclass.write(str(top4))
                            fichierclass.write(str(top5))
                            switch = 3
                    else:
                        top4,top5 = self.point,top4
                        fichierclass.write(str(top1))
                        fichierclass.write(str(top2))
                        fichierclass.write(str(top3))
                        fichierclass.write(str(top4)+"\n")
                        fichierclass.write(str(top5))
                        switch = 2
                else :
                    top5 = self.point
                    fichierclass.write(str(top1))
                    fichierclass.write(str(top2))
                    fichierclass.write(str(top3))
                    fichierclass.write(str(top4))
                    fichierclass.write(str(top5))
                    switch = 1
            else :
                fichierclass.write(str(top1))
                fichierclass.write(str(top2))
                fichierclass.write(str(top3))
                fichierclass.write(str(top4))
                fichierclass.write(str(top5))
            fichierclass.close()

            boucle = 1
            pseudo = ""
            with open("fichierpseudo.txt") as f:
                pseudo1 = f.readlines()[0]
            with open("fichierpseudo.txt") as f:
                pseudo2 = f.readlines()[1]
            with open("fichierpseudo.txt") as f:
                pseudo3 = f.readlines()[2]
            with open("fichierpseudo.txt") as f:
                pseudo4 = f.readlines()[3]
            with open("fichierpseudo.txt") as f:
                pseudo5 = f.readlines()[4]
            f.close()
            pseudo= go.entrerpseudo()
            fichierpseudo = open("fichierpseudo.txt","w")
            if switch == 1:
                fichierpseudo.write(pseudo1)
                fichierpseudo.write(pseudo2)
                fichierpseudo.write(pseudo3)
                fichierpseudo.write(pseudo4)
                fichierpseudo.write(pseudo)

            elif switch == 2:
                fichierpseudo.write(pseudo1)
                fichierpseudo.write(pseudo2)
                fichierpseudo.write(pseudo3)
                fichierpseudo.write(pseudo+"\n")
                fichierpseudo.write(pseudo4)

            elif switch == 3:
                fichierpseudo.write(pseudo1)
                fichierpseudo.write(pseudo2)
                fichierpseudo.write(pseudo+"\n")
                fichierpseudo.write(pseudo3)
                fichierpseudo.write(pseudo4)

            elif switch == 4:
                fichierpseudo.write(pseudo1)
                fichierpseudo.write(pseudo+"\n")
                fichierpseudo.write(pseudo2)
                fichierpseudo.write(pseudo3)
                fichierpseudo.write(pseudo4)

            elif switch == 5:
                fichierpseudo.write(pseudo+"\n")
                fichierpseudo.write(pseudo1)
                fichierpseudo.write(pseudo2)
                fichierpseudo.write(pseudo3)
                fichierpseudo.write(pseudo4)
            else :
                fichierpseudo.write(pseudo1)
                fichierpseudo.write(pseudo2)
                fichierpseudo.write(pseudo3)
                fichierpseudo.write(pseudo4)
                fichierpseudo.write(pseudo5)
            fichierpseudo.close()


        def updatepoint(self):
            fenetre.blit(recscore, (23,100))
            if self.lignecomplet == 1 : #se nomme un simple
                self.point = self.point + 60*self.lvl
            elif self.lignecomplet == 2 : #se nomme un double
                self.point = self.point + 100*self.lvl
            elif self.lignecomplet == 3: #se nomme un triple
                self.point = self.point + 300*self.lvl
            elif self.lignecomplet == 4: #se nomme un tétris
                self.point = self.point + 1200*self.lvl
            return self.point

        def updateniveau(self):
            testupdatelvl = 0
            if self.lvl == 1 :
                if self.point >= 1000:
                    self.lvl = 2
                    self.time = 0.42
                    testupdatelvl = 1
            elif self.lvl == 2 :
                if self.point >= 2000:
                    self.lvl = 3
                    self.time = 0.34
                    testupdatelvl = 1
            elif self.lvl == 3 :
                if self.point >= 4000:
                    self.lvl = 4
                    self.time = 0.28
                    testupdatelvl = 1
            elif self.lvl == 4 :
                if self.point >= 7000:
                    self.lvl = 5
                    self.time = 0.20
                    testupdatelvl = 1
            elif self.lvl == 5 :
                if self.point >= 11000:
                    self.lvl = 6
                    self.time = 0.12
                    testupdatelvl = 1
            elif self.lvl == 6 :
                if self.point >= 16000:
                    self.lvl = 7
                    self.time = 0.04
                    testupdatelvl = 1
            elif self.lvl == 7 :
                if self.point >= 22000:
                    self.lvl = 8
                    self.time = 0.01
                    testupdatelvl = 1
            elif self.lvl == 8 :
                if self.point >= 29000:
                    self.lvl = 9
                    self.time = 0.005
                    testupdatelvl = 1
            elif self.lvl == 9 :
                if self.point >= 37000:
                    self.lvl = 10
                    self.time = 0.002
                    testupdatelvl = 1
            elif self.lvl == 10 :
                if self.point >= 46000:
                    self.lvl = 11
                    self.time = 0.001
                    testupdatelvl = 1
            if testupdatelvl == 1:
                fenetre.blit(reclevel, (23,326))
                level= myfont.render(str(self.lvl), 1, (255,255,0))
                fenetre.blit(level, (100, 346))


        def afficher_plateau (self):
            for i in range (22):
                print ('|',self.plateau[i][0],'|',self.plateau[i][1],'|',self.plateau[i][2],'|',self.plateau[i][3],'|',self.plateau[i][4],'|',self.plateau[i][5],'|',self.plateau[i][6],'|',self.plateau[i][7],'|',self.plateau[i][8],'|',self.plateau[i][9],'|')

        def aléatoirepièce(self):
            fenetre.blit(recnext, (620,100))
            self.pieceatt = random.randint(1,7)
            if self.pieceatt == 1:
                fenetre.blit(carrebleu, (628, 146))
                fenetre.blit(carrebleu, (664, 146))
                fenetre.blit(carrebleu, (700, 146))
                fenetre.blit(carrebleu, (736, 146))
            elif self.pieceatt == 2:
                fenetre.blit(carrejaune, (663, 128))
                fenetre.blit(carrejaune, (663, 164))
                fenetre.blit(carrejaune, (699, 128))
                fenetre.blit(carrejaune, (699, 164))
            elif self.pieceatt == 3:
                fenetre.blit(carreviolet, (645, 128))
                fenetre.blit(carreviolet, (681, 128))
                fenetre.blit(carreviolet, (717, 128))
                fenetre.blit(carreviolet, (681, 164))
            elif self.pieceatt == 4:
                fenetre.blit(carreorange, (645, 128))
                fenetre.blit(carreorange, (681, 128))
                fenetre.blit(carreorange, (717, 128))
                fenetre.blit(carreorange, (645, 164))
            elif self.pieceatt == 5:
                fenetre.blit(carrebleufonce, (645, 128))
                fenetre.blit(carrebleufonce, (681, 128))
                fenetre.blit(carrebleufonce, (717, 128))
                fenetre.blit(carrebleufonce, (717, 164))
            elif self.pieceatt == 6:
                fenetre.blit(carrerouge, (645, 128))
                fenetre.blit(carrerouge, (681, 128))
                fenetre.blit(carrerouge, (681, 164))
                fenetre.blit(carrerouge, (717, 164))
            elif self.pieceatt == 7:
                fenetre.blit(carrevert, (645, 164))
                fenetre.blit(carrevert, (681, 164))
                fenetre.blit(carrevert, (681, 128))
                fenetre.blit(carrevert, (717, 128))

        def testligne(self):#a corriger
            if self.posepieces == 1:
                                variacouleur = 'b'
            elif self.posepieces == 2:
                                variacouleur = 'j'
            elif self.posepieces == 3:
                                variacouleur = 'vi'
            elif self.posepieces == 4:
                                variacouleur = 'o'
            elif self.posepieces == 5:
                                variacouleur = 'bf'
            elif self.posepieces == 6:
                                variacouleur = 'r'
            elif self.posepieces == 7:
                                variacouleur = 've'
            self.lignecomplet = 0
            lignecomplet = 0
            self.listeligne = []
            for i in range (22):
                varia = 0
                for j in range(10):
                    if self.plateau[i][j]!= variacouleur and self.plateau[i][j]!='bl':
                        varia +=1
                if varia ==10:
                        lignecomplet+=1
                        self.listeligne.append (i)
            self.lignecomplet = lignecomplet
            if lignecomplet >0:
                score = myfont.render(str(go.updatepoint()), 1, (255,255,0))
                fenetre.blit(score, (100, 120))
                go.updateniveau()
                return True

        def posepiece(self):
            self.posepieces = self.pieceatt
            go.aléatoirepièce()
            pygame.display.flip()
            if self.posepieces == 1:  #1111
                self.plateau[0][3] = 'b'
                self.plateau[0][4] = 'b'
                self.plateau[0][5] = 'b'
                self.plateau[0][6] = 'b'
                self.x = [0,0,0,0]
                self.y = [3,4,5,6]
                fenetre.blit(carrebleu,(329,14))
                fenetre.blit(carrebleu,(365,14))
                fenetre.blit(carrebleu,(401,14))
                fenetre.blit(carrebleu,(437,14))

            elif self.posepieces == 2:   #11
                self.plateau[0][4] = 'j' #11
                self.plateau[0][5] = 'j'
                self.plateau[1][4] = 'j'
                self.plateau[1][5] = 'j'
                self.x = [0,0,1,1]
                self.y = [4,5,4,5]
                fenetre.blit(carrejaune,(365,14))
                fenetre.blit(carrejaune,(401,14))
                fenetre.blit(carrejaune,(365,50))
                fenetre.blit(carrejaune,(401,50))

            elif self.posepieces == 3:      #111
                self.plateau[0][3] = 'vi'   #010
                self.plateau[0][4] = 'vi'
                self.plateau[0][5] = 'vi'
                self.plateau[1][4] = 'vi'
                self.x = [0,0,0,1]
                self.y = [3,4,5,4]
                fenetre.blit(carreviolet,(329,14))
                fenetre.blit(carreviolet,(365,14))
                fenetre.blit(carreviolet,(401,14))
                fenetre.blit(carreviolet,(365,50))

            elif self.posepieces == 4:    #111
                self.plateau[0][3] = 'o'  #100
                self.plateau[0][4] = 'o'
                self.plateau[0][5] = 'o'
                self.plateau[1][3] = 'o'
                self.x = [0,0,0,1]
                self.y = [3,4,5,3]
                fenetre.blit(carreorange,(329,14))
                fenetre.blit(carreorange,(365,14))
                fenetre.blit(carreorange,(401,14))
                fenetre.blit(carreorange,(329,50))

            elif self.posepieces == 5:    #111
                self.plateau[0][3] = 'bf' #001
                self.plateau[0][4] = 'bf'
                self.plateau[0][5] = 'bf'
                self.plateau[1][5] = 'bf'
                self.x = [0,0,0,1]
                self.y = [3,4,5,5]
                fenetre.blit(carrebleufonce,(329,14))
                fenetre.blit(carrebleufonce,(365,14))
                fenetre.blit(carrebleufonce,(401,14))
                fenetre.blit(carrebleufonce,(401,50))

            elif self.posepieces == 6:   #110
                self.plateau[0][3] = 'r' #011
                self.plateau[0][4] = 'r'
                self.plateau[1][4] = 'r'
                self.plateau[1][5] = 'r'
                self.x = [0,0,1,1]
                self.y = [3,4,4,5]
                fenetre.blit(carrerouge,(329,14))
                fenetre.blit(carrerouge,(365,14))
                fenetre.blit(carrerouge,(365,50))
                fenetre.blit(carrerouge,(401,50))

            elif self.posepieces == 7:    #011
                self.plateau[1][3] = 've' #110
                self.plateau[1][4] = 've'
                self.plateau[0][4] = 've'
                self.plateau[0][5] = 've'
                self.x = [1,1,0,0]
                self.y = [3,4,4,5]
                fenetre.blit(carrevert,(329,50))
                fenetre.blit(carrevert,(365,50))
                fenetre.blit(carrevert,(365,14))
                fenetre.blit(carrevert,(401,14))

        def tourne(self):
            if self.posepieces == 1:
                if self.postourne == 1:
                    if self.x[1] < 20:
                        if self.plateau[self.x[1]-1][self.y[1]] == 'bl' and self.plateau[self.x[1]+1][self.y[1]] == 'bl' and self.plateau[self.x[1]+2][self.y[1]] == 'bl':
                            self.plateau[self.x[1]-1][self.y[1]], self.plateau[self.x[1]+1][self.y[1]], self.plateau[self.x[1]+2][self.y[1]] = 'b','b','b'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1]-1,self.y[1]
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1]+1,self.y[1]
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]+2,self.y[1]
                            self.postourne = 2
                elif self.postourne == 2:
                    if self.y[1] > 0 and self.y[1] < 8:
                        if self.plateau[self.x[1]][self.y[1]-1] == 'bl' and self.plateau[self.x[1]][self.y[1]+1] == 'bl'and self.plateau[self.x[1]][self.y[1]+2] == 'bl':
                            self.plateau[self.x[1]][self.y[1]-1], self.plateau[self.x[1]][self.y[1]+1], self.plateau[self.x[1]][self.y[1]+2] = 'b','b','b'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1],self.y[1]-1
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1],self.y[1]+1
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1],self.y[1]+2
                            self.postourne = 1

            elif self.posepieces == 3:
                if self.postourne == 1:
                    if self.x[3] < 21:
                        if self.plateau[self.x[2]+1][self.y[2]] == 'bl' and self.plateau[self.x[2]+2][self.y[2]] == 'bl':
                                self.plateau[self.x[2]+1][self.y[2]], self.plateau[self.x[2]+2][self.y[2]] = 'vi','vi'
                                self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[2],self.y[2]
                                self.plateau[self.x[1]][self.y[1]],self.x[1],self.y[1] = 'bl',self.x[2]+1,self.y[2]
                                self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[2]+2,self.y[2]
                                self.postourne = 2
                elif self.postourne == 2:
                    if self.y[3] > 0:
                        if self.plateau[self.x[2]][self.y[2]-1] == 'bl' and self.plateau[self.x[2]][self.y[2]-2] == 'bl':
                                self.plateau[self.x[2]][self.y[2]-1], self.plateau[self.x[2]][self.y[2]-2] = 'vi','vi'
                                self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[2],self.y[2]
                                self.plateau[self.x[1]][self.y[1]],self.x[1],self.y[1] = 'bl',self.x[2],self.y[2]-1
                                self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[2],self.y[2]-2
                                self.postourne = 3
                elif self.postourne == 3:
                    if self.x[3] >0:
                        if self.plateau[self.x[2]-1][self.y[2]] == 'bl' and self.plateau[self.x[2]-2][self.y[2]] == 'bl':
                                self.plateau[self.x[2]-1][self.y[2]], self.plateau[self.x[2]-2][self.y[2]] = 'vi','vi'
                                self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[2],self.y[2]
                                self.plateau[self.x[1]][self.y[1]],self.x[1],self.y[1] = 'bl',self.x[2]-1,self.y[2]
                                self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[2]-2,self.y[2]
                                self.postourne = 4
                elif self.postourne == 4:
                    if self.y[3]<9:
                        if self.plateau[self.x[2]][self.y[2]+1] == 'bl' and self.plateau[self.x[2]][self.y[2]+2] == 'bl':
                                self.plateau[self.x[2]][self.y[2]+1], self.plateau[self.x[2]][self.y[2]+2] = 'vi','vi'
                                self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[2],self.y[2]
                                self.plateau[self.x[1]][self.y[1]],self.x[1],self.y[1] = 'bl',self.x[2],self.y[2]+1
                                self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[2],self.y[2]+2
                                self.postourne = 1

            elif self.posepieces == 4:
                if self.postourne == 1:
                    if self.plateau[self.x[1]+1][self.y[1]] == 'bl' and self.plateau[self.x[1]-1][self.y[1]] == 'bl'and self.plateau[self.x[1]-1][self.y[1]-1] == 'bl':
                        self.plateau[self.x[1]+1][self.y[1]], self.plateau[self.x[1]-1][self.y[1]], self.plateau[self.x[1]-1][self.y[1]-1] = 'o','o','o'
                        self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1]-1,self.y[1]
                        self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1]+1,self.y[1]
                        self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]-1,self.y[1]-1
                        self.postourne = 2
                elif self.postourne == 2:
                    if self.y[1]<9:
                        if self.plateau[self.x[1]][self.y[1]+1] == 'bl' and self.plateau[self.x[1]][self.y[1]-1] == 'bl'and self.plateau[self.x[1]-1][self.y[1]+1] == 'bl':
                            self.plateau[self.x[1]][self.y[1]+1], self.plateau[self.x[1]][self.y[1]-1], self.plateau[self.x[1]-1][self.y[1]+1] = 'o','o','o'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1],self.y[1]+1
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1],self.y[1]-1
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]-1,self.y[1]+1
                            self.postourne = 3
                elif self.postourne == 3:
                    if self.x[1]<21:
                        if self.plateau[self.x[1]+1][self.y[1]] == 'bl' and self.plateau[self.x[1]-1][self.y[1]] == 'bl'and self.plateau[self.x[1]+1][self.y[1]+1] == 'bl':
                            self.plateau[self.x[1]+1][self.y[1]], self.plateau[self.x[1]-1][self.y[1]], self.plateau[self.x[1]+1][self.y[1]+1] = 'o','o','o'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1]+1,self.y[1]
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1]-1,self.y[1]
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]+1,self.y[1]+1
                            self.postourne = 4
                elif self.postourne == 4:
                    if self.y[1]>0:
                        if self.plateau[self.x[1]][self.y[1]-1] == 'bl' and self.plateau[self.x[1]][self.y[1]+1] == 'bl'and self.plateau[self.x[1]+1][self.y[1]-1] == 'bl':
                            self.plateau[self.x[1]][self.y[1]-1], self.plateau[self.x[1]][self.y[1]+1], self.plateau[self.x[1]+1][self.y[1]-1] = 'o','o','o'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1],self.y[1]-1
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1],self.y[1]+1
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]+1,self.y[1]-1
                            self.postourne = 1

            elif self.posepieces == 5:
                if self.postourne == 1:
                    if self.x[1] >0:
                        if self.plateau[self.x[1]-1][self.y[1]] == 'bl' and self.plateau[self.x[1]+1][self.y[1]] == 'bl'and self.plateau[self.x[1]+1][self.y[1]-1] == 'bl':
                            self.plateau[self.x[1]-1][self.y[1]], self.plateau[self.x[1]+1][self.y[1]], self.plateau[self.x[1]+1][self.y[1]-1] = 'bf','bf','bf'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1]-1,self.y[1]
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1]+1,self.y[1]
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]+1,self.y[1]-1
                            self.postourne = 2
                elif self.postourne == 2:
                    if self.y[1]<9:
                        if self.plateau[self.x[1]][self.y[1]+1] == 'bl' and self.plateau[self.x[1]][self.y[1]-1] == 'bl'and self.plateau[self.x[1]-1][self.y[1]-  1] == 'bl':
                            self.plateau[self.x[1]][self.y[1]+1], self.plateau[self.x[1]][self.y[1]-1], self.plateau[self.x[1]-1][self.y[1]-1] = 'bf','bf','bf'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1],self.y[1]+1
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1],self.y[1]-1
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]-1,self.y[1]-1
                            self.postourne = 3
                elif self.postourne == 3:
                    if self.x[1]<21:
                        if self.plateau[self.x[1]+1][self.y[1]] == 'bl' and self.plateau[self.x[1]-1][self.y[1]] == 'bl'and self.plateau[self.x[1]-1][self.y[1]+1] == 'bl':
                            self.plateau[self.x[1]+1][self.y[1]], self.plateau[self.x[1]-1][self.y[1]], self.plateau[self.x[1]-1][self.y[1]+1] = 'bf','bf','bf'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1]+1,self.y[1]
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1]-1,self.y[1]
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]-1,self.y[1]+1
                            self.postourne = 4
                elif self.postourne == 4:
                    if self.y[1]>0:
                        if self.plateau[self.x[1]][self.y[1]-1] == 'bl' and self.plateau[self.x[1]][self.y[1]+1] == 'bl'and self.plateau[self.x[1]+1][self.y[1]+1] == 'bl':
                            self.plateau[self.x[1]][self.y[1]-1], self.plateau[self.x[1]][self.y[1]+1], self.plateau[self.x[1]+1][self.y[1]+1] = 'bf','bf','bf'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1],self.y[1]-1
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1],self.y[1]+1
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]+1,self.y[1]+1
                            self.postourne = 1

            elif self.posepieces == 6:
                if self.postourne == 1:
                    if self.x[1] >0:
                        if self.plateau[self.x[1]-1][self.y[1]] == 'bl' and self.plateau[self.x[1]+1][self.y[1]-1] == 'bl':
                            self.plateau[self.x[1]-1][self.y[1]], self.plateau[self.x[1]+1][self.y[1]-1] = 'r','r'
                            self.x[0],self.y[0] = self.x[1]-1,self.y[1]
                            self.plateau[self.x[2]][self.y[2]],self.x[2],self.y[2] = 'bl',self.x[1],self.y[1]-1
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]+1,self.y[1]-1
                            self.postourne = 2
                elif self.postourne == 2:
                    if self.y[1]<9:
                        if self.plateau[self.x[1]+1][self.y[1]] == 'bl' and self.plateau[self.x[1]+1][self.y[1]+1] == 'bl':
                            self.plateau[self.x[1]+1][self.y[1]], self.plateau[self.x[1]+1][self.y[1]+1] = 'r','r'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[1],self.y[1]-1
                            self.x[2],self.y[2] = self.x[1]+1,self.y[1]
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[1]+1,self.y[1]+1
                            self.postourne = 1

            elif self.posepieces == 7:
                if self.postourne == 1:
                    if self.x[2] >0:
                        if self.plateau[self.x[2]][self.y[2]-1] == 'bl' and self.plateau[self.x[2]-1][self.y[2]-1] == 'bl':
                            self.plateau[self.x[2]][self.y[2]-1], self.plateau[self.x[2]-1][self.y[2]-1] = 've','ve'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[2]-1,self.y[2]-1
                            self.x[1],self.y[1] = self.x[2],self.y[2]-1
                            self.plateau[self.x[3]][self.y[3]],self.x[3],self.y[3] = 'bl',self.x[2]+1,self.y[2]
                            self.postourne = 2
                elif self.postourne == 2:
                    if self.y[2]<9:
                        if self.plateau[self.x[2]][self.y[2]+1] == 'bl' and self.plateau[self.x[2]+1][self.y[2]-1] == 'bl':
                            self.plateau[self.x[2]][self.y[2]+1], self.plateau[self.x[2]+1][self.y[2]-1] = 've','ve'
                            self.plateau[self.x[0]][self.y[0]],self.x[0],self.y[0] = 'bl',self.x[2]+1,self.y[2]-1
                            self.plateau[self.x[1]][self.y[1]],self.x[1],self.y[1] = 'bl',self.x[2]+1,self.y[2]
                            self.x[3],self.y[3] = self.x[2],self.y[2]+1
                            self.postourne = 1


        def droite (self):
            if self.posepieces == 1:
                variacouleur = 'b'
            elif self.posepieces == 2:
                variacouleur = 'j'
            elif self.posepieces == 3:
                                variacouleur = 'vi'
            elif self.posepieces == 4:
                variacouleur = 'o'
            elif self.posepieces == 5:
                                variacouleur = 'bf'
            elif self.posepieces == 6:
                variacouleur = 'r'
            elif self.posepieces == 7:
                variacouleur = 've'
            testdroite = 0
            for i in range (4):
                if self.y[i] <  9:
                    testdroite+=1
            if testdroite == 4:
                for i in range(4):
                    if self.plateau[self.x[i]][self.y[i]+1] == 'bl' or self.plateau[self.x[i]][self.y[i]+1] == variacouleur:
                        testdroite+=1
            if testdroite == 8:
                pg = 0
                pp = 0
                mg=0
                mp=0
                rang = 0
                indicepg,indicemg,indicemp,indicepp=0,0,0,0
                for i in self.x:
                    if i>=pg:
                        pg,mg,mp,pp = i,pg,mg,mp
                        indicepg,indicemg,indicemp,indicepp = rang,indicepg,indicemg,indicemp
                    elif i>=mg:
                        mg,mp,pp = i,mg,mp
                        indicemg,indicemp,indicepp = rang,indicemg,indicemp
                    elif i>=mp:
                        mp,pp = i,mp
                        indicemp,indicepp = rang,indicemp
                    else:
                        pp=i
                        indicepp = rang
                    rang = rang+1
                self.plateau[self.x[indicepg]][self.y[indicepg]],self.y[indicepg] = 'bl',self.y[indicepg]+1
                self.plateau[self.x[indicemg]][self.y[indicemg]],self.y[indicemg] = 'bl',self.y[indicemg]+1
                self.plateau[self.x[indicemp]][self.y[indicemp]],self.y[indicemp] = 'bl',self.y[indicemp]+1
                self.plateau[self.x[indicepp]][self.y[indicepp]],self.y[indicepp] = 'bl',self.y[indicepp]+1
                for i in range (4):
                    self.plateau[self.x[i]][self.y[i]] = variacouleur



        def gauche (self):
            if self.posepieces == 1:
                variacouleur = 'b'
            elif self.posepieces == 2:
                variacouleur = 'j'
            elif self.posepieces == 3:
                variacouleur = 'vi'
            elif self.posepieces == 4:
                variacouleur = 'o'
            elif self.posepieces == 5:
                variacouleur = 'bf'
            elif self.posepieces == 6:
                variacouleur = 'r'
            elif self.posepieces == 7:
                variacouleur = 've'
            testgauche = 0
            for i in range (4):
                if self.y[i] > 0 :
                    testgauche+=1
            if testgauche == 4:
                for i in range(4):
                    if self.plateau[self.x[i]][self.y[i]-1] == 'bl' or self.plateau[self.x[i]][self.y[i]-1] == variacouleur:
                        testgauche+=1
            if testgauche == 8:
                pg = 0
                pp = 0
                mg=0
                mp=0
                rang = 0
                indicepg,indicemg,indicemp,indicepp=0,0,0,0
                for i in self.x:
                    if i>=pg:
                        pg,mg,mp,pp = i,pg,mg,mp
                        indicepg,indicemg,indicemp,indicepp = rang,indicepg,indicemg,indicemp
                    elif i>=mg:
                        mg,mp,pp = i,mg,mp
                        indicemg,indicemp,indicepp = rang,indicemg,indicemp
                    elif i>=mp:
                        mp,pp = i,mp
                        indicemp,indicepp = rang,indicemp
                    else:
                        pp=i
                        indicepp = rang
                    rang = rang+1
                self.plateau[self.x[indicepg]][self.y[indicepg]],self.y[indicepg] = 'bl',self.y[indicepg]-1
                self.plateau[self.x[indicemg]][self.y[indicemg]],self.y[indicemg] = 'bl',self.y[indicemg]-1
                self.plateau[self.x[indicemp]][self.y[indicemp]],self.y[indicemp] = 'bl',self.y[indicemp]-1
                self.plateau[self.x[indicepp]][self.y[indicepp]],self.y[indicepp] = 'bl',self.y[indicepp]-1
                for i in range (4):
                    self.plateau[self.x[i]][self.y[i]] = variacouleur

        def bas (self):
            if self.posepieces == 1:
                variacouleur = 'b'
            elif self.posepieces == 2:
                variacouleur = 'j'
            elif self.posepieces == 3:
                                variacouleur = 'vi'
            elif self.posepieces == 4:
                variacouleur = 'o'
            elif self.posepieces == 5:
                                variacouleur = 'bf'
            elif self.posepieces == 6:
                variacouleur = 'r'
            elif self.posepieces == 7:
                variacouleur = 've'
            testbas = 0
            for i in range (4):
                if self.x[i] < 21:
                    testbas +=1
            if testbas == 4:
                for i in range (4):
                    if self.plateau[self.x[i]+1][self.y[i]] == 'bl' or self.plateau[self.x[i]+1][self.y[i]] == variacouleur:
                        testbas+=1
            if testbas == 8:
                pg = 0
                pp = 0
                mg=0
                mp=0
                rang = 0
                indicepg,indicemg,indicemp,indicepp=0,0,0,0
                for i in self.x:
                    if i>=pg:
                        pg,mg,mp,pp = i,pg,mg,mp
                        indicepg,indicemg,indicemp,indicepp = rang,indicepg,indicemg,indicemp
                    elif i>=mg:
                        mg,mp,pp = i,mg,mp
                        indicemg,indicemp,indicepp = rang,indicemg,indicemp
                    elif i>=mp:
                        mp,pp = i,mp
                        indicemp,indicepp = rang,indicemp
                    else:
                        pp=i
                        indicepp = rang
                    rang = rang+1
                self.plateau[self.x[indicepg]][self.y[indicepg]],self.x[indicepg] = 'bl',self.x[indicepg]+1
                self.plateau[self.x[indicemg]][self.y[indicemg]],self.x[indicemg] = 'bl',self.x[indicemg]+1
                self.plateau[self.x[indicemp]][self.y[indicemp]],self.x[indicemp] = 'bl',self.x[indicemp]+1
                self.plateau[self.x[indicepp]][self.y[indicepp]],self.x[indicepp] = 'bl',self.x[indicepp]+1
                for i in range (4):
                    self.plateau[self.x[i]][self.y[i]] = variacouleur



        def start(self):
            fenetre.blit(grillejeu, (0,0))
            fenetre.blit(recscore, (23,100))
            fenetre.blit(recnext, (620,100))
            fenetre.blit(reclevel, (23,326))
            score = myfont.render('0', 1, (255,255,0))
            fenetre.blit(score, (100, 120))
            level= myfont.render('1', 1, (255,255,0))
            fenetre.blit(level, (100, 346))
            pygame.display.flip()
            jeuencours = 1
            debut = time()
            while jeuencours == 1 :
                for event in pygame.event.get():
                    if event.type == QUIT:
                        jeuencours = 0
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_d:
                            go.droite()
                        if event.key == K_a: #correspond au q sur un azerty
                            go.gauche()
                        if event.key == K_s:
                            go.bas()
                        if event.key == K_t:
                            go.tourne()

                for e in range(10):
                    for f in range (22):
                        if self.plateau[f][e] == 'bl':
                            fenetre.blit(carreblanc,(e*36+221,f*36+14))
                        elif self.plateau[f][e] == 'b' or self.plateau[f][e] == 'bfi':
                            fenetre.blit(carrebleu,(e*36+221,f*36+14))
                        elif self.plateau[f][e] == 'j' or self.plateau[f][e] == 'jfi':
                            fenetre.blit(carrejaune,(e*36+221,f*36+14))
                        elif self.plateau[f][e] == 'vi' or self.plateau[f][e] == 'vifi':
                            fenetre.blit(carreviolet,(e*36+221,f*36+14))
                        elif self.plateau[f][e] == 'o' or self.plateau[f][e] == 'ofi':
                            fenetre.blit(carreorange,(e*36+221,f*36+14))
                        elif self.plateau[f][e] == 'bf' or self.plateau[f][e] == 'bffi':
                            fenetre.blit(carrebleufonce,(e*36+221,f*36+14))
                        elif self.plateau[f][e] == 'r' or self.plateau[f][e] == 'rfi':
                            fenetre.blit(carrerouge,(e*36+221,f*36+14))
                        elif self.plateau[f][e] == 've' or self.plateau[f][e] == 'vefi':
                            fenetre.blit(carrevert,(e*36+221,f*36+14))

                pygame.display.flip()
                fin = time()
                if (fin -debut) >=self.time: #descente d'un niveau
                    debut =time()
                    desso = 0
                    switch = 0
                    if self.posepieces == 1:
                                variacouleur = 'b'
                    elif self.posepieces == 2:
                                variacouleur = 'j'
                    elif self.posepieces == 3:
                                variacouleur = 'vi'
                    elif self.posepieces == 4:
                                variacouleur = 'o'
                    elif self.posepieces == 5:
                                variacouleur = 'bf'
                    elif self.posepieces == 6:
                                variacouleur = 'r'
                    elif self.posepieces == 7:
                                variacouleur = 've'



                    for i in range (4): #test fin de jeu et de pose de pièce
                        if self.x[i] == 21:
                            desso = 1
                        if self.x[i]==0:
                            if self.plateau[self.x[i]+1][self.y[i]]!=variacouleur and self.plateau[self.x[i]+1][self.y[i]]!='bl':
                                go.classement()
                                print ('Perdu')
                                jeuencours =0
                                pygame.quit()
                                sys.exit()
                    if desso ==1:
                        for i in range (4):
                            self.plateau[self.x[i]][self.y[i]]= variacouleur+str('fi')          # a corriger !!
                            switch = 1
                    elif desso == 0:
                        for i in range (4):
                            if self.plateau[self.x[i]+1][self.y[i]] !=variacouleur and  self.plateau[self.x[i]+1][self.y[i]] !='bl':
                                desso = 1
                    if desso ==1:
                            for i in range (4):
                                self.plateau[self.x[i]][self.y[i]]= variacouleur+str('fi')
                                switch = 1
                    else:
                            pg = 0
                            pp = 0
                            mg=0
                            mp=0
                            rang = 0
                            indicepg,indicemg,indicemp,indicepp=0,0,0,0
                            for i in self.x:
                                    if i>=pg:
                                        pg,mg,mp,pp = i,pg,mg,mp
                                        indicepg,indicemg,indicemp,indicepp = rang,indicepg,indicemg,indicemp
                                    elif i>=mg:
                                        mg,mp,pp = i,mg,mp
                                        indicemg,indicemp,indicepp = rang,indicemg,indicemp
                                    elif i>=mp:
                                        mp,pp = i,mp
                                        indicemp,indicepp = rang,indicemp
                                    else:
                                        pp=i
                                        indicepp = rang
                                    rang = rang+1

                            self.plateau[self.x[indicepg]+1][self.y[indicepg]]=variacouleur
                            self.plateau[self.x[indicepg]][self.y[indicepg]]='bl'
                            self.plateau[self.x[indicemg]+1][self.y[indicemg]]=variacouleur
                            self.plateau[self.x[indicemg]][self.y[indicemg]]='bl'
                            self.plateau[self.x[indicemp]+1][self.y[indicemp]]=variacouleur
                            self.plateau[self.x[indicemp]][self.y[indicemp]]='bl'
                            self.plateau[self.x[indicepp]+1][self.y[indicepp]]=variacouleur
                            self.plateau[self.x[indicepp]][self.y[indicepp]]='bl'

                            for i in range (4):
                                self.x[i] = self.x[i]+1
                    go.afficher_plateau()
                    if go.testligne() == True:
                        if self.lignecomplet == 1:
                            a = self.listeligne.pop()
                            while a !=0:
                                self.plateau[a]=self.plateau[a-1]
                                a = a-1
                            self.plateau[a] =['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']

                        elif self.lignecomplet == 2:
                            a = self.listeligne.pop()
                            if a%2==0:
                                print('pair')
                                while a > 0:  #changer
                                    self.plateau[a],self.plateau[a-1]=self.plateau[a-2],self.plateau[a-3]
                                    a = a-2
                                self.plateau[a],self.plateau[a+1] =['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                go.afficher_plateau()
                            elif a%2==1:
                                print('impair')
                                while a>1:
                                    self.plateau[a],self.plateau[a-1]=self.plateau[a-2],self.plateau[a-3]
                                    a = a-2
                                self.plateau[a],self.plateau[a-1] =['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']

                        elif self.lignecomplet == 3:
                            a = self.listeligne.pop()
                            if a%3==0:
                                while a!= 3:
                                    self.plateau[a],self.plateau[a-1],self.plateau[a-2]=self.plateau[a-3],self.plateau[a-4],self.plateau[a-5]
                                    a = a-3
                                self.plateau[a] = self.plateau[a-3]
                                self.plateau[a-1] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-2] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-3] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                            elif a%3== 1:
                                while a!=4:
                                    self.plateau[a],self.plateau[a-1],self.plateau[a-2]=self.plateau[a-3],self.plateau[a-4],self.plateau[a-5]
                                    a = a-3
                                self.plateau[a],self.plateau[a-1]=self.plateau[a-3],self.plateau[a-4]
                                self.plateau[a-2] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-3] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-4] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                            elif a%3== 2:
                                while a!=2:
                                    self.plateau[a],self.plateau[a-1],self.plateau[a-2]=self.plateau[a-3],self.plateau[a-4],self.plateau[a-5]
                                    a = a-3
                                self.plateau[a] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-1] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-2] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']

                        elif self.lignecomplet == 4:
                            a = self.listeligne.pop()
                            if a%4==0:
                                while a!= 4:
                                    self.plateau[a],self.plateau[a-1],self.plateau[a-2],self.plateau[a-3]=self.plateau[a-4],self.plateau[a-5],self.plateau[a-6],self.plateau[a-7]
                                    a = a-4
                                self.plateau[a] = self.plateau[a-4]
                                self.plateau[a-1] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-2] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-3] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-4] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                            elif a%4== 1:
                                while a!=5:
                                    self.plateau[a],self.plateau[a-1],self.plateau[a-2],self.plateau[a-3]=self.plateau[a-4],self.plateau[a-5],self.plateau[a-6],self.plateau[a-7]
                                    a = a-4
                                self.plateau[a],self.plateau[a-1]=self.plateau[a-4],self.plateau[a-5]
                                self.plateau[a-2] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-3] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-4] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-5] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                            elif a%4== 2:
                                while a!=6:
                                    self.plateau[a],self.plateau[a-1],self.plateau[a-2],self.plateau[a-3]=self.plateau[a-4],self.plateau[a-5],self.plateau[a-6],self.plateau[a-7]
                                    a = a-4
                                self.plateau[a],self.plateau[a-1],self.plateau[a-2]=self.plateau[a-4],self.plateau[a-5],self.plateau[a-6]
                                self.plateau[a-3] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-4] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-5] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-6] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                            elif a%4== 3:
                                while a!=3:
                                    self.plateau[a],self.plateau[a-1],self.plateau[a-2],self.plateau[a-3]=self.plateau[a-4],self.plateau[a-5],self.plateau[a-6],self.plateau[a-7]
                                    a = a-4
                                self.plateau[a] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-1] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-2] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']
                                self.plateau[a-3] = ['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']

                    if switch == 1:
                        self.postourne = 1
                        go.posepiece()

        def pageacceuil(self):
            fenetre.blit(pageacceuil, (0,0))
            myfont = pygame.font.SysFont("monospace", 25)
            with open("fichierpseudo.txt") as f:
                pseudo1 = f.readlines()[0]
            with open("fichierpseudo.txt") as f:
                pseudo2 = f.readlines()[1]
            with open("fichierpseudo.txt") as f:
                pseudo3 = f.readlines()[2]
            with open("fichierpseudo.txt") as f:
                pseudo4 = f.readlines()[3]
            with open("fichierpseudo.txt") as f:
                pseudo5 = f.readlines()[4]
            f.close()
            with open("fichierscore.txt") as f:
                top1 = f.readlines()[0]
            with open("fichierscore.txt") as f:
                top2 = f.readlines()[1]
            with open("fichierscore.txt") as f:
                top3 = f.readlines()[2]
            with open("fichierscore.txt") as f:
                top4 = f.readlines()[3]
            with open("fichierscore.txt") as f:
                top5 = f.readlines()[4]
            f.close()
            pseudo1aff = myfont.render(pseudo1[:-1], 5, (255,255,255))
            fenetre.blit(pseudo1aff, (130, 287))
            pseudo1score = myfont.render(top1[:-1], 5, (255,255,255))
            fenetre.blit(pseudo1score, (260, 287))

            pseudo2aff = myfont.render(pseudo2[:-1], 5, (255,255,255))
            fenetre.blit(pseudo2aff, (130, 364))
            pseudo2score = myfont.render(top2[:-1], 5, (255,255,255))
            fenetre.blit(pseudo2score, (260, 364))

            pseudo3aff = myfont.render(pseudo3[:-1], 5, (255,255,255))
            fenetre.blit(pseudo3aff, (130, 441))
            pseudo3score = myfont.render(top3[:-1], 5, (255,255,255))
            fenetre.blit(pseudo3score, (260, 441))

            pseudo4aff = myfont.render(pseudo4[:-1], 5, (255,255,255))
            fenetre.blit(pseudo4aff, (130, 518))
            pseudo4score = myfont.render(top4[:-1], 5, (255,255,255))
            fenetre.blit(pseudo4score, (260, 518))

            pseudo5aff = myfont.render(pseudo5[:-1], 5, (255,255,255))
            fenetre.blit(pseudo5aff, (130, 595))
            pseudo5score = myfont.render(top5, 5, (255,255,255))
            fenetre.blit(pseudo5score, (260, 595))

            if self.switchson == 0 :
                fenetre.blit(sonon, (620, 590))
            elif self.switchson == 1:
                fenetre.blit(sonoff, (620, 590))
            pygame.display.flip()
            pageboucle = 1
            while pageboucle == 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        jeuencours = 0
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if 420<event.pos[0] and event.pos[0]<720:
                                if 250<event.pos[1] and event.pos[1]<550:
                                    pageboucle =0
                                    go.posepiece()
                                    go.start()
                            if 590<event.pos[0] and event.pos[0]<730:
                                if 620<event.pos[1] and event.pos[1]<760:
                                    if self.switchson == 0 :
                                        fenetre.blit(sonoff, (620, 590))
                                        self.switchson = 1
                                        pygame.display.flip()
                                        pygame.mixer.music.set_volume(0) # réglage du volume

                                    elif self.switchson == 1:
                                        fenetre.blit(sonon, (620, 590))
                                        self.switchson = 0
                                        pygame.display.flip()
                                        pygame.mixer.music.set_volume(0.6)
                            if 50<event.pos[0] and event.pos[0]<180:
                                if 645<event.pos[1] and event.pos[1]<775:
                                    pageboucle =0
                                    go.explicationrègle()

        def explicationrègle(self):
            fenetre.blit(pageparametre, (0,0))
            pygame.display.flip()
            pageboucle = 1
            while pageboucle == 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        jeuencours = 0
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if 50<event.pos[0] and event.pos[0]<230:
                                if 500<event.pos[1] and event.pos[1]<680:
                                    pageboucle =0
                                    go.pageacceuil()


        def entrerpseudo(self):
            base_font = pygame.font.Font(None, 32)
            user_text = ''

            input_rect = pygame.Rect(200, 200, 140, 32)

            color_passive = pygame.Color('chartreuse4')
            color = color_passive

            active = False
            pp = True
            while pp==True:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_RETURN:
                            if len(user_text) < 9:
                                pp = False
                        else:
                            user_text += event.unicode
                    if event.type == MOUSEBUTTONDOWN:
                            user_text = ''

                fenetre.fill((255, 255, 255))

                pygame.draw.rect(fenetre, color, input_rect)

                text_surface = base_font.render(user_text, True, (255, 255, 255))

                fenetre.blit(text_surface, (input_rect.x+5, input_rect.y+5))
                input_rect.w = max(100, text_surface.get_width()+10)

                pygame.display.flip()

                clock.tick(60)
            return user_text



premierepiece = random.randint(1,7)
go = jeu([['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl'],['bl', 'bl', 'bl','bl', 'bl', 'bl','bl', 'bl', 'bl','bl']],[0,0,0,0],[0,0,0,0],1,1,[],0,0,1,0.5,premierepiece,0)
go.pageacceuil()

#1h dessus pendant perm le 04/02
#dernière semaine : correction de bug comme celui des points et des tests, dév de réserve