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
        #a list to store the indexes
        # of user_guess in self.phrase  
        indexes=[]
        correct_guesses=[]

        #letters
        adapted_phrase_list=[]
        #if checker is ment
        if checker:
            #use enumerate to get indexes
            for index, letter in enumerate(self.phrase):
                #check letter and user_guess are equal
                if letter ==user_guess:   
                    
                    #append the index into the indexes list
                    indexes.append(index)
                    correct_guesses.append(user_guess)
                
         
                
            print(indexes)
            print(len(indexes))
            recovered_phrase=''
            for index,  letter in enumerate(hidden_phrase):
                if index in indexes:
                    letter=hidden_phrase[index].replace(letter, user_guess)
                    adapted_phrase_list.append(letter)
                    
                   
                else:
                    print(letter)
                    adapted_phrase_list.append(letter)
                print(adapted_phrase_list)
                print(type(adapted_phrase_list))
                save_option=''.join(adapted_phrase_list)
                print(save_option)
                #adapted_phrase_list
                
            
                    
                
            
            
       
      
            
            
                
                

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
