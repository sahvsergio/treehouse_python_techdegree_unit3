# Create your Phrase class logic here.
#create phrase class
class Phrase:
    # create __init with phrase parameter
    def __init__(self, phrase:str):

        # phrase: needs to be converted to lowercase
        
        self.phrase:str= phrase.lower()

    def display(self,hidden_phrase)->str:
        '''
        presents guessed letters and 
        non-guessed_ letters 
        as underscores ex: _ _ _ _'''
        
    
        
        
        


    def check_letter(self, user_guess:str) -> bool:
        '''
        checks to see if the letter selected 
        by the user
        matches a letter in the phrase.
        

        '''
        if user_guess in self.phrase:
            return True
        else:
            return False

       

    def check_complete(self)-> bool:
        '''
        check_complete(): checks to
        see if the whole phrase
        has been guessed.
        '''
        
        
      



