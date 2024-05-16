import pygame
import sys
import random
import time

hoihs = True
rand = 0
true = True
list =[]

clock = pygame.time.Clock()
background_colour = (234, 212, 252)
screen = pygame.display.set_mode((1920, 1080))
bg = pygame.image.load("Game hop phu huynh\wstpkm.png")

vu = pygame.image.load("Game hop phu huynh\_anh\_vsv.png")
khoi = pygame.image.load("Game hop phu huynh\_anh\_nkdk.png")
nam = pygame.image.load("Game hop phu huynh\_anh\_lbn.png")
thanh = pygame.image.load("Game hop phu huynh\_anh\_lht.png")
duykhanh = pygame.image.load("Game hop phu huynh\_anh\_ddk.png")
hiengiang = pygame.image.load("Game hop phu huynh\_anh\_dhieng.png")
hai = pygame.image.load("Game hop phu huynh\_anh\_pmh.png")
hminh = pygame.image.load("Game hop phu huynh\_anh\_dhm.png")
quan = pygame.image.load("Game hop phu huynh\_anh\_tpmq.png")
quynh = pygame.image.load("Game hop phu huynh\_anh\_dhtq.png")
han = pygame.image.load("Game hop phu huynh\_anh\_lgh.png")
vinh = pygame.image.load("Game hop phu huynh\_anh\_ncv.png")
dminh = pygame.image.load("Game hop phu huynh\_anh\_ndm.png")
linh = pygame.image.load("Game hop phu huynh\_anh\_vtgl.png")
vhuyen = pygame.image.load("Game hop phu huynh\_anh\_vtkh.png")
truc = pygame.image.load("Game hop phu huynh\_anh\_ltt.png")
van = pygame.image.load("Game hop phu huynh\_anh\_dkv.png")
manh = pygame.image.load("Game hop phu huynh\_anh\_nma.png")
tanh = pygame.image.load("Game hop phu huynh\_anh\_nnta.png")
binh = pygame.image.load("Game hop phu huynh\_anh\_phb.png")
honggiang = pygame.image.load("Game hop phu huynh\_anh\_dhongg.png")
tra = pygame.image.load("Game hop phu huynh\_anh\_ptt.png")
thanhf = pygame.image.load("Game hop phu huynh\_anh\_nnt.png")
yen = pygame.image.load("Game hop phu huynh\_anh\_nhy.png")
lgiang = pygame.image.load("Game hop phu huynh\_anh\_nplg.png")
nminh = pygame.image.load("Game hop phu huynh\_anh\_dnm.png")
nhat = pygame.image.load("Game hop phu huynh\_anh\_dln.png")
thuy = pygame.image.load("Game hop phu huynh\_anh\_nht.png")
tminh = pygame.image.load("Game hop phu huynh\_anh\_ptm.png")
huykhanh = pygame.image.load("Game hop phu huynh\_anh\_nhk.png")
chuyen = pygame.image.load("Game hop phu huynh\_anh\_ctkh.png")

vu_h = pygame.image.load("Game hop phu huynh\_anh\_vsv.png")
khoi_h = pygame.image.load("Game hop phu huynh\_anh\_nkdk.png")
nam_h = pygame.image.load("Game hop phu huynh\_anh\_lbn.png")
thanh_h = pygame.image.load("Game hop phu huynh\_anh\_lht.png")
duykhanh_h = pygame.image.load("Game hop phu huynh\_anh\_ddk.png")
hiengiang_h = pygame.image.load("Game hop phu huynh\_anh\_dhieng.png")
hai_h = pygame.image.load("Game hop phu huynh\_anh\_pmh.png")
hminh_h = pygame.image.load("Game hop phu huynh\_anh\_dhm.png")
quan_h = pygame.image.load("Game hop phu huynh\_anh\_tpmq.png")
quynh_h = pygame.image.load("Game hop phu huynh\_anh\_dhtq.png")
han_h = pygame.image.load("Game hop phu huynh\_anh\_lgh.png")
vinh_h = pygame.image.load("Game hop phu huynh\_anh\_ncv.png")
dminh_h = pygame.image.load("Game hop phu huynh\_anh\_ndm.png")
linh_h = pygame.image.load("Game hop phu huynh\_anh\_vtgl.png")
vhuyen_h = pygame.image.load("Game hop phu huynh\_anh\_vtkh.png")
truc_h = pygame.image.load("Game hop phu huynh\_anh\_ltt.png")
van_h = pygame.image.load("Game hop phu huynh\_anh\_dkv.png")
manh_h = pygame.image.load("Game hop phu huynh\_anh\_nma.png")
tanh_h = pygame.image.load("Game hop phu huynh\_anh\_nnta.png")
binh_h = pygame.image.load("Game hop phu huynh\_anh\_phb.png")
honggiang_h = pygame.image.load("Game hop phu huynh\_anh\_dhongg.png")
tra_h = pygame.image.load("Game hop phu huynh\_anh\_ptt.png")
thanhf_h = pygame.image.load("Game hop phu huynh\_anh\_nnt.png")
yen_h = pygame.image.load("Game hop phu huynh\_anh\_nhy.png")
lgiang_h = pygame.image.load("Game hop phu huynh\_anh\_nplg.png")
nminh_h = pygame.image.load("Game hop phu huynh\_anh\_dnm.png")
nhat_h = pygame.image.load("Game hop phu huynh\_anh\_dln.png")
thuy_h = pygame.image.load("Game hop phu huynh\_anh\_nht.png")
tminh_h = pygame.image.load("Game hop phu huynh\_anh\_ptm.png")
huykhanh_h = pygame.image.load("Game hop phu huynh\_anh\_nhk.png")
chuyen_h = pygame.image.load("Game hop phu huynh\_anh\_ctkh.png")

def rndm(any):
    rand = random.randint(0,30)
    if rand in list:
        rand = random.randint(0,30)
        rndm(0)
    else:
        list.append(rand)


pygame.display.set_caption("Who is that pokemon?")

screen.fill(background_colour)

running = True

rand = random.randint(0, 30)

while running:

    if hoihs == True:
        screen.blit(bg, (0, 0))
        
        if true == True:
            if rand == 0:
                screen.blit(khoi, (300, 300))
            elif rand == 1:
                screen.blit(nam, (300, 300))
            elif rand == 2:
                screen.blit(thanh, (300, 300))
            elif rand == 3:
                screen.blit(vu, (300, 300))
            elif rand == 4:
                screen.blit(duykhanh, (300, 300))
            elif rand == 5:
                screen.blit(hiengiang, (300, 300))
            elif rand == 6:
                screen.blit(hai, (500, 500))
            elif rand == 7:
                screen.blit(hminh, (300, 300))
            elif rand == 8:
                screen.blit(quan, (300, 300))
            elif rand == 9:
                screen.blit(quynh, (300, 300))
            elif rand == 10:
                screen.blit(han, (300, 300))
            elif rand == 11:
                screen.blit(vinh, (300, 300))
            elif rand == 12:
                screen.blit(dminh, (300, 300))
            elif rand == 13:
                screen.blit(linh, (300, 300))
            elif rand == 14:
                screen.blit(vhuyen, (300, 300))
            elif rand == 15:
                screen.blit(truc, (300, 300))
            elif rand == 16:
                screen.blit(van, (300, 300))
            elif rand == 17:
                screen.blit(manh, (300, 300))
            elif rand == 18:
                screen.blit(tanh, (300, 300))
            elif rand == 19:
                screen.blit(binh, (300, 300))
            elif rand == 20:
                screen.blit(honggiang, (300, 300))
            elif rand == 21:
                screen.blit(tra, (300, 300))
            elif rand == 22:
                screen.blit(thanhf, (300, 300))
            elif rand == 23:
                screen.blit(yen, (300, 300))
            elif rand == 24:
                screen.blit(lgiang, (300, 300))
            elif rand == 25:
                screen.blit(nminh, (300, 300))
            elif rand == 26:
                screen.blit(nhat, (300, 300))
            elif rand == 27:
                screen.blit(thuy, (300, 300))
            elif rand == 28:
                screen.blit(tminh, (300, 300))
            elif rand == 29:
                screen.blit(huykhanh, (300, 300))
            elif rand == 30:
                screen.blit(chuyen, (300, 300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            rand = random.randint(0,30)
            if rand in list:
                rand = random.randint(0,30)
                rndm(0)
            else:
                list.append(rand)
    pygame.display.flip()
