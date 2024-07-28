# Create your Game class logic in here.
#create game class
class Game:
    # The class should include an initializer or def __init__ method t
    def __init__(self):
        #method that sets the following attributes:
        self.missed=0
        self.phrases = [
            'Go confidently in the direction of your dreams! Live the life you\'ve imagined',
            'Success usually comes to those who are too busy to be looking for it.'
            'Leave nothing for tomorrow which can be done today'
            'Whatever the mind of man can conceive and believe, it can achieve.'
            'Don\'t find fault, find a remedy: anyone can complain.']
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
        while self.missed>5:
            #calls the get_guess method
            self.get_guess()

        else:
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
        if 
        print('game_over')
        
        pass
    