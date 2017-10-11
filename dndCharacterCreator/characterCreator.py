# This is the main program
# Purpose is to create a randomly generated Dungeons and Dragons character
# This includes: name, race, class, attributes (e.g. STR/DEX/etc.)

# This uses DnD 5th edition as reference

from attribute import Attribute
from character import Character
from profession import Profession
from race import Race

import copy
import random

def main():
    # add race OR replace races
    # add class OR replace classes
    # add names OR replace names
    # determine how attributes are set:
    #   - use array
    #   - use random
    #   - use point buy system
    #
    # setup names
    firstNamesFile = "Info/firstNames.txt"
    lastNamesFile = "Info/lastNames.txt"
    firstNames = setupNames(firstNamesFile)
    lastNames = setupNames(lastNamesFile)
    # setup attributes
    attributesFile = "Info/attributes.txt"
    Attribute.setupAttributes(attributesFile)
    # setup professions
    professionsFile = "Info/professions.txt"
    Profession.setupProfessions(professionsFile)
    # setup races
    racesFile = "Info/races.txt"
    Race.setupRaces(racesFile)
    # create the Character
    character = createCharacter(firstNames, lastNames)
    # print the Character
    print("\n")
    character.printCharacter()
    print("\n")
    return

def createCharacter(firstNames, lastNames):
    character = Character()
    # determine name
    genName(character, firstNames, lastNames)
    # determine profession
    genProfession(character)
    # determine race
    genRace(character)
    # set attributes
    genAttributes(character)
    return character

def genName(character, firstNames, lastNames):
    character.firstName = random.choice(firstNames)
    character.lastName = random.choice(lastNames)
    return

def genProfession(character):
    professions = list(Profession.professions.values())
    profession = random.choice(professions)
    character.profession = copy.copy(profession)
    return

def genRace(character):
    races = list(Race.races.values())
    character.race = random.choice(races)
    return

def genAttributes(character):
    numAttributes = len(Attribute.attributes)
    attrVals = [random.randint(2, 18) for x in range(numAttributes)]
    attrVals.sort(reverse=True)
    character.setAttributes(attrVals)
    return

# Get names from a file
def setupNames(fileName):
    names = []
    with open(fileName) as f:
        for line in f:
            name = line[:-1]
            names.append(name)
    return names

if __name__ == "__main__":
    main()
