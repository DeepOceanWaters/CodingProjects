from attribute import Attribute
from profession import Profession
from race import Race

import copy
import random

class Character:
    # random character generation guideline variables
    #   names
    firstNames = []
    lastNames = []
    #   attributes
    #       'a' = standard array
    #       'b' = point-buy system
    #       'r' = random
    attrGenStyle = 'a'
    #       range of possible random attribute values
    attrRandRange = (2, 18)
    #       standard array
    stdAttrArray = [15, 14, 13, 12, 10, 8]


    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.race = None
        self.profession = None
        self.attributes = {}
        self.attrGenStyle = Character.attrGenStyle
        # self.personality = None
        return



    def printCharacter(self):
        print("{} {} the {} {}".format(
            self.firstName,
            self.lastName,
            self.race.name,
            self.profession.name))
        for attr in self.attributes.values():
            print("{:>15}: {:>2}".format(attr.name, attr.value))
        return

    # setup character generation variables

    @classmethod
    def addNames(cls, firstNamesFile, lastNamesFile):
        cls.addFirstNames(firstNamesFile)
        cls.addLastNames(lastNamesFile)
        return

    @classmethod
    def addFirstNames(cls, fileName):
        firstNames = cls.setupNames(fileName)
        cls.firstNames.extend(firstNames)
        return

    @classmethod
    def addLastNames(cls, fileName):
        lastNames = cls.setupNames(fileName)
        cls.lastNames.extend(lastNames)
        return

    @classmethod
    def setupNames(cls, fileName):
        names = []
        with open(fileName) as f:
            for line in f:
                name = line[:-1]
                names.append(name)
        return names

    @classmethod
    def setAttributeGenStyle(cls, genStyle):
        cls.attrGenStyle = genStyle
        return

    # random character generation related functions

    @classmethod
    def initRandomCharacter(cls, attrGenStyle=None):
        character = cls()
        # set attribute generation style if specified for both obj and class
        if attrGenStyle is not None:
            character.attrGenStyle = cls.attrGenStyle = attrGenStyle
        # determine name
        character.genNewName()
        # determine profession
        character.genNewProfession()
        # determine race
        character.genNewRace()
        # set attributes
        character.genNewAttributes()
        return character

    def genNewName(self):
        self.firstName = random.choice(Character.firstNames)
        self.lastName = random.choice(Character.lastNames)
        return

    def genNewRace(self):
        races = list(Race.races.values())
        self.race = random.choice(races)
        return

    def genNewProfession(self):
        professions = list(Profession.professions.values())
        profession = random.choice(professions)
        self.profession = profession
        return

    def genNewAttributes(self, genStyle=None):
        # if generation style specified
        if genStyle is not None:
            self.attrGenStyle = attrGenStyle
        else:
            genStyle = self.attrGenStyle
        # use appropriate generation style
        if genStyle == 'a':
            self._genAttrsStdArray()
        elif genStyle == 'r':
            self._genAttrsRandom()
        elif genStyle == 'b':
            self._genAttrsPointBuy()
        else:
            raise Exception(
                    "Unknown style of attribute generation: {}"
                    .format(Character.attrGenStyle))
        return

    def _genAttrsStdArray(self):
        self._setAttributesFromValues(Attribute.standardArray)
        return

    def _genAttrsRandom(self):
        # get array of attributes with random values
        numAttributes = len(Attribute.attributes)
        attrVals = [random.randint(2, 18) for x in range(numAttributes)]
        attrVals.sort(reverse=True)
        # set attributes
        self._setAttributesFromValues(attrVals)
        return

    def _genAttrsPointBuy(self):
        return

    def _setAttributesFromValues(self, attrVals):
        attrs = self.profession.getSortedAttrs()
        for attr in attrs:
            newAttr = copy.copy(attr)
            newAttr.value = attrVals.pop(0)
            self.attributes[newAttr.toShortName] = newAttr
        return


    def randomize(self):
        return
