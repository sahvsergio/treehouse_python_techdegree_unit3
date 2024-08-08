from .phrase import Phrase
import random
import copy

class Game:

    def __init__(self)->None:
        self.missed=0
        self.phrases=[
            Phrase('Go confidently in the direction of your dreams Live the life you have imagined'),
            Phrase('Success usually comes to those who are too busy to be looking for it.'),
            Phrase('Leave nothing for tomorrow which can be done today'),
            Phrase('Whatever the mind of man can conceive and believe  it can achieve.'),
            Phrase('Dont find fault, find a remedy anyone can complain.')
            ]
        self.active_phrase=None
        self.guesses=[]
        return None
    
    def start(self):
        '''
        -Calls the welcome method,
        -Creates the game loop,
        -Calls the get_guess method,
        -Adds the user's guess to guesses,
        -Increments the number of missed by one if the guess is incorrect,
        -Calls the game_over method.

        '''

        #calling the welcome method,
        self.welcome()
        correct_guesses=[]

        #selects a single active_phrase
        self.active_phrase = self.get_random_phrase()
        
        print(self.active_phrase)
        #showing the initial dotted lines with phrase hidden
        hidden_phrase = ''
       
        for letter in self.active_phrase:
            if letter.isalpha():
                hidden_phrase += '_'
            elif letter.isspace():
                hidden_phrase += ' '
        print(hidden_phrase)
        
        #start the game loop untl missed letters reach 5
        while self.missed < 5:
            #ask user for a letter
            user_guess=self.get_guess()
            
            

            try:
                #if user enter just one letter
                if len(user_guess) == 1:
                    #append it to guesses 
                    self.guesses.append(user_guess)
                    #print(self.guesses)
                    self.correct_guesses.append(user_guess)
                    
                elif len(user_guess) > 1:
                    self.guesses.append(user_guess)
                    print(f"These were  your guesses: {','.join(self.guesses)}, they were a total of {len(self.guesses)}")

                    
                    raise Exception('No more than one unit please')
                

            except Exception as e:
                print(f'{e}')
                #self.guesses.append(user_guess)
            except TypeError:
                self.guesses.append(user_guess)
                break

             
            checker =self.active_phrase.check_letter(user_guess)
           
            # by using check_letter function:
            if checker:
                print('Hello, you got it ')
                
                self.active_phrase.display(checker, user_guess, hidden_phrase)
                

            else:
                print('Hello, you missed it ')

                self.missed += 1
                

                print(f'You have {5-self.missed} out of 5 lives' )
                continue
            print(f"These were  your guesses: {','.join(self.guesses)}, they were a total of {len(self.guesses)}")

        else:
            self.game_over()

        
        
        
        
    def get_random_phrase(self)->str:
        copied_phrases=copy.deepcopy(self.phrases)
        self.active_phrase=random.choice(copied_phrases)
        return self.active_phrase


    def welcome(self)->None:
        '''
        prints a friendly welcome message to the user
        at the start of the game
        '''
        welcome_message = '''
        Welcome to the phrase hunter game.

        You will be presented with a hidden  phrase and your job
        is to guess it , entering letter by letter

        '''.center(127)
        print(welcome_message)
        return None

    def get_guess(self) -> str:
        try:
            user_guess = str(input('Guess a letter: ').lower())
            # check if the guess is actually a  letter, not a number
            if user_guess.isalpha():
                if len(user_guess) == 1:
                    print('Great Job, remember that it is only 1 letter at a time')

            else:

                raise Exception('Please enter a letter not a number')
        except Exception as e:
            print(f'{e}')
        else:
            return user_guess
    def game_over(self):
        pass
