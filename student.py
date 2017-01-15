#encoding: utf8
__author__ = 'Rafael Almeida 68486'
__email__ = 'almeidarafael@ua.pt'

__author__ = 'João Quintanilha 68065'
__email__ = 'jpquintanilha@ua.pt'

__author__ = 'Fábio Costa '
__email__ = 'fabioUrso@ua.pt'

__version__ = "0.1"
import card
import random
from player import Player

class StudentPlayer(Player):
    def __init__(self, name="Meu nome", money=0):
        super(StudentPlayer, self).__init__(name, money)

    def play(self, dealer, players):
        return "s"

    def bet(self, dealer, players):
        return 1 
