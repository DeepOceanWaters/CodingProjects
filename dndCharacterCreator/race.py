class Race:
    races = {}

    def __init__(self):
        self.name = None
        self.abilities = None
        return

    @classmethod
    def fromName(cls, name):
        newRace = cls()
        newRace.name = name
        return newRace

    @classmethod
    def addRace(cls, race):
        cls.races[race.name.upper()] = race
        return

    @classmethod
    def setupRaces(cls, fileName):
        with open(fileName) as f:
            # skip header row
            next(f)
            for line in f:
                name = line.strip()
                race = cls.fromName(name)
                cls.addRace(race)
        return
