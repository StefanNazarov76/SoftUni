from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'

        elif player.guild != 'Unaffiliated':
            return f'Player {player.name} is in another guild.'

        else:
            self.players.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'

    def kick_player(self, player_name):
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
            self.players.remove(player)
            player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        except StopIteration:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_details = '\n'.join(p.player_info() for p in self.players)

        return f'Guild: {self.name}\n'\
            f'{players_details}'


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
player_two = Player("Tom", 50, 100)
guild_two = Guild("test")
print(guild_two.assign_player(player_two))
print(guild.assign_player(player_two))
print(guild.kick_player("George"))

print(guild.guild_info())
