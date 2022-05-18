from ..Model import player as modelplayer
from ..Vue import Player

class PlayerController:
    def __init__(self):
        self.vue = Player.VuePlayer()

    def start(self):
        info_player = self.vue.add_newplayer()
        objet_player = Player.modelplayer(*info_player)