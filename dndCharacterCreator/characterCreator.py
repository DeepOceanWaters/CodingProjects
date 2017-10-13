#!/usr/bin/python

# This is the main program
# Purpose is to create a randomly generated Dungeons and Dragons character
# This includes: name, race, class, attributes (e.g. STR/DEX/etc.)

# This uses DnD 5th edition as reference

# TODO: add ability to choose attribute allocation:
#           - using standard array
#           -
#       add ability to choose gender:
#           - binary or non-binary
#
#       choose to be multi-racial:
#           - randomly create a lineage of races:

from attribute import Attribute
from character import Character
from profession import Profession
from race import Race

import copy
import random
import sys

def main():
    # determine how attributes are set:
    #   - use array
    #   - use random
    #   - use point buy system
    #
    # set default attribute generation style to: standard array
    attrGenStyle = "a"
    # set default range for the random attribute generation style
    attrRandRange = range(2, 18)
    # remove the program name from argv
    args = sys.argv[1:]
    # iterate over the arguments
    while args:
        arg = args.pop(0)
        if arg == "--help":
            print("")
            print("Below are command-line arguments you can use:")
            print("    Attribute Creation")
            print("       -a: use standard array (default)")
            print("       -r: use random values (range 2-18)")
            print("           [num a] [num b]:  (range a-b)")
            print("       -b: use point-buy system")
            print("")
            return
        # set attribute generation style to: random
        elif arg == "-r":
            attrGenStyle = "r"
            # peak ahead unless there are no more arguments
            if args:
                arg = args[0]
                if arg[0] is not '-':
                    rangeMin = int(args.pop(0))
                    rangeMax = int(args.pop(0))
                    attrRandRange = range(rangeMin, rangeMax)
        # set attribute generation style to: point-buy system
        elif arg == "-b":
            attrGenStyle = "b"
        # set attribute generation style to: standard array
        elif arg == "-a":
            attrGenStyle = "a"
        # unknown argument, raise exception
        else:
            raise Exception("""Unrecognized command-line argument: {}.\n
                               Use --help for more information""".format(arg))
    # setup names
    firstNamesFile = "Info/firstNames.txt"
    lastNamesFile = "Info/lastNames.txt"
    Character.addNames(firstNamesFile, lastNamesFile)
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
    character = Character.initRandomCharacter(attrGenStyle)
    # print the Character
    print('')
    character.printCharacter()
    print('')
    return

if __name__ == "__main__":
    main()
