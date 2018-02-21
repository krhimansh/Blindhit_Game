from playerfile import Player
p = Player()
p.name = input("What is your character's name? ")
print ("type help to get a list of actions)\n")
print ("%s enters a dark cave, searching for adventure." % (p.name))
 
Commands = p.Commands

while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print ("%s doesn't understand the suggestion." % (p.name))
      
      if __name__ == '__main__':
          p=Player()
          print("It's working")
          