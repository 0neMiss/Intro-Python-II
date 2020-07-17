from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("outside",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])
# Write a loop that:
#
print(player.room)
running = True
while(running == True):
    print(player.room)
    direction = input('enter a cardinal direction')
    if direction == 'east':
        try:
            player.room = room[player.room.name].e_to
            print(player.room)
        except AttributeError:
            print('wrong way idiot')
            pass
    elif direction == 'west':
        try:
            player.room = room[player.room.name].w_to
            print(player.room)
        except AttributeError:
            print('wrong way idiot')
            pass
    elif direction == 'north':
        try:
            player.room = room[player.room.name].n_to
            print(player.room)
        except AttributeError:
            print('wrong way idiot')
            pass
    elif direction == 'south':
        try:
            player.room = room[player.room.name].s_to
            print(player.room)
        except AttributeError:
            print('wrong way idiot')
            pass
    elif direction == 'q':
        break

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
