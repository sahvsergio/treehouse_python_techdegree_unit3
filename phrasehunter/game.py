# Create your Game class logic in here.
#create game class
import copy
import random
class Game:
    # The class should include an initializer or def __init__ method t
    def __init__(self):
        #method that sets the following attributes:
        self.missed=0
        self.phrases = [
            'Go confidently in the direction of your dreams Live the life you\'ve imagined',
            'Success usually comes to those who are too busy to be looking for it.'
            'Leave nothing for tomorrow which can be done today'
            'Whatever the mind of man can conceive and believe  it can achieve.'
            'Dont find fault, find a remedy anyone can complain.']
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


        self.active_phrase=self.get_random_phrase()

        print(self.active_phrase)


        # Calls the welcome method
        self.welcome()
        hidden_phrase=''
        #game loop
        for  letter in self.active_phrase.lower():
            if letter.isalpha():
                hidden_phrase+='_'
            elif letter.isspace():
                hidden_phrase+=' '
        print(hidden_phrase)

        while self.missed<5:
            
            user_guess=self.get_guess()
            try:
                if user_guess in self.active_phrase:
                    print(hidden_phrase)
                else:
                    self.missed+=1
                    self.guesses.append(user_guess)

            except TypeError:
                print('Please enter a letter, not a number')

                
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


        try: 
            user_guess=str(input('Guess a letter: ').lower())
            #check if the guess is actually a  letter, not a number  
            if user_guess.isalpha():
                self.guesses.append(user_guess)
            elif len(user_guess)>1:
                raise Exception('Please enter only 1 letter')
            else:
                raise Exception('Please enter a letter not a number')
        except Exception as e:
            print(e)
        else:
            print(self.guesses)
            return str(user_guess)

            
    def get_random_phrase(self):
        
        '''
        Randomly retrieves one of the phrases stored in the phrases list and returns it.
        '''
        copied_phrases=copy.deepcopy(self.phrases)
        self.active_phrase=random.choice(copied_phrases)
        return self.active_phrase


   