
class Engine(object):

    pass


class Map(object):

    pass


class Scene(object):

    pass

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

        print self.intro_text
        self.hero1 = Hero()
        self.hero2 = Hero()
        self.hero3 = Hero()
        self.hero4 = Hero()




class Hero(object):

    lev = 0
    exp = 0
    mag = 0
    mdef = 0
    stre = 0
    defe = 0
    hp =  0
    name = None


    def __init__(self):
        self.initialize()

    def initialize(self):

        self.name = raw_input("Enter a hero name:\n> ")
        self.job = raw_input("Enter the job of your hero:\n> ")
        self  = self.job_change(self.job)


    def job_change(self, new_job):

        jobs = { 'warrior' : Warrior(),
                 '1' : Warrior(),
                 'white mage' : WhiteMage(),
                 '2' : WhiteMage(),
                 'black mage' : BlackMage(),
                 '3' : BlackMage(),
                 'theif' : Theif(),
                 '4' : Theif(),
                 '5' : Theif()

        }
        self = jobs[new_job]
        return self 

class Warrior(Hero):

    def __init__(self):
        print "you made a %s " % self.__class__.__name__

    def level_up(self):
        self.lev +=1
        self.exp = 0
        self.mag += 1
        self.mdef += 2
        self.stre += 5
        self.defe += 4
        self.hp *= 1.1




class WhiteMage(Hero):
    def __init__(self):
        print "you made a %s " % self.__class__.__name__

class BlackMage(Hero):
    def __init__(self):
        print "you made a %s " % self.__class__.__name__
class Theif(Hero):
    def __init__(self):
        print "you made a %s " % self.__class__.__name__
class Opening(Scene):


    def enter(self):
        print """

    This is the start of a game. Enter the name of your first hero.

    """



class Monster(object):

    pass

party = Party()
