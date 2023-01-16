import time
import random

class User():
    name = ""
    highest_score = ""
    curr_position  = None

    def __init__(self, name_):
        self.name = name_

    def update_curr_position(self, curr_pos):
        self.curr_position = curr_pos




class Board():
    #cubes = [100]
    
    dict_num = 0
    snakes_index = {
        32:10,
        34:6,
        48:26,
        62:18,
        88:24,
        95:56,
        97:78
    }  # cutomized snake tail and mouth
    ladder_index = {
        80:99,
        71:92,
        28:74,
        50:67,
        10:32,
        21:42,
        4:14,
        8:30
    } # customized ladder up and down 
    user_current_idx = 0
    game_loop = True
    user_obj = None

    def __init__(self, user_):
        self.user_obj = user_
    
    
    def random_generator(self):
        self.dice_num = random.choice([1,2,3,4,5,6])
    
    def play_the_game(self):
        
        self.random_generator()
        print "Rolling Dice..."
        time.sleep(2)
        print self.dice_num
        
        self.user_current_idx += self.dice_num
        if self.user_current_idx in self.snakes_index:
            print "Umm.. snake bit you!"
            self.user_current_idx = self.snakes_index[self.user_current_idx]
        elif self.user_current_idx in self.ladder_index:
            print "wow, you got ladder"
            self.user_current_idx = self.ladder_index[self.user_current_idx]

        self.user_obj.update_curr_position(self.user_current_idx)
            
        if self.user_current_idx >= 100:
            print "Congrats, you have won"
            print "Winner is {}".format(self.user_obj.name) 
            self.game_loop = False

        print "{}'s current position: {}".format(self.user_obj.name, self.user_current_idx)
            


while(True):
    print "Welcome to Snake-Ladder Game"
    print "============================"
    print "\n"

    print "\nWant to Play Again?...press Y, otherwise N"
    choice_input = (raw_input())
    print choice_input
    if choice_input == 'Y':
        pass
    else:
        print "GoodBye !"
        break


    user1 = User("Manish")
    user2 = User("Lenin")

    user1_board = Board(user1)
    user2_board = Board(user2)
    
    while(user1_board.game_loop and user2_board.game_loop):
        print "--------------------------"
        print "{}'s Turn".format(user1.name)
        user1_board.play_the_game()
        print "\n------------------------\n"
        time.sleep(1)
        print "{}'s Turn".format(user2.name)
        user2_board.play_the_game()
     
    
    
    
     
    
