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
    
    def compare_players(self, pl1, pl2, pl_arg):
        winner = ''
        pl1_score = getattr(pl1, pl_arg)
        pl2_score = getattr(pl2, pl_arg)
        pl1_name = getattr(pl1, 'name')
        pl2_name = getattr(pl2, 'name')
        pl1_strength_method = getattr(pl1, 'strength')
        pl2_strength_method = getattr(pl2, 'strength')
        p1_sum = self.sum_player(pl1)
        p2_sum = self.sum_player(pl2)
        
        if pl1_score == pl2_score:
            if pl1_strength_method()[1] == pl2_strength_method()[1]:
                if p1_sum == p2_sum:
                    return f"These two players might as well be twins!"
                elif p1_sum > p2_sum:
                        return pl1_name
                else: 
                    return pl2_name
            elif pl1_strength_method()[1] > pl2_strength_method()[1]:
                return pl1_name
            else: 
                return pl2_name    
        else:
            if pl1_score > pl2_score:
                return pl1_name
            else: 
                return pl2_name  
                
        
        
if __name__ == '__main__':
    # pl1 = Player('pl1',0.7, 0.9, 0.9)
    # pl2 = Player('pl2', 0.8, 0.8, 1)
    ray = Commentator('Ray Hudson')
    alice = Player('Alice', 0.3, 0.2, 0.5)
    bob = Player('Bob', 0.3, 0.2, 0.5)
    print(ray.compare_players(alice, bob, 'speed'))
    