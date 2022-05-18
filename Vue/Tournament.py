class VueTournament:
    def tournament_data(self):

        name = input('Name of tournament: ')
        place = input('Place of tournament: ')
        date = input('Date of tournament: (format : DD/MM/YYYY)')
        timing = input('Bullet, blitz or rapid chess: ')
        description = input('Description: ')

        tournament_info = [name, place, date, timing, description]
        # print(tournament_info)
        return tournament_info