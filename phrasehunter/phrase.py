from typing import List
# Create your Phrase class logic here.
# create phrase class
class Phrase():
    def __init__(self, phrase:str):
        self.phrase=phrase.lower()
       

        
    def __str__(self) -> str:
        return f'{self.phrase}'
    
    def __iter__(self):
        yield from self.phrase

    #def __eq__(self, value: object) -> bool:
    #    pass
        
        
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

    def display(self, checker:bool, user_guess:str, hidden_phrase:str) -> str:
        
        '''
        
        presents guessed letters and
        non-guessed_ letters
        as underscores ex: _ _ _ _'''
        indexes = []
        
        save_options=[]

        # letters
        adapted_phrase_list = []
        # if checker is meant
        if checker:
            # use enumerate to get indexes
            for index, letter in enumerate(self.phrase):
                # check letter and user_guess are equal
                if letter == user_guess:

                    # append the index into the indexes list
                    indexes.append(index)
                    
                

            #loop through the hidden phrases
            
            for index,  letter in enumerate(hidden_phrase):
                if index in indexes:
                    letter = hidden_phrase[index].replace(letter, user_guess)
                    adapted_phrase_list.append(letter)

                else:
                   
                    
                    adapted_phrase_list.append(letter)
                    
                
            print(type(adapted_phrase_list))
        save_option = ''.join(adapted_phrase_list)
        
        
        
            
                
            
        print(save_option)
      
            
                
        
        
       
       
       
            
                
            
          
          
       
        

    def check_complete(self):
        ''' checks to see if
        the whole phrase 
        has been guessed.'''
        pass
        
        
       

    
        


        

