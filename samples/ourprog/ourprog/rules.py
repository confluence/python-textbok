class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self, title):
        if title not in self.TITLES:
            raise ValueError("Unrecognised title: '%s'" % title)

        return "%s %s %s" % (title, self.name, self.surname)
