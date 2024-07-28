# Create your Game class logic in here.
#create game class
class Game:
    # The class should include an initializer or def __init__ method t
    def __init__(self):
        #method that sets the following attributes:
        self.missed=0
        self.phrases:List=['Hello',]
        self.active_phrase=None
        self.guesses=[]

    
    def start(self):
        '''
        -Calls the welcome method, 
        -Creates the game loop, 
        -Calls the get_guess method, 
        -Adds the user's guess to guesses, 
        -Increments the number of missed by one if the guess is incorrect, 
        -Calls the game_over method.

        '''
        pass


    def get_random_phrase(self):
        '''
        randomly retrieves one of the phrases
        stored in the phrases list 
        and returns it.
        '''
        pass

    def welcome(self):
        pass


    def get_guess(self):
        '''
        prints a friendly welcome message to the user 
        at the start of the game
        '''
        pass

    def game_over():
        '''
        -displays a friendly win or loss message
        -ends the game'''
        
        pass
    