import pickle

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

            if next_scene_name in ['menu', 'inv', 'save', 'equip', 'load']:
                if next_scene_name != 'menu':

                    next_scene_name = 'menu'




                else:

                    next_scene_name = current_scene.enter(prev_scene)
                    current_scene = self.scene_map.next_scene(next_scene_name)


            else:

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
        print "\n", "HELM".ljust(7),
        for hero in party_members:
            print hero.helm.name.ljust(15),
        print "\n", "CHEST".ljust(7),
        for hero in party_members:
            print hero.chest.name.ljust(15),
        print "\n", "ACC".ljust(7),
        for hero in party_members:
            if hero.acc:
                print hero.acc.ljust(15),
            else:
                print 'NONE'.ljust(15),
        print "\n"





class Equipment(object):

    def __init__(self, name, att, matt, parm, marm, health, mana, cost):
        self.name = name
        self.att = att
        self.matt = matt
        self.parm = parm
        self.marm = marm
        self.health = health
        self.mana = mana
        self.cost = cost

class Accesory(Equipment):

    pass

class Item(object):

    def __init__(self, name, hp, mp, desc):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.desc = desc
#Equipment Declarations
bronzehelm = Equipment('Bronze Helm', 1,0,5,3,10,0, 100)
bronzechestplate = Equipment('Bronze Plate', 1,0,10,5,0,0, 100)
bronzesword = Equipment('Bronze Sword', 10, 0, 0, 0, 0, 0, 100)
leatherhelm = Equipment('Leather Helm', 0, 1, 3, 5, 5, 10, 100)
leatherchestplate = Equipment('Leather Plate', 0, 1, 3, 11, 3, 0, 100)
woodenwand = Equipment('Wooden Wand', 0, 10, 0, 2, 0, 5, 100)
potion = Item('Potion', 100, 0, 'Restores 100 HP')
ether = Item('Ether', 0, 20, 'Restores 200 MP')
hipotion = Item('Hi-Potion', 500, 0, 'Restores 500 HP')
hiether = Item('Hi-Ether', 0, 500, 'Restores 200 MP')

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







class Warrior(Hero):



    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 1
        self.mdef += 2
        self.stre += 5
        self.defe += 4
        self.hp *= 1.1
        self.mp += 10

    def initialize_equipment(self):
        self.equip(bronzesword, 'sword')
        self.equip(bronzehelm, 'helm')
        self.equip(bronzechestplate, 'chest')



class WhiteMage(Hero):



    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 4
        self.mdef += 6
        self.stre += 1
        self.defe += 1
        self.hp *= 1.05
        self.mp *= 1.1

    def initialize_equipment(self):
        self.equip(woodenwand, 'sword')
        self.equip(leatherhelm, 'helm')
        self.equip(leatherchestplate, 'chest')

class BlackMage(Hero):



    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 7
        self.mdef += 4
        self.stre += 2
        self.defe += 1
        self.hp *= 1.06
        self.mp *= 1.1

    def initialize_equipment(self):
        self.equip(woodenwand, 'sword')
        self.equip(leatherhelm, 'helm')
        self.equip(leatherchestplate, 'chest')

class Theif(Hero):



    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 1
        self.mdef += 2
        self.stre += 6
        self.defe += 2
        self.hp *= 1.07
        self.mp += 10

    def initialize_equipment(self):
        self.equip(bronzesword, 'sword')
        self.equip(bronzehelm, 'helm')
        self.equip(bronzechestplate, 'chest')


class Inventory(object):

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
        else:
            self.contents[item.name] = 0

    def display_items(self):
        max_number = 20
        number_of_items = len(self.contents)

        enum = enumerate(self.contents.keys())
        numbered_list = list(enum)
        if number_of_items <= 20:
            for item in numbered_list:
                print item[0] + 1, ". ", item[1] , ": x", self.contents[item[1]]



        else:
            for row in range(0, max_number):

                for column in range(0, 4):
                    point = row + max_number * column
                    if point < number_of_items:
                        try:
                            print point + 1, numbered_list[point][0] + 1, ". ", numbered_list[point][1], ": x", self.contents[numbered_list[point][1]],
                        except:
                            pass

                print ""



class Opening(Scene):


    def enter(self):
        self.entrytext = """

    This is the start of a game.
    Press enter 1 for menu

    """
        formatborders(self.entrytext)


        prompt = raw_input("What do you want to do: \n>")
        if prompt in ['1', 'menu', 'Menu']:
            formatborders("MENU")

            return 'menu'
        elif prompt in ['quit', 'q', 'exit', 'Exit']:
            print "Game Exiting. Thank you for playing."
            return 'finished'

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
        7. Exit

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
                    print ''.ljust(10),
                if stat == 'hp':
                    print "/%d".ljust(10) % heroname.maxhp,
                if stat == 'mp':
                    print "/%d".ljust(10) % heroname.maxmp,

            print '\n'



class SubMenu(Scene):

    def enter(self, scene_name):
        print "You have accessed a submenu. It hasn't been initialized yet."
        return 'menu'

class InventoryMenu(SubMenu):

    def enter(self, scene_name):
        formatborders("INVENTORY")

        PARTY.inv.display_items()
        return 'menu'

class MagicMenu(SubMenu):

    def enter(self, scene_name):
        print "You  have entered the magic menu. more to come"
        return 'menu'


class EquipmentMenu(SubMenu):

    def enter(self, scene_name):
        PARTY.display_equipment()
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

class Help(Scene):

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

    Press Enter now to return to the main menu.

    """

    def enter(self):

        formatborders("HELP")
        print self.help_text

        go_back = raw_input()

        return 'start'

class Map(object):

    scenes = {
    'open' : Opening(),
    'finished' : Finished(),
    'menu' : Menu(),
    'inv' : InventoryMenu(),
    'save' : SaveMenu(),
    'start' : GameStart(),
    'help' : Help(),
    'equip' : EquipmentMenu(),
    'load' : LoadMenu()

    }


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


PARTY = None

a_map = Map('start')

a_game = Engine(a_map)
a_game.play()
