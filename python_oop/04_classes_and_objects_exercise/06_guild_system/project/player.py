class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        self.skills[skill_name] = mana_cost
        return f'Skill {skill_name} added to the collection of the player {self.name}'

    def player_info(self):
        skills = '\n'.join(f'==={skill_name} - {mana_cost}' for skill_name, mana_cost in self.skills.items())

        return f'Name: {self.name}\n'\
               f'Guild: {self.guild}\n'\
               f'HP: {self.hp}\n'\
               f'MP: {self.mp}\n'\
               f'{skills}'
