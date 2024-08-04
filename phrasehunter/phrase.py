# Create your Phrase class logic here.
# create phrase class
class Phrase:
    # create __init with phrase parameter
    def __init__(self, phrase: str):

        # phrase: needs to be converted to lowercase

        self.phrase: str = phrase.lower()
    

    def display(self, checker, hidden_phrase, user_guess) -> str:
        
        '''
        presents guessed letters and
        non-guessed_ letters
        as underscores ex: _ _ _ _'''
        #if the  user_guess is self.phrase
        if checker:
            pass
               
         
           
         
               
           
            
           
             
           
           
            
        
    def check_letter(self, user_guess: str) -> bool:
        '''
        checks to see if the letter selected
        by the user
        matches a letter in the phrase.


        '''

        if user_guess.lower() in self.phrase:
            if len(user_guess) > 1:
                return True
            else:
               return True
        else:
                return False


    def check_complete(self) -> bool:
        '''
        check_complete(): checks to
        see if the whole phrase
        has been guessed.
        '''
        pass
