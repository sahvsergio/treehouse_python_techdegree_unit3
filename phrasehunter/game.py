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
        # Calls the welcome method
        self.welcome()
        #game loop


        #calls the get_guess method
        self.get_guess()

        #calls the game_over method
        self.game_over()



    def get_random_phrase(self):
        '''
        randomly retrieves one of the phrases
        stored in the phrases list 
        and returns it.
        '''
        pass

    def welcome(self):
        '''
        prints a friendly welcome message to the user
        at the start of the game
        '''
        welcome_message='''
        Welcome to the phrase hunter game.

        You will be presented with a hidden  phrase and your job
        is to guess it , entering letter by letter

        '''.center(127)
        print(welcome_message)
        return None


    def get_guess(self):
        '''
      
        '''
        
        pass

    def game_over(self):
        '''
        -displays a friendly win or loss message
        -ends the game
        '''
        print('game_over')
        
        pass
    