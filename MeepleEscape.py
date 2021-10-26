# gameplay code

from Game import week
from Lib import restricted_input, validated_input
from Village import Village


print("Welcome to Meeple Escape!")

print("You will have to manage a Village by reassigning jobs to help you Meeples escape the Village")
print("Enter the number of Farmers, Doctors, and Researchers you want to start with:")
f = validated_input("Farmers: ", int)
d = validated_input("Doctors: ", int)
r = validated_input("Researchers: ", int)

game_village = Village()
game_village.populate(f, d, r)

print("Here is your Village:")
print(game_village)

while True:
    if week(game_village): break
    print("input 'f', 'd', 'r' and an id to change a Meeple's job to farmer, doctor, or reseacher")
    print("input 'done' when finished or 'q' to quit game")
    command = ''
    while not command == 'done':
        usr_in = input('enter command > ').split(' ')
        command = usr_in[0]
        id = 0
        if command == 'q':
            exit()
        elif command == 'done':
            break
        try:
            if len(usr_in) > 1:
                id = int(usr_in[1])
            else:
                print('must indicate id of meeple')
        except:
                print('id must be integer')
        if (command in ['f','d','r']) and id < len(game_village.meeples):
            game_village.reassign(id, command)
            print(f"reassigned: {game_village.meeples[id]}")
        else:
            print('invalid command')
            

print(game_village.end_report)