# Create your Phrase class logic here.
# create phrase class
class Phrase():
    def __init__(self, phrase:str):
        self.phrase=phrase.lower()
       

        
    def __str__(self) -> str:
        return f'{self.phrase}'
        
    def check_letter(self, phrase,user_guess)->bool:
        if user_guess in self.phrase:
            return True
        else:
            return False
        
        
       

    
        


        

