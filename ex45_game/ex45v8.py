
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

            if next_scene_name in ['menu', 'inv']:
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

Welcome. Choose a name and class for your heroes.

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

        return jobs[info]

class Hero(object):

    lev = 0
    exp = 0
    mag = 0
    mdef = 0
    stre = 0
    defe = 0
    hp =  0
    mp = 0
    name = None
    speed = 0


    def __init__(self):
        self.initialize()

    def initialize(self):

        self.name = raw_input("Enter a hero name:\n> ")





class Warrior(Hero):


    sword = bronzesword
    helm = bronzehelm
    chest = bronzechestplate
    acc = None

    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 1
        self.mdef += 2
        self.stre += 5
        self.defe += 4
        self.hp *= 1.1
        self.mp += 10




class WhiteMage(Hero):

    sword = bronzesword
    helm = bronzehelm
    chest = bronzechestplate
    acc = None

    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 1
        self.mdef += 2
        self.stre += 5
        self.defe += 4
        self.hp *= 1.1
        self.mp += 10


class BlackMage(Hero):
    sword = bronzesword
    helm = bronzehelm
    chest = bronzechestplate
    acc = None

    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 1
        self.mdef += 2
        self.stre += 5
        self.defe += 4
        self.hp *= 1.1
        self.mp += 10

class Theif(Hero):
    sword = bronzesword
    helm = bronzehelm
    chest = bronzechestplate
    acc = None

    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 1
        self.mdef += 2
        self.stre += 5
        self.defe += 4
        self.hp *= 1.1
        self.mp += 10

class Opening(Scene):


    def enter(self):
        self.entrytext = """

    This is the start of a game.
    Press enter 1 for menu

    """
        formatborders(self.entrytext)
        prompt = raw_input("What do you want to do? : ")
        if prompt == "1":
            print "going to menu"

            return 'menu'

        else:
            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You finished"


class Monster(object):

    pass

class Menu(Scene):


    def enter(self, scene_name):


        print """

        1. Stats
        2. Inventory
        3. Magic
        4. Equipment
        5. Save
        6. Exit

        """
        choice = None

        while choice not in ["exit", "return", "6"]:

            choice = raw_input("What would  you like to do?")

            if choice in ['stats', 'Stats', '1']:
                self.stats(PARTY)
            if choice in ['inventory', 'Inventory', 'inv', 'Inv', '2']:
                return 'inv'


        return scene_name
    def stats(self, party):
        print "You accessed stats"
        print party.hero1.stre




class SubMenu(Scene):

    def enter(self, scene_name):
        print "You have accessed a submenu. It hasn't been initialized yet."
        return scene_name

class Inventory(SubMenu):

    def enter(self, scene_name):
        print "You have entered the inventory screen."
        return 'menu'

class MagicMenu(SubMenu):

    def enter(self, scene_name):
        print "You  have entered the magic menu. more to come"
        return 'menu'


class EquipmentMenu(SubMenu):

    def enter(self, scene_name):
        print "You have entered the equipment menu. More to come."
        return 'menu'

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

bronzehelm = Equipment('Bronze Helm', 1,0,5,3,10,0, 100)
bronzechestplate = Equipment('Bronze Chestplate', 1,0,10,5,0,0, 100)
bronzesword = Equipment('Bronze Sword', 10, 0, 0, 0, 0, 0, 100)
leatherhelm = Equipment('Leather Helm', 0, 1, 3, 5, 5, 10, 100)
leatherchestplate = Equipment('Leather Chestplate', 0, 1, 3, 11, 3, 0, 100)
woodenwand = Equipment('Wooden Wand', 0, 10, 0, 2, 0, 5, 100)





class Map(object):

    scenes = {
    'open' : Opening(),
    'finished' : Finished(),
    'menu' : Menu(),
    'inv' : Inventory()

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

def formatborders(textinput):
    print '=' * 20
    print textinput
    print '=' * 20

PARTY = Party()
a_map = Map('open')
a_game = Engine(a_map)
a_game.play()
