import random
from re import M
from time import sleep
import math

class Player:
    def __init__(self, name):
        self.name = name
        self.poke1 = 0
        self.poke2 = 0
        self.poke3 = 0
        self.poke4 = 0
        self.poke5 = 0
        self.poke6 = 0
        self.dead = []
        self.pc_box = []
        self.total_pokemon = 0
        self.victorious = False

    def battle(self, target):
        while self.victorious == False:
            print('                                         ')
            print('                                         ')
            print('                                         ')
            print('#########################################')
            print('#                                       #')
            print('#            BATTLE SEQUENCE            #')
            print('#                                       #')
            print('#########################################')
            print('                                         ')
            print('                                         ')
            print('                                         ')
            print('===============================')
            print(''"level",self.poke1.lvl, self.poke1.name, 'has',int(self.poke1.hp), '/', int(self.poke1.total_hp),'HP left')
            print('===============================')
            print(''"level",target.poke1.lvl, target.poke1.name, 'has',int(target.poke1.hp), '/',int(target.poke1.total_hp),'HP left')
            print('===============================')
            print('                                         ')
            print('================================')
            print(" 1. ", self.poke1.move1.name, '')
            print('===============================')
            print(' 2. ', self.poke1.move2.name, '')
            print('===============================')
            print('                                         ')
            print('                                         ')
            option = input('Choose your attack!: ')
            if self.poke1.speed >= target.poke1.speed:
                if option == "1":
                    print(self.poke1.name, 'used', self.poke1.move1.name,'!')
                    self.poke1.attack(self.poke1.move1, target.poke1)
                    sleep(1)
                    if self.alive(target) == False:
                        self.victory(target)
                    else:
                        print(target.poke1.name, 'has', int(target.poke1.hp),'/',int(target.poke1.total_hp),"HP left!")
                        print(target.poke1.name, 'used', target.poke1.move1.name,'!')
                        target.poke1.attack(target.poke1.move1, self.poke1)
                        sleep(1)
                        if self.alive(self) == False:
                            self.lose(target)
                            break
                        else:
                            print(self.poke1.name, 'has', int(self.poke1.hp),'/',int(self.poke1.total_hp),"HP left!")
                            continue
                elif option == "2":
                    print(self.poke1.name, 'used', self.poke1.move2.name,'!')
                    self.poke1.attack(self.poke1.move2, target.poke1)
                    sleep(1)
                    if self.alive(target) == False:
                        self.victory(target)
                    else:
                        print(target.poke1.name, 'has', int(target.poke1.hp),'/',int(target.poke1.total_hp),"HP left!")
                        print(target.poke1.name, 'used', target.poke1.move1.name,'!')
                        target.poke1.attack(target.poke1.move1, self.poke1)
                        sleep(1)
                        if self.alive(self) == False:
                            self.lose(target)
                            break
                        else:
                            print(self.poke1.name, 'has', int(self.poke1.hp),'/',int(self.poke1.total_hp), "HP left!")
                            continue
                else:
                    print('Please choose a valid option')
                    continue
            else:
                if option == "1":
                    print(target.poke1.name, 'used', target.poke1.move1.name,'!')
                    target.poke1.attack(target.poke1.move1, self.poke1)
                    sleep(1)
                    if self.alive(self) == False:
                            self.lose(target)
                            break
                    else:
                        print(self.poke1.name, 'has', int(self.poke1.hp),'/',int(self.poke1.total_hp), "HP left!")
                        print(self.poke1.name, 'used', self.poke1.move1.name,'!')
                        self.poke1.attack(self.poke1.move1, target.poke1)
                        sleep(1)
                        if self.alive(target) == False:
                            self.victory(target)
                        else:
                            print(target.poke1.name, 'has', int(target.poke1.hp),'/',int(target.poke1.total_hp),"HP left!")
                            continue
                if option == "2":
                    print(target.poke1.name, 'used', target.poke1.move1.name,'!')
                    target.poke1.attack(target.poke1.move1, self.poke1)
                    sleep(1)
                    if self.alive(self) == False:
                            self.lose(target)
                            break
                    else:
                        print(self.poke1.name, 'has', int(self.poke1.hp),'/',int(self.poke1.total_hp), "HP left!")
                        print(self.poke1.name, 'used', self.poke1.move2.name,'!')
                        self.poke1.attack(self.poke1.move2, target.poke1)
                        sleep(1)
                        if self.alive(target) == False:
                            self.victory(target)
                        else:
                            print(target.poke1.name, 'has', int(target.poke1.hp),'/',int(target.poke1.total_hp),"HP left!")
                            continue
        else:
            pass

    def swap(self, target):
        if target.poke2 != 0:
            target.poke1 = target.poke2
            target.poke2 = 0
            sleep(2)
            print('                                         ')
            print(target.name, 'sent out out their next POKEMON')
            print('                                         ')
            print(target.name,'sent out', target.poke1.name)
            print('Go get em', target.poke1.name,"!")
            self.battle(target)
        elif isinstance(target, Trainer):
            print(target.name, 'is out of usable POKEMON!')
            sleep(1)
            pass
        else:
            pass
    
    def selfswap(self, target):
        if self.poke2 != 0:
            self.dead = [self.poke1]
            self.poke1 = self.poke2
            self.poke2 = 0
            print((self.name.title()), 'sent out out their next POKEMON')
            print(self.name,'sent out', self.poke1)
            print('Go get em', self.poke1.name,"!")
            self.battle(target)
        else:
            print(self.name, 'is out of usable POKEMON!')
            sleep(1)
            pass

    def alive(self, target):
        if target.poke1.hp <= 0:
            return False
        else:
            return True

    def victory(self, target):
        sleep(1)
        print(target.poke1.name, 'has fainted!')
        sleep(1)
        self.poke1.exp_gain(target.poke1)
        self.swap(target)
        print('The battle is over!')
        print('You are victorious!')
        self.victorious = True

    def lose(self, target):
        sleep(1)
        print(self.poke1.name, 'has fainted!')
        sleep(1)
        self.selfswap(target)
        print('The battle is over!')
        print('You have been defeated!')

    def wildbattle(self, target):
        target.hp = target.total_hp
        target.captured = False
        while target.captured == False:
            print('                                         ')
            print('                                         ')
            print('                                         ')
            print('#########################################')
            print('#                                       #')
            print('#            BATTLE SEQUENCE            #')
            print('#                                       #')
            print('#########################################')
            print('                                         ')
            print('                                         ')
            print('                                         ')
            print('===============================')
            print(''"level",self.poke1.lvl, self.poke1.name, 'has',int(self.poke1.hp), '/', int(self.poke1.total_hp),'HP left')
            print('===============================')
            print(''"level",target.poke1.lvl, target.poke1.name, 'has',int(target.poke1.hp), '/',int(target.poke1.total_hp),'HP left')
            print('===============================')
            print('                                         ')
            print('================================')
            print(" 1. ", self.poke1.move1.name, '')
            print('===============================')
            print(' 2. ', self.poke1.move2.name, '')
            print('===============================')
            print(' 3.  Throw POKEBALL')
            print('===============================')
            print('                                         ')
            print('                                         ')
            option = input('Choose your action!: ')
            if option == '3':
                if self.total_pokemon <= 6:
                    self.capture(target)
                    if target.captured == True:
                        break
                    else:
                        target.poke1.attack(target.poke1.move1, self.poke1)
                        sleep(1)
                        print(self.poke1.name, 'has', int(self.poke1.hp), "HP left!")
                        if self.alive(self) == False:
                            self.lose(target)
                            break
                        else:
                            continue
                else:
                    print('Your party is full!')
                    continue
            else:
                pass
            if self.poke1.speed >= target.poke1.speed:
                if option == "1":
                    print(self.poke1.name, 'used', self.poke1.move1.name,'!')
                    self.poke1.attack(self.poke1.move1, target.poke1)
                    sleep(1)
                    if self.alive(target) == False:
                        self.victory(target)
                        break
                    else:
                        print(target.poke1.name, 'has', int(target.poke1.hp), "HP left!")
                        print(target.poke1.name, 'used', target.poke1.move1.name,'!')
                        target.poke1.attack(target.poke1.move1, self.poke1)
                        sleep(1)
                        if self.alive(self) == False:
                            self.lose(target)
                            break
                        else:
                            print(self.poke1.name, 'has', int(self.poke1.hp), "HP left!")
                            continue
                elif option == "2":
                    print(self.poke1.name, 'used', self.poke1.move2.name,'!')
                    self.poke1.attack(self.poke1.move2, target.poke1)
                    sleep(1)
                    if self.alive(target) == False:
                        self.victory(target)
                        break
                    else:
                        print(target.poke1.name, 'has', int(target.poke1.hp), "HP left!")
                        print(target.poke1.name, 'used', target.poke1.move1.name,'!')
                        target.poke1.attack(target.poke1.move1, self.poke1)
                        sleep(1)
                        print(self.poke1.name, 'has', int(self.poke1.hp), "HP left!")
                        if self.alive(self) == False:
                            self.lose(target)
                            break
                        else:
                            continue
                else:
                    print('Please choose a valid option')
                    continue
            else:
                if option == "1":
                    print(target.poke1.name, 'used', target.poke1.move1.name,'!')
                    target.poke1.attack(target.poke1.move1, self.poke1)
                    sleep(1)
                    if self.alive(self) == False:
                            self.lose(target)
                            break
                    else:
                        print(self.poke1.name, 'has', int(self.poke1.hp), "HP left!")
                        print(self.poke1.name, 'used', self.poke1.move1.name,'!')
                        self.poke1.attack(self.poke1.move1, target.poke1)
                        sleep(1)
                        if self.alive(target) == False:
                            self.victory(target)
                            break
                        else:
                            print(target.poke1.name, 'has', int(target.poke1.hp), "HP left!")
                            continue
                elif option == "2":
                    print(target.poke1.name, 'used', target.poke1.move1.name,'!')
                    target.poke1.attack(target.poke1.move1, self.poke1)
                    sleep(1)
                    if self.alive(self) == False:
                            self.lose(target)
                            break
                    else:
                        print(self.poke1.name, 'has', int(self.poke1.hp), "HP left!")
                        print(self.poke1.name, 'used', self.poke1.move2.name,'!')
                        self.poke1.attack(self.poke1.move2, target.poke1)
                        sleep(1)
                        if self.alive(target) == False:
                            self.victory(target)
                            break
                        else:
                            print(target.poke1.name, 'has', int(target.poke1.hp), "HP left!")
                            continue
                else:
                    print('Please choose a valid option')
                    continue

    def capture(self, target):
        advantage = (self.poke1.lvl / target.lvl)
        throw = (random.randrange(3, 5) / 10) * advantage
        if throw >= 0.4:
            sleep(2)
            print('                                         ')
            print('                                         ')
            print('...')
            print('                                         ')
            print('                                         ')
            if throw >= 0.45:
                sleep(2)
                print('                                         ')
                print('                                         ')
                print('...')
                print('                                         ')
                print('                                         ')
                if throw >= 0.5:
                    sleep(2)
                    print('                                         ')
                    print('                                         ')
                    print(target.name,'has been captured!')
                    print('                                         ')
                    print('                                         ')
                    print(target.name,"has been added to your party")
                    sleep(1)
                    choice = input("What would you like to name your new POKEMON?: ")
                    target.name = choice
                    if self.total_pokemon == 1:
                        self.poke2 = target
                        self.total_pokemon += 1
                    elif self.total_pokemon == 2:
                        self.poke3 = target
                        self.total_pokemon += 1
                    elif self.total_pokemon == 3:
                        self.poke4 = target
                        self.total_pokemon += 1
                    elif self.total_pokemon == 4:
                        self.poke5 = target
                        self.total_pokemon += 1
                    elif self.total_pokemon == 5:
                        self.poke6 = target
                        self.total_pokemon += 1
                    target.captured = True
            else:
                print('!!!')
                print('The POKEMON broke free!')
        else:
            sleep(2)
            print('!!!')
            print('The POKEMON broke free!')

    def wild_encounter(self, target:None):
        if target is None:
            self.target = []
        else:
            self.target = target
        pokemon = random.choices(
                    population = [1,2,3],
                    weights = [50, 40, 10],
                    k = 1
                  )
        if pokemon == [1]:
            encounter = target[0]
            encounter.poke1 = encounter
            encounter.poke2 = 0
            self.wildbattle(encounter)
        elif pokemon == [2]:
            encounter = target[1]
            encounter.poke1 = encounter
            encounter.poke2 = 0
            self.wildbattle(encounter)
        elif pokemon == [3]:
            encounter = target[2]
            encounter.poke1 = encounter
            encounter.poke2 = 0
            self.wildbattle(encounter)

    def heal(self, target):
        target.hp = target.total_hp

    def heal_team(self):
        self.heal(self.poke1)
        if self.poke2 != 0:
            self.heal(self.poke2)
        elif self.poke3 != 0:
            self.heal(self.poke3)
        elif self.poke4 != 0:
            self.heal(self.poke4)
        elif self.poke5 != 0:
            self.heal(self.poke5)
        elif self.poke3 != 0:
            self.heal(self.poke6)
        for x in self.dead:
            self.heal(x)
        if len(self.dead) == 5:
            self.poke2 = self.dead[0]
            self.poke3 = self.dead[1]
            self.poke4 = self.dead[2]
            self.poke5 = self.dead[3]
            self.poke6 = self.dead[4]
            self.dead = []
        elif len(self.dead) == 4 and self.total_pokemon == 6:
            self.poke3 = self.dead[0]
            self.poke4 = self.dead[1]
            self.poke5 = self.dead[2]
            self.poke6 = self.dead[3]
            self.dead = []
        elif len(self.dead) == 4 and self.total_pokemon == 5:
            self.poke2 = self.dead[0]
            self.poke3 = self.dead[1]
            self.poke4 = self.dead[2]
            self.poke5 = self.dead[3]
            self.dead = []
        elif len(self.dead) == 3 and self.total_pokemon == 6:
            self.poke4 = self.dead[0]
            self.poke5 = self.dead[1]
            self.poke6 = self.dead[2]
            self.dead = []
        elif len(self.dead) == 3 and self.total_pokemon == 5:
            self.poke3 = self.dead[0]
            self.poke4 = self.dead[1]
            self.poke5 = self.dead[2]
            self.dead = []
        elif len(self.dead) == 3 and self.total_pokemon == 4:
            self.poke2 = self.dead[0]
            self.poke3 = self.dead[1]
            self.poke4 = self.dead[2]
            self.dead = []
        elif len(self.dead) == 2 and self.total_pokemon == 6:
            self.poke5 = self.dead[0]
            self.poke6 = self.dead[1]
            self.dead = []
        elif len(self.dead) == 2 and self.total_pokemon == 5:
            self.poke4 = self.dead[0]
            self.poke5 = self.dead[1]
            self.dead = []
        elif len(self.dead) == 2 and self.total_pokemon == 4:
            self.poke3 = self.dead[0]
            self.poke4 = self.dead[1]
            self.dead = []
        elif len(self.dead) == 2 and self.total_pokemon == 3:
            self.poke2 = self.dead[0]
            self.poke3 = self.dead[1]
            self.dead = []
        elif len(self.dead) == 1 and self.total_pokemon == 6:
            self.poke6 = self.dead[0]
            self.dead = []
        elif len(self.dead) == 1 and self.total_pokemon == 5:
            self.poke5 = self.dead[0]
            self.dead = []
        elif len(self.dead) == 1 and self.total_pokemon == 4:
            self.poke4 = self.dead[0]
            self.dead = []
        elif len(self.dead) == 1 and self.total_pokemon == 3:
            self.poke3 = self.dead[0]
            self.dead = []
        elif len(self.dead) == 1 and self.total_pokemon == 2:
            self.poke2 = self.dead[0]
            self.dead = []
        else:
            pass

    def menu(self):
        print('                                         ')
        print('=========================================')
        print('            Party     POKEMON            ')
        print('=========================================')
        if self.total_pokemon == 6:
            print('                                         ')
            print(' 1.', self.poke1.name,'lvl',self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name,'lvl', self.poke2.lvl)
            print('                                         ')
            print(' 3.', self.poke3.name,'lvl', self.poke3.lvl)
            print('                                         ')
            print(' 4.', self.poke4.name,'lvl', self.poke4.lvl)
            print('                                         ')
            print(' 5.', self.poke5.name,'lvl', self.poke5.lvl)
            print('                                         ')
            print(' 6.', self.poke6.name,'lvl', self.poke6.lvl)
            print('                                         ')
            print('=========================================')
        elif self.total_pokemon == 5:
            print('                                         ')
            print(' 1.', self.poke1.name, self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name, self.poke2.lvl)
            print('                                         ')
            print(' 3.', self.poke3.name, self.poke3.lvl)
            print('                                         ')
            print(' 4.', self.poke4.name, self.poke4.lvl)
            print('                                         ')
            print(' 5.', self.poke5.name, self.poke5.lvl)
            print('                                         ')
            print('=========================================')
        elif self.total_pokemon == 4:
            print('                                         ')
            print(' 1.', self.poke1.name, self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name, self.poke2.lvl)
            print('                                         ')
            print(' 3.', self.poke3.name, self.poke3.lvl)
            print('                                         ')
            print(' 4.', self.poke4.name, self.poke4.lvl)
            print('                                         ')
            print('=========================================')
        elif self.total_pokemon == 3:
            print('                                         ')
            print(' 1.', self.poke1.name, self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name, self.poke2.lvl)
            print('                                         ')
            print(' 3.', self.poke3.name, self.poke3.lvl)
            print('                                         ')
            print('=========================================')
        elif self.total_pokemon == 2:
            print('                                         ')
            print(' 1.', self.poke1.name, self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name, self.poke2.lvl)
            print('                                         ')
            print('=========================================')
        elif self.total_pokemon == 1:
            print('                                         ')
            print(' 1.', self.poke1.name, self.poke1.lvl)
            print('                                         ')
            print('=========================================')

    def pc(self):
        self.logged_in = True
        while self.logged_in == True:
            print('                                         ')
            print('=========================================')
            print("         Welcome to Bill's PC            ")
            print('=========================================')
            print(' 1. Check Box         2. Deposit POKEMON ')
            print('                                         ')
            print(' 3. Withdraw POKEMON  4. Exit            ')
            print('=========================================')
            print('                                         ')
            print('                                         ')
            choice = input('What action would you like to perform?: ')
            if choice == '1':
                self.pc_view()
                continue
            elif choice == '2':
                self.pc_deposit()
                continue
            elif choice == '3':
                self.pc_withdraw()
                continue
            elif choice == '4':
                print('                                         ')
                print('Have a good day, see you next time!')
                self.logged_in = False
            else:
                print('                                         ')
                print('Please choose a valid selection!')
                continue

    def pc_view(self):
        print('=========================================')
        print('Name', 'Type', 'HP', 'Attack', 'Defense', 'Speed')
        print('=========================================')
        for x in range(len(self.pc_box)):
            print(self.pc_box[x-1])

    def pc_deposit(self):
        print('                                         ')
        print('=========================================')
        print(' Choose a POKEMON to deposit into the PC ')
        print('=========================================')
        if self.total_pokemon == 6:
            print('                                         ')
            print(' 1.', self.poke1.name,'lvl',self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name,'lvl', self.poke2.lvl)
            print('                                         ')
            print(' 3.', self.poke3.name,'lvl', self.poke3.lvl)
            print('                                         ')
            print(' 4.', self.poke4.name,'lvl', self.poke4.lvl)
            print('                                         ')
            print(' 5.', self.poke5.name,'lvl', self.poke5.lvl)
            print('                                         ')
            print(' 6.', self.poke6.name,'lvl', self.poke6.lvl)
            print('                                         ')
            print('=========================================')
            choice = input('Please make your selection: ')
            if choice == '1':
                self.pc_box.append(self.poke1)
                print('                                         ')
                print(self.poke1.name,"lvl",self.poke1.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke1 = self.poke2
                self.poke2 = self.poke3
                self.poke3 = self.poke4
                self.poke4 = self.poke5
                self.poke5 = self.poke6
                self.poke6 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '2':
                self.pc_box.append(self.poke2)
                print('                                         ')
                print(self.poke2.name,"lvl",self.poke2.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke2 = self.poke3
                self.poke3 = self.poke4
                self.poke4 = self.poke5
                self.poke5 = self.poke6
                self.poke6 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '3':
                self.pc_box.append(self.poke3)
                print('                                         ')
                print(self.poke3.name,"lvl",self.poke3.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke3 = self.poke4
                self.poke4 = self.poke5
                self.poke5 = self.poke6
                self.poke6 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '4':
                self.pc_box.append(self.poke4)
                print('                                         ')
                print(self.poke4.name,"lvl",self.poke4.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke4 = self.poke5
                self.poke5 = self.poke6
                self.poke6 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '5':
                self.pc_box.append(self.poke5)
                print('                                         ')
                print(self.poke5.name,"lvl",self.poke5.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke5 = self.poke6
                self.poke6 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '6':
                self.pc_box.append(self.poke6)
                print('                                         ')
                print(self.poke6.name,"lvl",self.poke6.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke6 = 0
                self.total_pokemon -= 1
                pass
            else:
                print('Invalid Selection')
                pass
        elif self.total_pokemon == 5:
            print('                                         ')
            print(' 1.', self.poke1.name, self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name, self.poke2.lvl)
            print('                                         ')
            print(' 3.', self.poke3.name, self.poke3.lvl)
            print('                                         ')
            print(' 4.', self.poke4.name, self.poke4.lvl)
            print('                                         ')
            print(' 5.', self.poke5.name, self.poke5.lvl)
            print('                                         ')
            print('=========================================')
            choice = input('Please make your selection')
            if choice == '1':
                self.pc_box.append(self.poke1)
                print('                                         ')
                print(self.poke1.name,"lvl",self.poke1.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke1 = self.poke2
                self.poke2 = self.poke3
                self.poke3 = self.poke4
                self.poke4 = self.poke5
                self.poke5 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '2':
                self.pc_box.append(self.poke2)
                print('                                         ')
                print(self.poke2.name,"lvl",self.poke2.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke2 = self.poke3
                self.poke3 = self.poke4
                self.poke4 = self.poke5
                self.poke5 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '3':
                self.pc_box.append(self.poke3)
                print('                                         ')
                print(self.poke3.name,"lvl",self.poke3.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke3 = self.poke4
                self.poke4 = self.poke5
                self.poke5 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '4':
                self.pc_box.append(self.poke4)
                print('                                         ')
                print(self.poke4.name,"lvl",self.poke4.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke4 = self.poke5
                self.poke5 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '5':
                self.pc_box.append(self.poke5)
                print('                                         ')
                print(self.poke5.name,"lvl",self.poke5.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke5 = 0
                self.total_pokemon -= 1
                pass
            else:
                print('Invalid Selection')
                pass
        elif self.total_pokemon == 4:
            print('                                         ')
            print(' 1.', self.poke1.name, self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name, self.poke2.lvl)
            print('                                         ')
            print(' 3.', self.poke3.name, self.poke3.lvl)
            print('                                         ')
            print(' 4.', self.poke4.name, self.poke4.lvl)
            print('                                         ')
            print('=========================================')
            choice = input('Please make your selection')
            if choice == '1':
                self.pc_box.append(self.poke1)
                print('                                         ')
                print(self.poke1.name,"lvl",self.poke1.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke1 = self.poke2
                self.poke2 = self.poke3
                self.poke3 = self.poke4
                self.poke4 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '2':
                self.pc_box.append(self.poke2)
                print('                                         ')
                print(self.poke2.name,"lvl",self.poke2.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke2 = self.poke3
                self.poke3 = self.poke4
                self.poke4 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '3':
                self.pc_box.append(self.poke3)
                print('                                         ')
                print(self.poke3.name,"lvl",self.poke3.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke3 = self.poke4
                self.poke4 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '4':
                self.pc_box.append(self.poke4)
                print('                                         ')
                print(self.poke4.name,"lvl",self.poke4.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke4 = 0
                self.total_pokemon -= 1
                pass
            else:
                print('Invalid Selection')
                pass
        elif self.total_pokemon == 3:
            print('                                         ')
            print(' 1.', self.poke1.name, self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name, self.poke2.lvl)
            print('                                         ')
            print(' 3.', self.poke3.name, self.poke3.lvl)
            print('                                         ')
            print('=========================================')
            choice = input('Please make your selection')
            if choice == '1':
                self.pc_box.append(self.poke1)
                print('                                         ')
                print(self.poke1.name,"lvl",self.poke1.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke1 = self.poke2
                self.poke2 = self.poke3
                self.poke3 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '2':
                self.pc_box.append(self.poke2)
                print('                                         ')
                print(self.poke2.name,"lvl",self.poke2.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke2 = self.poke3
                self.poke3 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '3':
                self.pc_box.append(self.poke3)
                print('                                         ')
                print(self.poke3.name,"lvl",self.poke3.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke3 = 0
                self.total_pokemon -= 1
                pass
            else:
                print('Invalid Selection')
                pass
        elif self.total_pokemon == 2:
            print('                                         ')
            print(' 1.', self.poke1.name, self.poke1.lvl)
            print('                                         ')
            print(' 2.', self.poke2.name, self.poke2.lvl)
            print('                                         ')
            print('=========================================')
            choice = input('Please make your selection')
            if choice == '1':
                self.pc_box.append(self.poke1)
                print('                                         ')
                print(self.poke1.name,"lvl",self.poke1.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke1 = self.poke2
                self.poke2 = 0
                self.total_pokemon -= 1
                pass
            elif choice == '2':
                self.pc_box.append(self.poke2)
                print('                                         ')
                print(self.poke2.name,"lvl",self.poke2.lvl,"has been deposited into Bill's PC")
                print('                                         ')
                self.poke2 = 0
                self.total_pokemon -= 1
                pass
            else:
                print('Invalid Selection')
                pass
        else:
            print("You can't deposit your only POKEMON!")
            pass

    def pc_withdraw(self):
        if self.total_pokemon < 6:
            print('=========================================')
            print('Name', 'Level')
            print('=========================================')
            i = 0
            for x in self.pc_box:
                i += 1
                print(i,'.', x.name, 'lvl', x.lvl)
                print('=========================================')
            choice = int(input('Choose which pokemon you want to withdraw(#): '))
            print('=========================================')
            i = 0
            for x in self.pc_box:
                i += 1
                if i == choice:
                    if self.poke2 == 0:
                        self.poke2 = self.pc_box[i-1]
                        self.pc_box.pop(i-1)
                        print(self.poke2.name,'has been added to your party')
                        self.total_pokemon += 1
                        break
                    elif self.poke3 == 0:
                        self.poke3 = self.pc_box[i-1]
                        self.pc_box.pop(i-1)
                        print(self.poke3.name,'has been added to your party')
                        self.total_pokemon += 1
                        break
                    elif self.poke4 == 0:
                        self.poke4 = self.pc_box[i-1]
                        self.pc_box.pop(i-1)
                        print(self.poke4.name,'has been added to your party')
                        self.total_pokemon += 1
                        break
                    elif self.poke5 == 0:
                        self.poke5 = self.pc_box[i-1]
                        self.pc_box.pop(i-1)
                        print(self.poke5.name,'has been added to your party')
                        self.total_pokemon += 1
                        break
                    elif self.poke6 == 0:
                        self.poke6 = self.pc_box[i-1]
                        self.pc_box.pop(i-1)
                        print(self.poke6.name,'has been added to your party')
                        self.total_pokemon += 1
                        break
                else:
                    continue
        else:
            print('                                        ')
            print('You already have 6 POKEMON in your party')
            print('                                        ')
            print("Please deposit one before you try to make a withdrawal")
            print('                                        ')
            pass
#=======================Story Lines ======================================


    def introduction(self):
        while True:
            print('Oak: Hello there! Welcome to the world of POKEMON! My name is OAK!')
            sleep(2)
            print('                                         ')
            print('People call me the POKEMON PROF!')
            sleep(2)
            print('                                         ')
            print(r"""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⢀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠁⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠒⠊⠉⠉⠁⣽⣿⣿⡿⠋⠀⠀⠀⠀⣠⠖⠁⠀⠀⠈⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢀⠇⢀⣀⣀⣀⣀⣀⠀⠀⠀⢀⡠⠔⠊⠁⠀⠀⠀⠀⠀⠀⢠⣿⡿⠋⠁⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⡄⠀
            ⠀⠀⠀⠀⠀⠀⠀⢸⣀⠴⠋⠉⠁⠀⠀⠀⠀⠀⠉⠙⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠛⠁⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⢠⠀
            ⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⠀⣾⢙⣶⡄⠀⠀⠰⢤⣠⡤⠤⠔⠒⠂⠉⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀
            ⠀⠀⠀⠀⠀⠀⣮⣞⣹⠀⠀⠀⠀⠀⠀⠙⠿⠿⠃⠀⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠼⠃
            ⠀⠀⠀⠀⠀⢰⠛⠿⠁⣈⣀⣀⣀⣤⠀⠀⠀⢠⠖⠒⠲⡄⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⢰⠧⠤⠔⠂⠐⠈⠈⠀⠀⠀⣠⠔⠊⠁⠀⠀
            ⠀⠀⠀⠀⢠⡟⣇⠀⠉⢿⣿⣿⣿⣿⠀⠀⠀⢯⡐⠲⣠⡇⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⣠⠔⠋⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠸⣦⡟⠀⠀⠈⢿⠟⠛⢻⠀⠀⠀⠀⠙⠚⠋⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠳⣄⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⢀⣀⠬⠷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠚⠃⠢⢄⠀⠈⢣⡀⠀⠀⠀⠀⠀⢀⡽⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⣤⠔⠊⠁⠀⠀⠀⠈⠳⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⢿⠁⠀⠀⠀⠈⠀⠀⠘⡿⢆⠀⠀⣠⠔⠉⠀⠀⣀⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠐⡏⠸⠀⠀⠀⠀⠀⠀⠀⢢⠀⠈⠳⢄⣀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⣀⡀⠀⠀⠀⠱⡈⠣⡀⠀⢠⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠻⠦⢤⣀⠀⠀⠀⠀⠀⠀⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠤⠼⠛⠁⠀⠀⠀⠀⠘⣆⠙⢶⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠉⠉⠙⠒⠒⠒⠒⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠳⣾⣿⣿⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⡘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⣀⡤⠔⠲⣶⣆⣀⡀⠀⠐⠤⠤⠔⠒⠉⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠤⣥⠤⢴⠚⠉⠀⠀⠀⠈⠉⠒⠂⠤⠤⢤⡤⠞⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⣀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢋⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """)
            sleep(4)
            print('                                         ')
            print('Oak: This world is inhabited by creatures called POKEMON! For some')
            sleep(2)
            print('                                         ')
            print('people, POKEMON are pets. Others use them for fights. Myself...')
            sleep(2)
            print('                                         ')
            print('I study POKEMON as a profession.')
            sleep(3)
            print('                                         ')
            choice = input("Oak: First, what is your name?: ")
            if choice.isalpha() == False:
                print("Please only select letters!")
                continue
            else:
                sleep(2)
                print('Right! So your name is '+ choice)
                sleep(4)
                print(choice,'! Your very own POKEMON legend is about to unfold! A world of')
                print("dreams and adventures with POKEMON awaits! Let's go!")
                player.name = choice
                self.pallet_town()

    def pallet_town(self):
        while True:
            sleep(5)
            print(r"""
                #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
                #$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
                #$# [02'01] ---         Pallet Town         --- [02'01] #$#
                #$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
                #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
                    """)
            sleep(4)
            print('Mom: Well I guess all boys leave home some day.')
            print('It said so on TV.PROF.OAK, next door, is looking for you.')
            sleep(4)
            print('                                         ')
            print(self.name,': "Guess I need to head over to PROF.OAKS lab!"')
            sleep(3)
            print(r"""
                  #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
                  ##  Oak Pokemon Research Lab  #$
                  #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
                  """)
            sleep(4)
            print("You walk in to find PROF.OAK waiting with his grandson Gary...")
            sleep(2)
            print('                                         ')
            print("Gary: Gramps, I'm fed up with waiting!")
            sleep(2)
            print('                                         ')
            print("Oak: Gary? Let me think... Oh that's right, I told you to come! Just wait!")
            sleep(2)
            print('                                         ')
            print("Oak: Here", self.name, "! There are 3 POKEMON here! Haha! They are inside the POKE BALLS. When I was young, I was a serious POKEMON trainer. In my old age, I have only 3 left, but you can have one! Choose!")
            sleep(3)
            print('                                         ')
            print('Blue: Hey! Gramps! What about me?')
            sleep(2)
            print('                                         ')
            print('Oak: Be patient! Gary you can have one too!')
            sleep(2)
            print('                                         ')
            print('Oak: Now,', self.name,'which POKEMON do you want?')
            sleep(2)
            Bulbasaur.display()
            sleep(2)
            Squirtle.display()
            sleep(2)
            Charmander.display()
            print('======================')
            print('===  1. Bulbasaur  ===')
            print('======================')
            print('===  2. Squirtle   ===')
            print('======================')
            print('===  3. Charmander ===')
            print('======================')
            starter = input('Choose your first pokemon!: ')
            if starter == "1":
                #nickname = input('What would you like to call your new Bulbasaur?: ')
                starter = Bulbasaur(5)
                self.poke1 = starter
                #self.poke1.name = nickname
                self.total_pokemon += 1
                rivalstarter = Charmander(5)
            elif starter == "2":
                #nickname = input('What would you like to call your new Squirtle?: ')
                starter = Squirtle(5)
                self.poke1 = starter
                #self.poke1.name = nickname
                self.total_pokemon += 1
                rivalstarter = Bulbasaur(5)
            elif starter == "3":
                #nickname = input('What would you like to call your new Charmander?: ')
                starter = Charmander(5)
                self.poke1 = starter
                #self.poke1.name = nickname
                self.total_pokemon += 1
                rivalstarter = Squirtle(5)
            else:
                print('Please choose a valid input!') #come back later to fix
            gary.poke1 = rivalstarter
            sleep(3)
            print('Oak: Congratulations on picking your new', starter.name,'!')
            sleep(2)
            print("Oak: Now it's your turn to pick Gary!")
            sleep(2)
            print('Gary: Move over gramps, I already know which one I want')
            sleep(2)
            print('Gary has chosen ', rivalstarter.name, '!')
            sleep(2)
            print('Gary: My POKEMON looks a lot stronger.')
            sleep(3)
            print('Oak: A wonderful journey awaits you two. Better get started!')
            sleep(3)
            print("Gary: Wait ", self.name , "! Let's check out our POKEMON! Come on, I'll take you on!")
            sleep(3)
            self.gary_encounter(gary)

    def gary_encounter(self, target):
        self.battle(target)
        if self.victorious == True:
            sleep(5)
            print('                                         ')
            print('                                         ')
            print('Gary: WHAT? Unbelievable! I picked the wrong POKEMON!')
            sleep(2)
            print('                                         ')
            print("Gary: Okay! I'll make my POKEMON fight to toughen it up!")
            print('                                         ')
            print(self.name,"! Gramps! Smell you later!")
            sleep(2)
            print('                                         ')
            print('Gary walks out the door')
            sleep(2)
            self.post_battle()
        else:
            print('                                         ')
            print('                                         ')
            print('Gary: Nice try, but I clearly chose the stronger POKEMON!')
            sleep(2)
            print('                                         ')
            print(self.name,"! Gramps! Smell you later!")
            sleep(2)
            print('                                         ')
            print('Gary walks out the door')
            sleep(2)
            self.post_battle()

    def post_battle(self):
        
        sleep(2)
        print('                                         ')
        print('Oak:', self.name,'! I want you to take these')
        sleep(2)
        print('                                         ')
        print('PROF.OAK hands you several POKEBALLS')
        sleep(2)
        print('                                         ')
        print('Oak: POKEBALLS can be used to catch POKEMON in the wild.')
        print('                                         ')
        print('Oak: To become a POKEMON master, that was my dream!')
        print('                                         ')
        print("But, I'm too old! I can't do it! So, I want you two to fulfill my dream for me!")
        print('                                         ')
        sleep(2)
        print('Get moving, you two! This is a great undertaking in POKEMON history!')
        print('                                         ')
        sleep(2)
        print(self.name, 'to self... Better stop by home before I set out.')
        self.return_home()

    def return_home(self):
        print(r"""
              #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
              ##  Pallet Town  -  Your   house  #$
              #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
              """)
        sleep(3)
        print('                                         ')
        print('Mom: ',self.name,'! You should take a quick rest.')
        self.heal_team()
        sleep(4)
        print('                                         ')
        print('Mom: Oh good! You and your POKEMON are looking great!')
        print('The next town is VIRIDIAN CITY, but in order')
        print("to get their, you'll have to go through Route 1!")
        print('                                         ')
        print('Take care now!')
        sleep(4)
        print('                                         ')
        self.route1()

    def pokemon_center(self):
        print(r"""
              #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
              ##        POKEMON   CENTER        #$
              #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$
              """)
        sleep(3)
        print('                                         ')
        print('Nurse Joy: ',self.name,'! Your POKEMON look exhausted.')
        print("Let me heal them up for you!")
        self.heal_team()
        sleep(4)
        print('                                         ')
        print('                                         ')
        print('Nurse Joy: Your POKEMON are looking much healthier now!')
        print('Enjoy your stay in VIRIDIAN CITY!')
        print('                                         ')
        sleep(2)
        print('                                         ')
        print('1. Yes')
        print('                                         ')
        print('2. No')
        print('                                         ')
        choice = input('Would you like to use the PC? yes or no?: ')
        if choice == '1':
            self.pc()
            self.viridian_city()
        else: 
            sleep(4)
            print('                                         ')
            self.viridian_city()

    def route1(self):
        print('                                         ')
        print('                                         ')
        print(r"""
        #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
        #$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
        #$# [02'02] ---           Route 1           --- [02'02] #$#
        #$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
        #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
        """)
        print('                                         ')
        print('                                         ')
        sleep(2)
        print('Welcome to Route 1!')
        sleep(2)
        print('                                         ')
        print('Defeat or capture the POKEMON that')
        print('stand in your path to VIRIDIAN CITY,')
        print('or return home to heal your POKEMON.')
        sleep(2)
        print('                                         ')
        print('A wild POKEMON approaches!')
        self.wild_encounter(route1.fauna)
        sleep(2)
        while True:
            print('                                         ')
            print('Would you like to')
            print('                                         ')
            print('1. Continue to VIRIDIAN CITY')
            print('                                         ')
            print('2. Return home')
            print('                                         ')
            choice = int(input('What is your choice?: '))
            if choice == 1:
                sleep(2)
                print('                                         ')
                print('A wild POKEMON approaches!')
                sleep(2)
                self.wild_encounter(route1.fauna)
                sleep(2)
                while True:
                    print('                                         ')
                    print('Would you like to')
                    print('                                         ')
                    print('1. Continue to VIRIDIAN CITY')
                    print('                                         ')
                    print('2. Return home')
                    print('                                         ')
                    choice = int(input('What is your choice?: '))
                    if choice == 1:
                        print('                                         ')
                        print('A Trainer ambushes you!')
                        print('                                         ')
                        print('Youngster Joey wants to fight!')
                        print('                                         ')
                        self.victorious = False
                        sleep(2)
                        player.battle(youngster1)
                        if self.victorious == True:
                            self.victorious = False
                            self.viridian_city()
                        else:
                            self.return_home()
                    elif choice == 2:
                        self.return_home()
                    else:
                        print('Please   choose a valid choice.')
                        continue
            elif choice == 2:
                self.return_home()
            else:
                print('Please choose a valid choice.')
                continue
        
    def viridian_city(self):
        print('                                         ')
        print('                                         ')
        print(r"""
        #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
        #$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
        #$# [02'03] ---        Viridian City        --- [02'03] #$#
        #$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
        #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
        """)
        print('                                         ')
        print('                                         ')
        sleep(2)
        print('Welcome to VIRIDIAN CITY!')
        sleep(2)
        print('                                         ')
        sleep(2)
        while True:
            print('                                         ')
            print('Where would you like to go?')
            print('                                         ')
            print('1. POKEMON CENTER')
            print('                                         ')
            print('2. VIRIDIAN FOREST')
            print('                                         ')
            print('3. Route 22')
            print('                                         ')
            print('4. Back to PALLET TOWN')
            print('                                         ')
            print('5. View your party')
            print('                                         ')
            choice = input('What is your choice?: ')
            if choice == '1':
                self.pokemon_center()
                continue
            elif choice == '2':
                sleep(2)
                print('                                         ')
                print("I'm sorry, the road to VIRIDIAN FOREST is currently closed.")
                print('Better turn back around!')
                sleep(2)
                print('                                         ')
            elif choice == '3':
                self.route22()
            elif choice == '4':
                self.return_home()
            elif choice == '5':
                self.menu()
                continue
            else:
                print('                                         ')
                print('Please choose a valid choice')
                print('                                         ')
                continue

    def route22(self):
        print('                                         ')
        print('                                         ')
        print(r"""
        #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
        #$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
        #$# [02'02] ---           Route 22          --- [02'02] #$#
        #$#$#$#$#$#$#$                               $#$#$#$#$#$#$#
        #$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#
        """)
        print('                                         ')
        print('                                         ')
        sleep(2)
        print('Welcome to Route 22!')
        sleep(2)
        print('                                         ')
        print('Defeat or capture the POKEMON that')
        print('stand in your path to INDIGO PLATEAU,')
        print('or return to VIRIDIAN CITY.')
        sleep(2)
        print('                                         ')
        print('A wild POKEMON approaches!')
        self.wild_encounter(route22.fauna)
        sleep(2)
        while True:
            print('                                         ')
            print('Would you like to')
            print('                                         ')
            print('1. Continue to INDIGO PLATEAU')
            print('                                         ')
            print('2. Return to VIRIDIAN CITY')
            print('                                         ')
            choice = int(input('What is your choice?: '))
            if choice == 1:
                sleep(2)
                print('                                         ')
                print('A wild POKEMON approaches!')
                sleep(2)
                self.wild_encounter(route22.fauna)
                sleep(2)
                while True:
                    print('                                         ')
                    print('Would you like to')
                    print('                                         ')
                    print('1. Continue to INDIGO PLATEAU')
                    print('                                         ')
                    print('2. Return to VIRIDIAN CITY')
                    print('                                         ')
                    choice = int(input('What is your choice?: '))
                    if choice == 1:
                        print('                                         ')
                        sleep(3)
                        print('Gary: Hold up there! This path leads to the INDIGO PLATEAU')
                        print('                                         ')
                        print("Gary: If you want to make it to the Elite Four, you're going to have to go through me!")
                        sleep(2)
                        self.victorious = False
                        self.gary_encounter_2(gary)
                    elif choice == 2:
                        self.viridian_city()
                    else:
                        print('Please   choose a valid choice.')
                        continue
            elif choice == 2:
                self.viridian_city()
            else:
                print('Please choose a valid choice.')
                continue

    def gary_encounter_2(self, target):
        target.poke2 = target.poke1
        target.poke2.lvl = 11
        target.poke1 = Pidgey(9)
        target.poke2.hp = target.poke2.total_hp
        self.battle(target)
        if self.victorious == True:
            print('                                         ')
            print('Gary: If you want to make it to the ELITE FOUR,')
            print('you have to collect all 8 gym badges!')
            sleep(2)
            print("Gary: We'll see if you've got what it take to be champion!")
            sleep(2)
            print('                                         ')
            print(self.name,'to self: Better return to VIRIDIAN CITY...')
            sleep(2)
            self.viridian_city()
        else:
            print('                                         ')
            print('Gary: If you want to make it to the ELITE FOUR,')
            print("you'll have to do a lot better than that!")
            print('                                         ')
            sleep(2)
            self.viridian_city()

#============================================================================

class Trainer:
    def __init__(self, name, poke1, poke2, poke3, poke4, poke5, poke6 ):
        self.name = name
        self.poke1 = poke1
        self.poke2 = poke2
        self.poke3 = poke3
        self.poke4 = poke4
        self.poke5 = poke5
        self.poke6 = poke6

class Moves:
    def __init__(self,name, type, damage):
        self.name = name
        self.type = type
        self.damage = damage

############################################
############   Move List    ################
############################################
scratch = Moves('Scratch', 'normal', 40)
tackle = Moves('Tackle', 'normal', 35)
water_gun = Moves('Water Gun', 'water', 40)
ember = Moves('Ember', 'fire', 40)
vine_whip = Moves('Vine Whip', 'grass', 40)
gust = Moves('Gust', 'flying', 40)
thunder_shock = Moves('Thunder Shock', 'electric', 40)
poison_sting = Moves('Poison Sting', "poison", 40)
karate_chop = Moves('Karate Chop', 'fighting', 50)

############################################
############################################
############################################

class Pokemon:
    def __init__(self, lvl):
        self.name = 0
        self.lvl = lvl
        self.exp = 0
        self.power = 0
        self.total_hp = 0
        self.defense = 0
        self.speed = 0
        self.type = '0'
        self.fainted = False
        
    def attack(self, move, target):
        modifier = self.power / target.defense
        if move.type == 'grass':                         #1
            if target.type == 'water': 
                modifier *= 2
            elif target.type == 'fire':
                modifier /= 2
            elif target.type == 'normal':
                pass
            elif target.type == 'electric':
                pass
            elif target.type == 'grass':
                modifier /= 2
            elif target.type == 'flying':
                modifier /= 2
            elif target.type == 'poison':
                modifier /= 2
            elif target.type == 'fighting':
                pass
        elif move.type == 'water':                         #2
            if target.type == 'water':
                modifier /= 2
            elif target.type == 'fire':
                modifier *= 2
            elif target.type == 'normal':
                pass
            elif target.type == 'electric':
                pass
            elif target.type == 'grass':
                modifier /= 2
            elif target.type == 'flying':
                pass
            elif target.type == 'poison':
                pass
            elif target.type == 'fighting':
                pass
        elif move.type == 'fire':                            #3
            if target.type == 'water':
                modifier /= 2
            elif target.type == 'fire':
                modifier /= 2
            elif target.type == 'grass':
                modifier *= 2
            elif target.type == 'normal':
                pass
            elif target.type == 'electric':
                pass
            elif target.type == 'flying':
                pass
            elif target.type == 'poison':
                pass
            elif target.type == 'fighting':
                pass
        elif move.type == 'electric':                            #4
            if target.type == 'water':
                modifier *= 2
            elif target.type == 'fire':
                pass
            elif target.type == 'normal':
                pass
            elif target.type == 'electric':
                modifier /= 2
            elif target.type == 'grass':
                modifier /= 2
            elif target.type == 'flying':
                modifier *= 2
            elif target.type == 'poison':
                pass
            elif target.type == 'fighting':
                pass
        elif move.type == 'normal':                            #5
            if target.type == 'water':
                pass
            elif target.type == 'fire':
                pass
            elif target.type == 'normal':
                pass
            elif target.type == 'electric':
                pass
            elif target.type == 'grass':
                pass
            elif target.type == 'flying':
                pass
            elif target.type == 'poison':
                pass
            elif target.type == 'fighting':
                pass
        elif move.type == 'flying':                            #6
            if target.type == 'water':
                pass
            elif target.type == 'fire':
                pass
            elif target.type == 'normal':
                pass
            elif target.type == 'electric':
                modifier /= 2
            elif target.type == 'grass':
                modifier *= 2
            elif target.type == 'flying':
                pass
            elif target.type == 'poison':
                pass
            elif target.type == 'fighting':
                modifier *= 2
        elif move.type == 'poison':                              #7
            if target.type == 'water':
                pass
            elif target.type == 'fire':
                pass
            elif target.type == 'normal':
                pass
            elif target.type == 'electric':
                pass
            elif target.type == 'grass':
                modifier *= 2
            elif target.type == 'flying':
                pass
            elif target.type == 'poison':
                pass
            elif target.type == 'fighting':
                pass
        elif move.type == 'fighting':                           #8
            if target.type == 'water':
                pass
            elif target.type == 'fire':
                pass
            elif target.type == 'normal':
                pass
            elif target.type == 'electric':
                pass
            elif target.type == 'grass':
                pass
            elif target.type == 'flying':
                modifier /= 2
            elif target.type == 'poison':
                modifier /= 2
            elif target.type == 'fighting':
                pass
        else:
            pass
        damage = (math.floor(move.damage * modifier/7))
        print('The attack did',damage,'damage!')
        target.hp -= damage

        #receive a damage modifier based on unique values for (move)
        #interaction with (target) hp based on damage from move * attack/defense ratio
        #Ends the combat sequence if targets health is reduced to 0

    def exp_gain(self, target):
        self.exp += (target.lvl * target.total_hp)
        print(self.name, 'has', int(self.exp),'exp out of',25 + (self.lvl * 10),'needed for next level')
        if self.exp >= 25 + (self.lvl * 10):
            self.exp -= 25 + (self.lvl * 10)
            self.lvl += 1
            print(self.name, "has leveled up to lvl", self.lvl)

    def __str__(self): 
        return '{}, {}, {}, {}, {}, {},'.format(self.name, self.type.upper(), int(self.total_hp), int(self.power), int(self.defense), int(self.speed))
            


    def evolution(self, target):
        #transfer all current object info to a new object of the (target) pokemon subclass
        pass

class Bulbasaur(Pokemon):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = 'Bulbasaur'
        self.type = 'grass'
        self.move1 = tackle
        self.move2 = vine_whip
        self.lvl = lvl
        self.total_hp = (random.randrange(10, 12) + (lvl * 0.6))
        self.power = (random.randrange(5, 8) + (lvl * 0.4))
        self.defense = (random.randrange(8, 11) + (lvl * 0.6))
        self.speed = (random.randrange(4, 7) + (lvl * 0.4))
        self.hp = self.total_hp

    @classmethod
    def display(self):
        print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠈⡖⡤⠄⠀')
        print('⠀⠀⢀⡀⠀⠀⠀⡐⠁⠀⠀⠠⠐⠂⠀⠁⠀⠀⠀⠀')
        print('⠀⠰⡁⠐⢉⣉⣭⡍⠁⠂⠉⠘⡀⠀⠀⠀⠀⠂⠡⠀')
        print('⢀⣊⠀⡄⠻⠿⠋⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⢀')
        print('⡎⣾⠀⠁⣴⡆⠀⠡⢺⣿⣆⠀⢠⢱⣄⠀⠀⠀⠀⠈')
        print('⡑⠟⠀⠀⠀⠀⠀⢀⣸⡿⠟⠀⠀⠈⢿⣿⡦⡀⠀⡰')
        print('⠙⠔⠦⣤⣥⣤⣤⣤⡤⠆⠀⠀⠀⠀⢀⢀⠀⠈⠎⠀')
        print('⠀⠀⠈⣰⡋⢉⠉⠁⠒⠂⢇⢠⡆⠀⠸⢴⣿⠀⠘⠀')
        print('⠀⠀⠘⡿⠃⠀⠨⠒⢆⣸⣿⠁⠀⡠⡇⠈⠋⠀⠰⠀')
        print('⠀⠀⠀⠛⠒⠒⠁⠀⠈⠷⡤⠤⠐⠀⠘⠒⠒⠖⠁⠀')

    def __str__(self):
        return '{}, {}, {}, {}, {},'.format(self.name, self.total_hp, self.power, self.defense, self.speed)

class Squirtle(Pokemon):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = 'Squirtle'
        self.type = 'water'
        self.move1 = tackle
        self.move2 = water_gun
        self.lvl = lvl
        self.total_hp = (random.randrange(8, 12) + (lvl * 0.6))
        self.power = (random.randrange(10, 12) + (lvl * 0.6))
        self.defense = (random.randrange(12, 15) + (lvl * 0.7))
        self.speed = (random.randrange(6, 8) + (lvl * 0.4))
        self.hp = self.total_hp

    @classmethod
    def display(self):
        print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
        print('⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿')
        print('⣿⣿⣿⡇⢰⣿⣿⣿⣿⣿⠉⠉⢹⣿⣿⣿⣿⣿⣿⣿⡏⢱⣶⣶⣶⣶⡎⢹⣿⣿')
        print('⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣶⠉⠉⢹⣿⠉⢱⣿⣿⣿⠛⣿⣿⡇⢸⣿')
        print('⣿⡇⢈⣸⣿⣿⣿⡟⡛⠛⣿⣿⣧⡜⢻⣿⣿⣇⣀⠿⢿⣿⡇⢸⣿⣿⡿⢇⣸⣿')
        print('⣿⡇⢸⣿⣿⣿⣿⡇⢸⠉⣿⣿⣿⡇⠸⠿⢿⣿⣿⣀⡸⠇⢀⣀⣀⣀⣸⣿⣿⣿')
        print('⣿⣿⣧⣤⠛⠛⣿⣷⣶⣶⣿⡏⠉⢱⣶⣶⡆⢸⣿⣿⡇⢰⣾⣿⣿⣿⣿⣿⣿⣿')
        print('⣿⣿⣿⣿⣤⠛⠃⢠⣤⣤⡄⢸⣿⣿⣿⡏⠉⢹⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿')
        print('⣿⣿⣿⣿⣿⣿⡿⢇⣸⣿⣿⣇⣀⣀⣀⣀⡀⢸⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿')
        print('⣿⣿⣿⣿⣿⣿⣧⡜⠃⠈⠉⠉⢹⣿⣿⣿⡇⠸⢇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
        print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡄⢠⣤⣿⣧⡄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
        print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
        print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')
        print('⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿')

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.name, self.total_hp, self.power, self.defense, self.speed)

class Charmander(Pokemon):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = 'Charmander'
        self.type = 'fire'
        self.move1 = scratch
        self.move2 = ember
        self.lvl = lvl
        self.total_hp = (random.randrange(7, 9) + (lvl * 0.4))
        self.power = (random.randrange(9, 12) + (lvl * 0.6))
        self.defense = (random.randrange(5, 8) + (lvl * 0.4))
        self.speed = (random.randrange(8, 10) + (lvl * 0.6))
        self.hp = self.total_hp
        
    @classmethod
    def display(self):
        print('           ⣀⠤⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print('⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⠉⠀⠀⠀⠀⠀⠈⠑⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print('⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⣠⣄⠀⠈⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print('⠀⠀⠀⠀⠀⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⡸⢛⣷⡀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print('⠀⠀⠀⠀⠀⣠⡿⠋⠀⠀⠀⠀⠀⠀⢰⣷⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print('⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⢏⡏⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print('⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠋⠁⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print('⠀⠀⠀⠘⣦⡀⠐⠂⠠⠴⠀⠀⠀⠀⠀⠀⠀⣀⡴⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⢀⠀⠀⠀')
        print('⠀⢰⠦⣄⠈⢿⣶⡶⠤⠤⠤⠔⠒⠒⣶⠒⡫⢋⡄⠀⢸⠀⠀⠀⠀⢀⣀⠤⣤⠀⠀⠀⠀⠀⢀⡞⠉⠛⢆⠀⠀')
        print('⢰⡟⢷⠂⠉⠚⠿⣿⣄⣀⣀⣀⣠⣴⣛⣯⠔⠋⠀⠠⠼⠦⠔⠒⠊⠁⠠⡶⢧⡄⠀⠀⠀⠀⠸⣧⠀⡀⠈⣿⠀')
        print('⠀⠙⢮⡀⠀⠀⠀⠈⠉⡖⠛⠋⠉⠉⠁⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣥⠞⠁⠀⠀⠀⠀⠀⡏⠿⢧⢀⠈⡆')
        print('⠀⠀⠀⠙⢄⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⣇⠀⠸⣯⠀⡿')
        print('⠀⠀⠀⠀⠀⠓⢄⣠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠐⠒⢖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠉⣶⡇')
        print('⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣴⢦⠞⠁')
        print('⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⢸⠀⠀')
        print('⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠸⠀⠀')
        print('⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠁⢀⡇⠀⠀')
        print('⠀⠀⠀⠀⠀⠀⠀⡠⠚⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠤⠤⢤⣸⠓⠢⠄⢀⠀⠤⠔⠊⠁⠀⠀⡼⠀⠀⠀')
        print('⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⠀⠀⠀⠀')
        print('⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠈⠑⠦⣀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⢀⡠⠊⠀⠀⠀⠀⠀')
        print('⠀⠀⠀⠀⠀⠀⢳⡄⠀⠀⠀⠀⠀⢀⡜⠉⠉⠛⢧⠀⠀⠀⠀⠀⠀⣸⠥⣄⣀⣀⣀⠠⠖⠉⠀⠀⠀⠀⠀⠀⠀')
        print('⠀⠀⢀⣀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⢸⠇⠀⠀⠀⢀⣴⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print('⠀⠀⢿⣿⣷⣦⣀⣀⣀⡀⠤⠤⠤⠚⠁⠀⠀⠀⢸⡤⢤⡤⢤⡴⢤⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
        print('⠀   ⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠾⡷⠞⠿⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')

class Rattata(Pokemon):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = 'Rattata'
        self.type = 'normal'
        self.move1 = scratch
        self.move2 = tackle
        self.lvl = lvl
        self.total_hp = (random.randrange(5, 7) + (lvl * 0.3))
        self.power = (random.randrange(6, 9) + (lvl * 0.5))
        self.defense = (random.randrange(4, 7) + (lvl * 0.3))
        self.speed = (random.randrange(7, 9) + (lvl * 0.5))
        self.hp = self.total_hp

class Pidgey(Pokemon):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = 'Pidgey'
        self.type = 'flying'
        self.move1 = gust
        self.move2 = tackle
        self.lvl = lvl
        self.total_hp = (random.randrange(6, 8) + (lvl * 0.4))
        self.power = (random.randrange(7, 8) + (lvl * 0.5))
        self.defense = (random.randrange(4, 7) + (lvl * 0.4))
        self.speed = (random.randrange(9, 11) + (lvl * 0.6))
        self.hp = self.total_hp

class Pikachu(Pokemon):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = 'Pikachu'
        self.type = 'electric'
        self.move1 = thunder_shock
        self.move2 = tackle
        self.lvl = lvl
        self.total_hp = (random.randrange(5, 7) + (lvl * 0.4))
        self.power = (random.randrange(7, 10) + (lvl * 0.5))
        self.defense = (random.randrange(5, 7) + (lvl * 0.4))
        self.speed = (random.randrange(8, 10) + (lvl * 0.5))
        self.hp = self.total_hp

class Nidoran(Pokemon):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = 'Nidoran'
        self.type = 'poison'
        self.move1 = poison_sting
        self.move2 = tackle
        self.lvl = lvl
        self.total_hp = (random.randrange(5, 7) + (lvl * 0.4))
        self.power = (random.randrange(6, 8) + (lvl * 0.4))
        self.defense = (random.randrange(5, 7) + (lvl * 0.4))
        self.speed = (random.randrange(6, 8) + (lvl * 0.4))
        self.hp = self.total_hp

class Mankey(Pokemon):
    def __init__(self, lvl):
        super().__init__(lvl)
        self.name = 'Mankey'
        self.type = 'fighting'
        self.move1 = karate_chop
        self.move2 = tackle
        self.lvl = lvl
        self.total_hp = (random.randrange(5, 7) + (lvl * 0.4))
        self.power = (random.randrange(8, 10) + (lvl * 0.5))
        self.defense = (random.randrange(4, 6) + (lvl * 0.3))
        self.speed = (random.randrange(7, 9) + (lvl * 0.5))
        self.hp = self.total_hp

class Zone:
    def __init__(self, fauna:None):
        if fauna is None:
            self.fauna = []
        else:
            self.fauna = fauna

##############################################
#               Zone Encounters              #
##############################################
route1 = Zone(
    [Rattata((random.randrange(2, 5))), 
    Pidgey((random.randrange(2, 5))), 
    Pikachu((random.randrange(4, 6)))]
    )

route22 = Zone(
    [Pidgey((random.randrange(4, 6))), 
    Nidoran((random.randrange(5, 7))),
    Mankey(8)
    ]
)

###############################################
###############################################
player = Player(0)
gary = Trainer('Gary',0,0,0,0,0,0)
youngster1 = Trainer('Youngster Joey', Pidgey(6), Nidoran(7),0,0,0,0)



"""
# Wild encounter tester
player.poke1 = Pikachu(10)
while True:
    player.wild_encounter(route1.fauna)
    continue



PLAYTHROUGH TESTER

player.poke2 = Pikachu(20)
"""
player.introduction()






"""
PC TESTER

player.pc_box = [Pidgey('Pidgey', 1), Nidoran('Nidoran', 2),Pidgey('Pidgey', 3), Nidoran('Nidoran', 4),Pidgey('Pidgey', 5), Nidoran('Nidoran', 6),Pidgey('Pidgey', 7), Nidoran('Nidoran', 8)]
player.poke1 = Pikachu('Pikachu', 10)
player.total_pokemon +=1
player.pc()
"""

