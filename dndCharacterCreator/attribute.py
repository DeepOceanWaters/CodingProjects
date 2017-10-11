import copy

class Attribute():
    attributes = {}

    def __init__(self):
        self.name = None
        self.value = None
        self.preferrenceLvll = None
        return

    def toShortName(self):
        return self.name[:3].upper()

    @classmethod
    def fromName(cls, name):
        try:
            shortName = name[:3].upper()
            attr = copy.copy(cls.attributes[shortName])
        except KeyError:
            attr = cls()
            attr.name = name
        return attr

    @classmethod
    def addAttribute(cls, attr):
        attrKey = attr.toShortName()
        cls.attributes[attrKey] = attr
        return

    @classmethod
    def copyFromName(cls, name):
        if len(name) > 3:
            name = name[:3].upper()
        return copy.copy(attributes[name])

    @classmethod
    def setupAttributes(cls, fileName):
        with open(fileName) as f:
            # skip header row
            next(f)
            for line in f:
                name = line.strip()
                attribute = cls.fromName(name)
                cls.addAttribute(attribute)

        return
