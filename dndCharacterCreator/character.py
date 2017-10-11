from attribute import Attribute

import copy

class Character:
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.race = None
        self.profession = None
        self.attributes = {}

    def setAttributes(self, attrVals):
        attrs = self.profession.attributes
        for attrKey, attr in attrs.items():
            newAttr = copy.copy(attr)
            prefLvl = attr.preferrenceLvl
            attrVal = attrVals[prefLvl]
            while attrVal is None:
                prefLvl += 1
                attrVal = attrVals[prefLvl]
            attrVals[prefLvl] = None
            newAttr.value = attrVal
            self.attributes[attrKey] = newAttr
        return

    def printCharacter(self):
        print("{} {} the {} {}".format(
            self.firstName,
            self.lastName,
            self.race.name,
            self.profession.name))
        for attr in self.attributes.values():
            print("{:>15}: {:>3}".format(attr.name, attr.value))
        return
