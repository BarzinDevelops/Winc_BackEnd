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
        return sum([ getattr(player, 'speed'),
                     getattr(player, 'endurance'),
                     getattr(player, 'accuracy')])
    
    def compare_players(self, pl1, pl2, pl_attr):      
        # compare based on player attribute: 'speed', 'endurance' and 'accuracy' 
        if getattr(pl1, pl_attr) > getattr(pl2, pl_attr):
            return pl1.name
        elif getattr(pl2, pl_attr) > getattr(pl1, pl_attr): 
            return pl2.name 
        
        # compare based on result of Player -> strength() method:
        pl1_strength = getattr(pl1, 'strength')
        pl2_strength = getattr(pl2, 'strength')
        if pl1_strength()[1] > pl2_strength()[1]:
            return pl1.name
        elif pl2_strength()[1] > pl1_strength()[1]:
            return pl2.name
        
        #  compare based on result of self.strength() method:
        if self.sum_player(pl1) > self.sum_player(pl2):
            return pl1.name
        elif self.sum_player(pl2) > self.sum_player(pl1):
                return pl2.name
            
        # if all comparisons result equal:
        return f"These two players might as well be twins!" 
                
        
        
if __name__ == '__main__':
    alice = Player("Alice", 0.8, 0.2, 0.6)
    bob = Player("Bob", 0.5, 0.2, 0.6)
    candice = Player("Candice", 0.8, 0.2, 0.7)
    dirk = Player("Dirk", 0.5, 0.2, 0.6)
    eric = Player("Eric", 0.5, 0.2, 0.6)
    
    print(alice.strength())
    print(bob.introduce())
    
    ray = Commentator('Ray Hudson')

    print(ray.compare_players(alice, bob, 'speed'))
    print(ray.compare_players(alice, candice, "accuracy"))
    print(ray.compare_players(dirk, eric, "speed"))