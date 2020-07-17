# Implement a class to hold room information. This should have name and
# description attributes.
class Room(object):
    def __init__(self, name, discription):
        self.name = name
        self.discription = discription
    def __str__(self):
        return self.name + self.discription
