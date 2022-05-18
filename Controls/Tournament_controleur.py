from ..Model import Tournament as modeltournament
from ..Vue import  Tournament

class TournamentController:
    def __init__(self):
        self.vue = Tournament.VueTournament()

    def start(self):
        info_tournament = self.vue.tournament_data()
        objet_tournament = modeltournament.Tournament(*info_tournament)
