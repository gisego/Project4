class VuePlayer:
    # def add_existantplayer(self):
    #     pass

    def add_newplayer(self):
        firstname = input('First name: ')
        lastname = input('Last name: ')
        birthdate = input('Birthdate format(dd/mm/yyyy): ')
        gender = input('Gender (F/M): ')
        ranking = input('Ranking: ')

        new_player_info = [firstname, lastname, birthdate, gender, ranking]
        return new_player_info
