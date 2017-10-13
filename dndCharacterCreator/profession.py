from attribute import Attribute

import random

class Profession:
    professions = {}

    def __init__(self):
        self.name = None
        self.attributes = {}
        self.hitDie = None
        return

    # translates hit die number to print string
    # e.g. hitDie = 10, hitDieToStr = "d10"
    def hitDieToStr(self):
        return "d{}".format(self.hitDie)

    def setupAttributes(self, prefAttrStr):
        # ex: "STR CON|DEX" becomes
        # ["STR", "CON|DEX"] becomes
        # [["STR"], ["CON", "DEX"]]
        prefAttr = [x.split("|") for x in prefAttrStr.split()]
        for prefLvl, attrNames in enumerate(prefAttr):
            for attrName in attrNames:
                attr = Attribute.fromName(attrName)
                attr.preferrenceLvl = prefLvl
                self.attributes[attr.toShortName()] = attr
        # set preferrence to highest level (higher = less preferred)
        prefLvl += 1
        # add the rest of the attributes not in the list of preferred attributes
        for attrName in Attribute.attributes.keys():
            if attrName not in self.attributes.keys():
                # create new attribute
                newAttr = Attribute.fromName(attrName)
                # set preferrence level to lowest
                newAttr.preferrenceLvl = prefLvl
                # add attribute to profession's attribute list
                self.attributes[attrName] = newAttr
        return

    def getAttributeByName(self, attrName):
        return self.attributes[attrName]

    def getSortedAttrs(self):
        numAttrs = len(Attribute.attributes)
        sortedAttrs = [None]*numAttrs
        possiblePositions = [x for x in range(numAttrs)]
        for attr in self.attributes.values():
            position = attr.preferrenceLvl
            # if position is already filled, find new random position
            while sortedAttrs[position] is not None:
                random.shuffle(possiblePositions)
                position = possiblePositions.pop()
            sortedAttrs[position] = attr
        return sortedAttrs

    def toKey(self):
        return self.name.upper()

    @classmethod
    def addProfession(cls, profession):
        cls.professions[profession.toKey()] = profession
        return

    @classmethod
    def setupProfessions(cls, fileName):
        with open(fileName) as f:
            # skip header row
            next(f)
            for line in f:
                profession = Profession()
                # remove newline character
                line = line[:-1]
                name, prefAttrStr, hitDie = [x.strip() for x in line.split(",")]
                # set name
                profession.name = name
                # set preferred attributes
                profession.setupAttributes(prefAttrStr)
                # set hit die
                profession.hitDie = int(hitDie)
                # add to Profession.professions
                cls.addProfession(profession)
        return
