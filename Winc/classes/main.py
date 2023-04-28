# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line
class Player:
    def __init__(self, name, speed, endurance, accuracy):
        if not 0 <= speed <= 1:
            raise ValueError('Speed must be between 0 and 1')
        if not 0 <= endurance <= 1:
            raise ValueError('endurance must be between 0 and 1')
        if not 0 <= accuracy <= 1:
            raise ValueError('accuracy must be between 0 and 1')
        
        if name:
            self.name = name
        else:
            self.name = 'Bob'
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
    def introduce(self):
        return f'Hello everyone, my name is {self.name}.'
        # if self.name:
        #     return f'Hello everyone, my name is {self.name}.'
        # else:
        #     return f'Hello everyone, my name is Super Bob.'


if __name__ == '__main__':
    pl1 = Player('player1',1, 0, 0,)
    # pl1 = Player('',1, 0, 0)

    print(f"pl1.introduce -> {pl1.introduce()}")
    # pl2 = Player('pl2', 0, -1, 0)
    # pl3 = Player('pl3', 0, 0, -1)
    # pl4 = Player('pl4', -1, 0, 0)
    