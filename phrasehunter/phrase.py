# Create your Phrase class logic here.
#create phrase class
class Phrase:
    # create __init with phrase parameter
    def __init__(self, phrase):

        # phrase: needs to be converted to lowercase
        
        self.phrase= phrase.lower()

    def display(self):
        '''
        presents guessed letters and 
        non-guessed_ letters 
        as underscores ex: _ _ _ _'''

        pass
    def check_letter(self):
        '''
        checks to see if the letter selected 
        by the user
        matches a letter in the phrase.

        '''
        pass

    def check_complete(self):
        '''
        check_complete(): checks to
        see if the whole phrase
        has been guessed.
        '''
        
      



