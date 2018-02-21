from charfile import Character
#from playerfile import Player

from random import randint #random here may not be required

class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'a goblin'
    self.health = randint(1, player.health)
    
