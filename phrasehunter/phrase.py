# Create your Phrase class logic here.
# create phrase class
class Phrase():
    def __init__(self, phrase:str):
        self.phrase=phrase.lower()
       

        
    def __str__(self) -> str:
        return f'{self.phrase}'
    
    def __iter__(self):
        yield from self.phrase

    def __eq__(self, value: object) -> bool:
        pass
        
        
    def check_letter(self,user_guess)->bool:
        '''checks to see if the letter selected
        by the user matches a letter 
        in the phrase.
        '''
        try:
            if user_guess in self.phrase:
                return True
        
            else:
                return False
        except TypeError:
            print('Please enter only letters, not numbers')

    def display(self, user_guess, checker,hidden_phrase)->str:
        '''
        
        presents guessed letters and
        non-guessed_ letters
        as underscores ex: _ _ _ _'''

        
        #a list to store the indexes
        # of user_guess in self.phrase  
        indexes=[]
        correct_guesses
        print(hidden_phrase)
        #for letter in 

    def check_complete(self):
        ''' checks to see if
        the whole phrase 
        has been guessed.'''
        pass
        
        
       

    
        


        

