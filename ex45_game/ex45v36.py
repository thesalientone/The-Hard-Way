import pickle
from random import randint

class Engine(object):



    def __init__(self, scene_map):
        self.scene_map = scene_map




    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        prev_scene = self.scene_map.name_of_scene(current_scene)

        next_scene_name = current_scene.enter()
        current_scene = self.scene_map.next_scene(next_scene_name)


        while current_scene != last_scene:

            if next_scene_name in ['menu', 'inv', 'save', 'equip',
                                   'load', 'mhelp', 'debug']:
                if next_scene_name != 'menu':

                    next_scene_name = 'menu'




                else:

                    next_scene_name = current_scene.enter(prev_scene)
                    current_scene = self.scene_map.next_scene(next_scene_name)

            elif next_scene_name in ['help']:
                next_scene_name = current_scene.enter(prev_scene)
                current_scene = self.scene_map.next_scene(next_scene_name)


            else:

                if prev_scene not in [self.scene_map.towns, 'start'] and next_scene_name not in [self.scene_map.towns, 'start']:
                    if randint(0, 100) <= 35:
                        Battle().enter(prev_scene)
                next_scene_name = current_scene.enter()
                prev_scene = self.scene_map.name_of_scene(current_scene)
                current_scene = self.scene_map.next_scene(next_scene_name)


        current_scene.enter()



class Scene(object):

    def enter(self):
        print "scene not yet finished"

#Battle is a type of Scene


class Party(object):

    intro_text = """

Welcome. Choose a name and class for 4 heroes.

The following classes are available:

1. Warrior
2. White Mage
3. Black Mage
4. Theif

    """

    def __init__(self):

        formatborders(self.intro_text)
        self.hero1 = eval(self.change_job(self.get_job()))
        self.hero2 = eval(self.change_job(self.get_job()))
        self.hero3 = eval(self.change_job(self.get_job()))
        self.hero4 = eval(self.change_job(self.get_job()))
        self.inv = Inventory()
        self.initialize_inventory()



    def get_job(self):


        job = raw_input("Enter the job of your hero:\n> ")

        return  job

    def change_job(self, info):

        jobs = {
            'warrior' : "Warrior()",
            'Warrior' : "Warrior()",
            '1' : "Warrior()",
            'white mage' : "WhiteMage()",
            'White Mage' : "WhiteMage()",
            'white' : "WhiteMage()",
            '2' : "WhiteMage()",
            'black mage' : "BlackMage()",
            'Black Mage' : "BlackMage()",
            'black' : "BlackMage()",
            '3' : "BlackMage()",
            'theif' : "Theif()",
            'Theif' : "Theif()",
            '4' : "Theif()"


        }

        while info not in jobs.keys():
            print "You have not selected a proper job."
            formatborders(self.intro_text)
            info = self.get_job()
        return jobs[info]

    def get_party_members(self):
        party_members = [self.hero1, self.hero2, self.hero3, self.hero4]

        return party_members

    def initialize_inventory(self):
        self.inv.add_item(potion, 10)
        self.inv.add_item(ether, 5)
        self.inv.add_item(hipotion, 1)
        self.inv.add_item(hiether, 1)

        for hero in self.get_party_members():
            hero.initialize_equipment()

    def display_equipment(self):

        formatborders("EQUIPMENT: Equipment Stats are in the format HP/MP/ATT/MATT/PARM/MARM")
        party_members = self.get_party_members()
        print "NAME".ljust(7),
        for hero in party_members:
            print hero.name.ljust(15),
        print "\n", "JOB".ljust(7),
        for hero in party_members:
            print hero.job.ljust(15),
        print "\n", "WEAPON".ljust(7),
        for hero in party_members:
            print hero.sword.name.ljust(15),
        print "\n"
        print "\n", "".ljust(7),
        for hero in party_members:
            hero.sword.print_stats(),
        print "\n"
        print "\n", "HELM".ljust(7),
        for hero in party_members:
            print hero.helm.name.ljust(15),
        print "\n"
        print "\n", "".ljust(7),
        for hero in party_members:
            hero.helm.print_stats(),
        print "\n"
        print "\n", "CHEST".ljust(7),
        for hero in party_members:
            print hero.chest.name.ljust(15),
        print "\n"
        print "\n", "".ljust(7),
        for hero in party_members:
            hero.chest.print_stats(),
        print "\n"
        print "\n", "ACC".ljust(7),
        for hero in party_members:
            if hero.acc:
                print hero.acc.ljust(15),
            else:
                print 'NONE'.ljust(15),
        print "\n"

    def display_heros(self):
        print "\n"
        members = self.get_party_members()
        for i in range(4):
            class_name = members[i].__class__.__name__
            print i+1, ". %s" % members[i].name.ljust(10) , "(%s)" % class_name
        print "\n"

    def return_avg_levels(self):
        lvlavg = self.hero1.lev + self.hero2.lev + self.hero3.lev + self.hero4.lev
        lvlavg /= 4
        return lvlavg

    def display_hp(self):
        print "HP".ljust(10),
        heros = self.get_party_members()
        for hero in heros:
            print "%d/%d".ljust(10) % (hero.hp, hero.maxhp)


class Equipment(object):

    equip_stat_string_list = ['att', 'matt', 'parm', 'marm', 'health', 'mana', 'cost']
    def __init__(self, name, att, matt, parm, marm, health, mana, cost, armortype):
        self.name = name
        self.att = att
        self.matt = matt
        self.parm = parm
        self.marm = marm
        self.health = health
        self.mana = mana
        self.cost = cost
        self.armortype = armortype

    def return_stats(self):
        stat_list = [self.health, self.mana, self.att, self.matt, self.parm, self.marm]
        return stat_list
    def print_stats(self):
        stat_text = []
        for stat in self.return_stats():
            stat_text.append(str(stat))
        print "/".join(stat_text).ljust(15),

    def print_stats_inventory(self):
        print "NAME".ljust(10), self.name
        for stat in self.equip_stat_string_list:

            run_code = 'self.' + stat
            print stat.upper().ljust(10), eval(run_code)




class Accesory(Equipment):

    pass

class Item(object):

    def __init__(self, name, hp, mp, desc, itype):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.desc = desc
        self.itype = itype
#Equipment Declarations
bronzehelm = Equipment('Bronze Helm', 1,0,5,3,10,0, 100, 'whelm')
bronzechestplate = Equipment('Bronze Plate', 1,0,10,5,0,0, 100, 'wchest')
bronzesword = Equipment('Bronze Sword', 10, 0, 0, 0, 0, 0, 100, 'wwep')
leatherhelm = Equipment('Leather Helm', 0, 1, 3, 5, 5, 10, 100, 'mhelm')
leatherchestplate = Equipment('Leather Plate', 0, 1, 3, 11, 3, 0, 100, 'mchest')
woodenwand = Equipment('Wooden Wand', 0, 10, 0, 2, 0, 5, 100, 'mwep')
ironhelm = Equipment('Iron Helm', 0, 0, 15, 7, 0 , 0, 150, 'whelm')
ironchest = Equipment('Iron Chest', 0, 0, 15, 7, 0 , 0, 200, 'wchest')
potion = Item('Potion', 100, 0, 'Restores 100 HP', 'p')
ether = Item('Ether', 0, 20, 'Restores 200 MP', 'm')
hipotion = Item('Hi-Potion', 500, 0, 'Restores 500 HP', 'p')
hiether = Item('Hi-Ether', 0, 500, 'Restores 200 MP', 'm')

class Hero(object):




    def __init__(self):

        self.lev = 0
        self.exp = 0
        self.mag = 0
        self.mdef = 0
        self.stre = 0
        self.defe = 0
        self.maxhp = 0
        self.hp =  0
        self.maxmp = 0
        self.mp = 0
        self.name = None
        self.speed = 0
        self.job = self.__class__.__name__
        self.initialize()
        self.stats = {'name' : self.name,
                      'job' : self.job,
                      'lev' : self.lev,
                      'exp' : self.exp,
                      'mag' : self.mag,
                      'mdef' : self.mdef,
                      'stre' : self.stre,
                      'defe' :self.defe,
                      'hp' : self.hp,
                      'mp' : self.mp,
                      'speed' : self.speed}
        self.sword = None
        self.helm = None
        self.chest = None
        self.acc = None


    def initialize(self):

        self.name = raw_input("Enter a hero name:\n> ")
        if len(self.name) > 11 or len(self.name) < 1:
            print "Please Enter a hero name that is 10 characters or less."
            self.initialize()

    def return_stats(self):
        hero_stats = [self.name, self.lev, self.exp, self.mag, self.mdef,
                      self.stre, self.defe, self.hp, self.mp, self.speed,
                      self.maxhp, self.maxmp]
        return hero_stats

    def equip(self, equipment, eqtype):
        if eqtype == 'sword':
            self.sword = equipment
        if eqtype == 'helm':
            self.helm = equipment
        if eqtype == 'chest':
            self.chest = equipment
        if eqtype == 'acc':
            self.acc = equipment

    def set_stats(self, lev, exp, mag, mdef, stre, defe, hp, maxhp, mp, maxmp, speed):
        self.lev = lev
        self.exp = exp
        self.mag = mag
        self.mdef = mdef
        self.stre = stre
        self.defe = defe
        self.hp = hp
        self.mp = mp
        self.speed = speed
        self.maxhp = maxhp
        self.maxmp = maxmp





class Warrior(Hero):



    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 1
        self.mdef += 2
        self.stre += 5
        self.defe += 4
        self.maxhp *= 1.1
        self.maxmp += 10
        self.hp = self.maxhp
        self.mp = self.maxmp


    def initialize_equipment(self):
        self.equip(bronzesword, 'sword')
        self.equip(bronzehelm, 'helm')
        self.equip(bronzechestplate, 'chest')
        self.set_stats(1, 0, 5, 6, 9, 8, 100,100, 5, 5, 10)



class WhiteMage(Hero):



    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 4
        self.mdef += 6
        self.stre += 1
        self.defe += 1
        self.maxhp *= 1.05
        self.maxmp *= 1.1
        self.hp = self.maxhp
        self.mp = self.maxmp

    def initialize_equipment(self):
        self.equip(woodenwand, 'sword')
        self.equip(leatherhelm, 'helm')
        self.equip(leatherchestplate, 'chest')
        self.set_stats(1, 0, 10, 7, 1, 3, 60, 60, 60, 60, 10)

class BlackMage(Hero):



    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 7
        self.mdef += 4
        self.stre += 2
        self.defe += 1
        self.maxhp *= 1.06
        self.maxmp *= 1.1
        self.hp = self.maxhp
        self.mp = self.maxmp

    def initialize_equipment(self):
        self.equip(woodenwand, 'sword')
        self.equip(leatherhelm, 'helm')
        self.equip(leatherchestplate, 'chest')
        self.set_stats(1, 0, 10, 7, 1, 3, 60, 60, 60,  60, 10)

class Theif(Hero):



    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 1
        self.mdef += 2
        self.stre += 6
        self.defe += 2
        self.maxhp *= 1.07
        self.maxmp += 10
        self.hp = self.maxhp
        self.mp = self.maxmp

    def initialize_equipment(self):
        self.equip(bronzesword, 'sword')
        self.equip(bronzehelm, 'helm')
        self.equip(bronzechestplate, 'chest')
        self.set_stats(1, 0, 5, 6, 7, 8, 80, 80, 5, 5, 12)

class Monster(object):

    def __init__(self, lev):

        self.lev = lev
        self.exp = 0
        self.mag = 0
        self.mdef = 0
        self.stre = 0
        self.defe = 0
        self.maxhp = 0
        self.hp =  0
        self.maxmp = 0
        self.mp = 0

        self.speed = 0
        self.job = self.__class__.__name__

        self.stats = {'job' : self.job,
                      'lev' : self.lev,
                      'exp' : self.exp,
                      'mag' : self.mag,
                      'mdef' : self.mdef,
                      'stre' : self.stre,
                      'defe' :self.defe,
                      'hp' : self.hp,
                      'mp' : self.mp,
                      'speed' : self.speed}




class Slime(Monster):

    def __init__(self, lev):
        super(Slime, self).__init__(lev)

        self.adjust_stats()
    def adjust_stats(self):
        #print "Stats"
        self.hp = self.lev * 100
        self.maxhp = self.hp



class Inventory(object):

    item_dictionary = {
        'Potion' : potion,
        'Ether' : ether,
        'Hi-Potion' : hipotion,
        'Hi-Ether' : hiether,
        'Iron Helm' : ironhelm,
        'Iron Chest' : ironchest,
        'Bronze Helm' : bronzehelm,
        'Bronze Plate' : bronzechestplate,
        'Bronze Sword' : bronzesword,
        'Leather Helm' : leatherhelm,
        'Leather Plate' : leatherchestplate,
        'Wooden  Wand' : woodenwand
    }

    def __init__(self):
        self.contents = {}

    def add_item(self, item, amount):
        if item.name in self.contents.keys():
            self.contents[item.name] += amount
        else:
            self.contents[item.name] = amount

    def sub_item(self, item, amount):
        if item.name in self.contents.keys():
            self.contents[item.name] -= amount
            if self.contents[item.name] <= 0:
                del self.contents[item.name]


    def select_item(self, item_list):

        item_number = raw_input("Enter the number or of the item you wish to use:")

        try:
            item_to_use = self.item_dictionary[item_list[int(item_number) -1][1]]
            class_name = self.item_dictionary[item_list[int(item_number) -1][1]].__class__.__name__
            if class_name == "Item":
                if item_number:
                    print item_list[int(item_number) -1][1], " Description: \n"
                    print item_to_use.desc

                    return item_number, item_to_use

                else:
                    return None
            elif class_name == "Equipment":
                item_to_use.print_stats_inventory()
                return None
        except:
            print "Improper item number entered."
            formatborders("MENU")
            return None

    def select_equipment(self, item_list):
        item_number = raw_input("Enter the number of the item you wish to equip:")

        #try goes here
        item_to_use = self.item_dictionary[item_list[int(item_number) -1][1]]
        wep_type = item_to_use.armortype
        if item_number:
            PARTY.display_heros()
            hero_num = raw_input("Enter the number of the hero to equip the %s to: " % item_to_use.name)
            members = PARTY.get_party_members()
            if hero_num:
                hero = members[int(hero_num) - 1]
                if wep_type in ['whelm', 'mhelm']:
                    hero_wep_type = hero.helm.armortype
                    if wep_type == hero_wep_type:
                        formatborders(hero.name)
                        self.compare_equipment(hero.helm, item_to_use)
                        confirm_change = raw_input("Do you wish to change the equipment (Y/N): \n>")

                        if confirm_change in ['y', 'Y', 'yes', 'Yes', item_to_use.name]:
                            PARTY.inv.add_item(hero.helm, 1)
                            hero.helm = item_to_use
                            PARTY.inv.sub_item(item_to_use, 1)
                            print "%s successfully equipped. " % item_to_use.name
                    else:
                        print "This equipment is not for that class of hero."
                elif wep_type in ['wchest', 'mchest']:
                    hero_wep_type = hero.chest.armortype
                    if wep_type == hero_wep_type:
                        formatborders(hero.name)
                        self.compare_equipment(hero.chest, item_to_use)
                        confirm_change = raw_input("Do you wish to change the equipment (Y/N): \n>")

                        if confirm_change in ['y', 'Y', 'yes', 'Yes', item_to_use.name]:
                            PARTY.inv.add_item(hero.chest, 1)
                            hero.chest = item_to_use
                            PARTY.inv.sub_item(item_to_use, 1)
                            print "%s successfully equipped. " % item_to_use.name
                    else:
                        print "This equipment is not for that class of hero."
                elif wep_type in ['wwep', 'mwep']:
                    hero_wep_type = hero.sword.armortype
                    if wep_type == hero_wep_type:
                        formatborders(hero.name)
                        self.compare_equipment(hero.sword, item_to_use)
                        confirm_change = raw_input("Do you wish to change the equipment (Y/N): \n>")

                        if confirm_change in ['y', 'Y', 'yes', 'Yes', item_to_use.name]:
                            PARTY.inv.add_item(hero.sword, 1)
                            hero.sword = item_to_use
                            PARTY.inv.sub_item(item_to_use, 1)
                            print "%s successfully equipped. " % item_to_use.name
                    else:
                        print "This equipment is not for that class of hero."

                else:
                    print "Something went wrong. Don't save. You might ruin your file. "

            else:
                print "No hero selected."
                return None
        else:
            print "No item selected. "
            return None

            print "Enter proper item number. Returning to menu"
            return None

    def compare_equipment(self, equip1, equip2):

        print "NAME".ljust(10), equip1.name.ljust(15), equip2.name.ljust(15), "CHANGE"
        for stat in Equipment.equip_stat_string_list:
            old = eval('equip1.' + stat)
            new = eval('equip2.' + stat)
            diff = new - old
            if diff > 0:
                diff = '+' + str(diff)
            print stat.upper().ljust(10), str(old).ljust(15), str(new).ljust(15), diff




    def use_item(self, item):

        print "\n"
        members = PARTY.get_party_members()
        for i in range(4):
            print i+1, ". %s" % members[i].name.ljust(10),
        print "\n"

        hero_number = raw_input("Enter the number of the hero to use the %s on: " % item.name)
        if hero_number:
            try :
                hero = members[int(hero_number) - 1]
                #If using a potion to restore HP
                if item.itype == 'p':
                    hero_temp_stat = hero.hp
                    self.use_potion(item, hero)
                    self.sub_item(item, 1)
                    hero_temp_stat = hero.hp - hero_temp_stat

                    print "Restored %d health to %s. " % ( hero_temp_stat , hero.name)
                #If using a potion to restore mp
                if item.itype == 'm':
                    hero_temp_stat = hero.mp
                    self.use_potion(item, hero)
                    self.sub_item(item, 1)
                    hero_temp_stat = hero.mp - hero_temp_stat

                    print "Restored %d mana to %s. " % ( hero_temp_stat, hero.name)
            except:
                print "Improper hero number entered. Returning to menu."
                formatborders("MENU")
        else:
            print "No hero entered. Returning to menu. "
            formatborders("MENU")

    def use_potion(self, item, hero):

        hero_new_hp = hero.hp + item.hp

        if hero_new_hp >= hero.maxhp:
            hero.hp = hero.maxhp
        else :
            hero.hp = hero_new_hp

        hero_new_mp = hero.mp + item.mp
        if hero_new_mp >= hero.maxmp:
            hero.mp = hero.maxmp
        else:
            hero.mp = hero_new_mp


    def display_items(self, option):
        if option == 'item':
            pack = self.contents
        elif option == 'equip':
            pack = self.seive_equipment()

        else:
            pack = self.contents

        max_number = 20
        number_of_items = len(pack)

        enum = enumerate(pack.keys())
        numbered_list = list(enum)
        if number_of_items <= 20:
            for item in numbered_list:
                print item[0] + 1, ". ", item[1] , ": x", pack[item[1]]

        else:
            for row in range(0, max_number):

                for column in range(0, 4):
                    point = row + max_number * column
                    if point < number_of_items:
                        try:
                            print point + 1, numbered_list[point][0] + 1, ". ", numbered_list[point][1], ": x", pack[numbered_list[point][1]],
                        except:
                            pass

                print ""
        return numbered_list




    def seive_equipment(self):

        equipment_dictionary = {}

        for item_name in self.contents.keys():
            if self.item_dictionary[item_name].__class__.__name__ in ['Equipment', 'Accesory']:
                equipment_dictionary[item_name] = self.contents[item_name]


        return equipment_dictionary

class Opening(Scene):


    def enter(self):
        self.entrytext = """

    This is the start of a game.
    Press enter 1 for menu
    Press 2 to injure hero1 for testing
    Press 3 to add Iron Helm, Iron Chest for testing
    Enter 4 to go to the field.
    """
        formatborders(self.entrytext)


        prompt = raw_input("What do you want to do: \n>")
        if prompt in ['1', 'menu', 'Menu']:
            formatborders("MENU")

            return 'menu'
        elif prompt in ['2']:
            PARTY.hero1.hp -= 20
            print 'DIE HERO!!! Now his health is %d' % PARTY.hero1.hp
            return 'open'
        elif prompt in ['3']:
            PARTY.inv.add_item(ironhelm, 1)
            PARTY.inv.add_item(ironchest, 1)
            print "Added Iron Helm"
            return 'open'
        elif prompt in ['quit', 'q', 'exit', 'Exit']:
            print "Game Exiting. Thank you for playing."
            return 'finished'
        elif prompt in ['4', 'field', 'Field']:
            print "Going to field."
            return 'field_0_1'

        else:
            return 'open'

class GameStart(Scene):
    global PARTY


    def enter(self):
        global PARTY
        start_text = """

Python Fantasy
by Stefan Jenkins


1. New Game
2. Load Game
3. Help
4. Exit Game

        """
        formatborders(start_text)
        start_option = raw_input("Type a Number or Command:\n>")

        if start_option in ['1', 'new', 'New', 'n', 'N']:
            print "Starting New Game........"
            PARTY = Party()
            return 'open'

        elif start_option in ['2', 'load', 'Load', 'l', 'L']:
            print "Loading Save File........"
            load_data = self.check_memory_card()
            load_data.display_saves()

            load_slot = raw_input("Which file would you like to load: \n>")
            try:
                load_slot = int(load_slot)
            except:
                load_slot = 0


            if load_slot == 1:
                if load_data.save1:
                    PARTY = load_data.save1.party
                    return load_data.save1.scene_name
                else:
                    print "No save file found. Returning to start."
                    return 'start'
            if load_slot == 2:
                if load_data.save2:
                    PARTY = load_data.save2.party
                    return load_data.save2.scene_name
                else:
                    print "No save file found. Returning to start."
                    return 'start'
            if load_slot == 3:
                if load_data.save3:
                    PARTY = load_data.save3.party
                    return load_data.save3.scene_name
                else:
                    print "No save file found. Returning to start."
                    return 'start'
            if load_slot == 0:
                formatborders("Wrong slot name. Please enter 1,2, or 3. Returning to Start.")
                return 'start'
        elif start_option in ['3', 'help', 'Help', 'h', 'H']:
            return 'help'

        elif start_option in ['4', 'Exit', 'exit', 'q', 'Q', 'quit', 'Quit']:
            formatborders("Exiting game. Thank you for playing.")
            quit()


        else:
            print "Please select a proper option."
            return 'start'


    def check_memory_card(self):
        try :
            load_file = open('save.txt', 'r')
        except:
            load_file = open('save.txt', 'w')
        try:
            load_data = pickle.load(load_file)


        except:
            load_data = MemoryCard()

        load_file.close()
        return load_data


class Finished(Scene):

    def enter(self):
        print "You finished"


class Monster(object):

    pass

class Menu(Scene):


    def enter(self, scene_name):

        self.menu_text =  """

        1. Stats
        2. Inventory
        3. Magic
        4. Equipment
        5. Save
        6. Load
        7. Exit Menu
        8. Quit Game
        9. Help
        10. Debug Menu
        """
        print self.menu_text
        choice = None

        while choice not in ["exit", "return", "7", "q", "quit"]:

            choice = raw_input("What would  you like to do: \n>")

            if choice in ['stats', 'Stats', '1']:
                self.stats(PARTY)
                print self.menu_text
            if choice in ['inventory', 'Inventory', 'inv', 'Inv', '2', 'i', 'I']:
                return 'inv'
            if choice in ['save', 'Save', '5']:
                return 'save'
            if choice in ['4', 'equip' 'Equip', 'equipment', 'Equipment', 'e', 'E']:
                return 'equip'
            if choice in ['6', 'load', 'Load', 'l', 'L']:
                return 'load'
            if choice in ['8', 'quit', 'q', 'Q']:
                return 'finished'
            if choice in ['9', 'help', 'Help', 'h', 'H']:
                return 'mhelp'
            if choice in ['10', 'd']:
                return 'debug'


        return scene_name
    def stats(self, party):

        stat_names = ['name', 'job', 'lev', 'hp', 'mp', 'exp', 'mag', 'mdef',
                      'stre', 'defe', 'speed']

        formatborders("STATS")
        for stat in stat_names:

            print stat.upper().ljust(10),
            for heroname in party.get_party_members():
                state_code = 'heroname.' + stat

                print eval(state_code),
                if stat in  ['name', 'job']:
                    print ''.ljust(10 - len(eval(state_code))),
                elif stat in ['hp', 'mp']:
                    pass
                else:
                    print ''.ljust(10 - len(str(eval(state_code)))),
                if stat == 'hp':
                    print "/%d".ljust(10-len(str(heroname.maxhp))) % heroname.maxhp,
                if stat == 'mp':
                    print "/%d".ljust(10-len(str(heroname.maxmp))) % heroname.maxmp,

            print '\n',
        print "\n"
        raw_input("Press Enter")



class SubMenu(Scene):

    def enter(self, scene_name):
        print "You have accessed a submenu. It hasn't been initialized yet."
        return 'menu'

class InventoryMenu(SubMenu):

    def enter(self, scene_name):
        formatborders("INVENTORY")

        item_list = PARTY.inv.display_items('item')
        item_num_type = PARTY.inv.select_item(item_list)
        if item_num_type:
            PARTY.inv.use_item(item_num_type[1])
        return 'menu'

class MagicMenu(SubMenu):

    def enter(self, scene_name):
        print "You  have entered the magic menu. more to come"
        return 'menu'


class EquipmentMenu(SubMenu):

    def enter(self, scene_name):
        PARTY.display_equipment()
        equip_list = PARTY.inv.display_items('equip')
        PARTY.inv.select_equipment(equip_list)

        print "You have entered the equipment menu. More to come."
        return 'menu'

class SaveMenu(SubMenu):

    def enter(self, scene_name):


        load_data = self.check_memory_card()
        load_data.display_saves()
        save_slot = raw_input("Which slot do you want to use: \n>")

        try:
            save_slot = int(save_slot)
        except:
            save_slot = 0

        if save_slot in [1,2,3]:
            print "Saving game......."
            if save_slot == 1:
                load_data.save1 = Save()
                load_data.save1.save_game(scene_name)

            if save_slot == 2:
                load_data.save2 = Save()
                load_data.save2.save_game(scene_name)
            if save_slot == 3:
                load_data.save3 = Save()
                load_data.save3.save_game(scene_name)

            print "Saving Complete. Writing to file......."
            save_file = open('save.txt', "w+")
            pickle.dump(load_data, save_file)
            save_file.close()
        else:
            print "Improper save entered. Returning to menu. Game NOT saved."

        return 'menu'

    def check_memory_card(self):
        try :
            load_file = open('save.txt', 'r')
        except:
            load_file = open('save.txt', 'w')
        try:
            load_data = pickle.load(load_file)


        except:
            load_data = MemoryCard()

        load_file.close()
        return load_data

class LoadMenu(SubMenu):
    global PARTY

    def enter(self, scenename):
        global PARTY
        print "Loading Save File........"
        load_data = self.check_memory_card()
        load_data.display_saves()

        load_slot = raw_input("Which file would you like to load: \n>")
        try:
            load_slot = int(load_slot)
        except:
            load_slot = 0


        if load_slot == 1:
            if load_data.save1:
                PARTY = load_data.save1.party
                return load_data.save1.scene_name
            else:
                print "No save file found. Returning to Menu."
                return 'menu'
        if load_slot == 2:
            if load_data.save2:
                PARTY = load_data.save2.party
                return load_data.save2.scene_name
            else:
                print "No save file found. Returning to Menu."
                return 'menu'
        if load_slot == 3:
            if load_data.save3:
                PARTY = load_data.save3.party
                return load_data.save3.scene_name
            else:
                print "No save file found. Returning to Menu."
                return 'menu'
        if load_slot == 0:
            formatborders("Wrong slot name. Please enter 1,2, or 3. Returning to Menu.")
            return 'menu'

    def check_memory_card(self):
        try :
            load_file = open('save.txt', 'r')
        except:
            load_file = open('save.txt', 'w')
        try:
            load_data = pickle.load(load_file)


        except:
            load_data = MemoryCard()

        load_file.close()
        return load_data

class Field_0_1(Scene):

    text = """

    You have entered a field.

    1. Menu
    2. Go to town
    3. Go to field.

    """

    def enter(self):

        print self.text
        location = raw_input("Enter a number: \n>")

        if location in ['1', 'menu', 'Menu', 'm', 'M']:
            return 'menu'
        elif location in ['2', 'town', 'Town']:

            return 'town1'
        elif location in ['3', 'field', 'f', 'Field', 'F']:
            return 'field_1_1'
        else:
            return 'field_0_1'

class Field_1_1(Scene):

    text = """

    You have entered another field.

    1. Menu
    2. Go back to the field.

    """

    def enter(self):

        print self.text
        location = raw_input("Enter a number: \n>")

        if location in ['1', 'menu', 'Menu', 'm', 'M']:
            return 'menu'
        elif location in ['2', 'field', 'Field']:

            return 'field_0_1'
        else:
            return 'field_1_1'


class Town1(Scene):

    text = """

    You have entered a Town.

    1. Menu
    2. Go to field.

"""

    def enter(self):

        print self.text
        location = raw_input("Enter a number: \n>")

        if location in ['1', 'menu', 'Menu', 'm', 'M']:
            return 'menu'
        if location in ['2', 'field', 'Field']:
            return 'field_0_1'
        else:
            return 'town1'


class Battle(Scene):

    calmlands = [Slime]
    area_monsters = {
    'field_0_1' : calmlands,
    'field_1_1' : calmlands
    }

    monster_text = [
        "A random %s has appeared!",
        "A %s has suddently manifested. It looks angry.",
        "A %s looks at you and  you wet your pants. ",
        "You hear battle music start to play in your head as a %s charges you.",
        "POP! A %s begins twerking menacingly in your direction. ",
    ]


    def enter(self, current_area):
        print "Entering a battle from %s. " % current_area
        mobs = self.generate_monsters(current_area)
        formatborders("BATTLE")

        for monster in mobs:
            print self.monster_text[randint(0, len(self.monster_text) - 1)] % monster.__class__.__name__




    def generate_monsters(self, current_area):

        monster_pool = self.area_monsters[current_area]
        monster_amount = randint(1, 3)
        monsters = []
        level = PARTY.return_avg_levels()
        for n in range(monster_amount):
            monster_choices = len(monster_pool)
            monster_choice = randint(0, monster_choices - 1)
            monsters.append(monster_pool[monster_choice](level))

        return monsters


class Help(Scene):

    help_text = """

    Python Fantasy is a text based role playing game. You navagate through
screens by using the number of the command you wish to select, or typing out the
option itself.

    For example look at the following menu:

    1. Menu
    2. Inventory
    3. Stats
    4. Exit

    To access the menu you can enter 1, Menu, or menu. To access the Inventory
you can enter 2, Inventory, inv, or Inv. To exit you can enter 4, Exit, exit, or
anything other than the options given (q for instance).

    Entering q on most selection options will return you to the previous menu.
To exit the game, enter the menu and select option 8.

    Press Enter now to return.

    """

    def enter(self, scenename):

        formatborders("HELP")
        print self.help_text

        go_back = raw_input()

        return scenename

class MHelp(Scene):

    help_text = """

    Python Fantasy is a text based role playing game. You navagate through screens
by using the number of the command you wish to select, or typing out the option
itself.

    For example look at the following menu:

    1. Menu
    2. Inventory
    3. Stats
    4. Exit

    To access the menu you can enter 1, Menu, or menu. To access the Inventory
you can enter 2, Inventory, inv, or Inv. To exit you can enter 4, Exit, exit, or
anything other than the options given (q for instance).

    Entering q on most selection options will return you to the previous menu.

    Press Enter now to return.

    """

    def enter(self, scenename):

        formatborders("HELP")
        print self.help_text

        go_back = raw_input()

        return 'menu'

class Debug(Scene):

    def enter(self, scenename):

        print "Debug menu"


        slime1 = Slime(1)
        print slime1.hp


        option = raw_input("\n>")
        return 'menu'

class Map(object):

    scenes = {
    'open' : Opening(),
    'finished' : Finished(),
    'menu' : Menu(),
    'inv' : InventoryMenu(),
    'save' : SaveMenu(),
    'start' : GameStart(),
    'help' : Help(),
    'mhelp' : MHelp(),
    'equip' : EquipmentMenu(),
    'load' : LoadMenu(),
    'town1' : Town1(),
    'field_0_1' : Field_0_1(),
    'field_1_1' : Field_1_1(),
    'debug' : Debug(),
    'battle' : Battle()

    }

    towns = ['town1']


    invscenes = { v : k for k, v in scenes.items()}

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def name_of_scene(self, scene):
        val = Map.invscenes.get(scene)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)




class Save(object):




    def save_game(self, scene_name):
        self.scene_name = scene_name
        self.party = PARTY

class MemoryCard(object):
    def __init__(self):
        self.save1 = None
        self.save2 = None
        self.save3 = None

    def display_saves(self):
        formatborders("SAVE SLOTS")
        try:
            print "SLOT 1 : %s" % Map.scenes[self.save1.scene_name].__class__.__name__
            for hero in self.save1.party.get_party_members():
                print hero.name.upper().ljust(10), "LVL: ", str(hero.lev).ljust(2),
        except:
            print "SLOT 1 : EMPTY"
        print "\n"
        try:
            print "SLOT 2 : %s" % Map.scenes[self.save2.scene_name].__class__.__name__
            for hero in self.save2.party.get_party_members():
                print hero.name.upper().ljust(10), "LVL: ", str(hero.lev).ljust(2),
        except:
            print "SLOT 2 : EMPTY"
        print "\n"
        try :
            print "SLOT 3 : %s" % Map.scenes[self.save3.scene_name].__class__.__name__
            for hero in self.save3.party.get_party_members():
                print hero.name.upper().ljust(10), "LVL: ", str(hero.lev).ljust(2),
        except:
            print "SLOT 3 : EMPTY"
        print "\n"

        formatborders("Enter the slot number or press enter to return to previous screen")
        print  "\n"


def formatborders(textinput):
    print '=' * 80
    print textinput
    print '=' * 80

def nl():
    print "\n"

PARTY = None

a_map = Map('start')

a_game = Engine(a_map)
a_game.play()
