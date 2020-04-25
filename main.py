import time
import random
import os
from config import *
import sys

def clear_screen():
    if 'linux' in sys.platform.lower(): os.system('clear')
    else: os.system('clr')

class horse:
    def __init__(self,name):
        self.position = 0
        self.name = name
        self.buff = 1
        self.buff_count = 0
        self.fall_count = 0
    
    def tick(self):
        if self.fall_count > 0:
            self.fall_count-=1
            return
        if self.buff_count<=0 : self.buff = 1
        if random.random()<=0.1:
            if random.random()>FALL_POSS: 
                self.buff_count=20
                self.buff = 2
            else:
                self.fall_count = 10
        self.position += random.randint(RANGE_LOW,RANGE_HIGH)*self.buff
        if self.buff_count>=0: self.buff_count-=1

    def arrives(self):
        return self.position >= MAX_LENGTH
    
    def display(self):
        now_pos = min(self.position,MAX_LENGTH)
        char_cnt = int(100*now_pos/MAX_LENGTH)
        ch = '*'
        if self.fall_count: ch='x'
        print("%8s:[ %s%s%s]"%(self.name,'='*char_cnt, ch, '='*(99-char_cnt)))

def horse_game(play_num):
    players = []
    for i in range(play_num): players.append(horse(str(i+1)))
    while True:
        clear_screen()
        ARRIVE = []
        for player in players: 
            if  player.arrives(): ARRIVE.append(player.name)
        if ARRIVE:
            print(ARRIVE)
            break
        for player in players: player.display()
        for i in range(play_num):
            players[i].tick()
        
        time.sleep(0.5)

def main():
    horse_game(5)

if __name__ == '__main__':
    main()