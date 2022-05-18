class Tournament:
    def __init__(self, name, place, date, timing, description):
        self.name = name
        self.place = place
        self.date = date
        self.timing = timing
        self.description = description

    def __str__(self):
        return self.name