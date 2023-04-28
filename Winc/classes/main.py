# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line
# Part 1: Players
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

    def strength(self):
        if self.speed >= self.endurance and self.speed >= self.accuracy:
            return ('speed', self.speed)
        elif self.endurance >= self.accuracy:
            return ('endurance', self.endurance)
        else:
            return ('accuracy', self.accuracy)

# Part 2: Commentators
class Commentator:
    def __init__(self, name):
        self.name = name
        
    def sum_player(self, player):
        speed = getattr(player, 'speed')
        endurance = getattr(player, 'endurance')
        accuracy = getattr(player, 'accuracy')
        return speed + endurance + accuracy

if __name__ == '__main__':
    pl1 = Player('pl1',0.7, 0.9, 0.9)
    ray = Commentator('Ray Hudson')
    # print(ray.name)
    print(ray.sum_player(pl1))
    