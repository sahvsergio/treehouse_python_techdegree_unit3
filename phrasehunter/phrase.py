from typing import List
# Create your Phrase class logic here.
# create phrase class


class Phrase():
    def __init__(self, phrase: str):
        self.phrase = phrase.lower()

    def __str__(self) -> str:
        return f'{self.phrase}'

    def __iter__(self):
        yield from self.phrase

    def check_letter(self, user_guess: str) -> bool:
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

    def display(self,
                checker: bool,
                user_guess: str,
                hidden_phrase: str) -> str:

        '''
        presents guessed letters and
        non-guessed_ letters
        as underscores ex: _ _ _ _'''
        # initialize an index list to keep record
        # of the indexes in which
        # the letters are located
        indexes: List[int] = []
        # list to keep all of the letters in self.phrase

        adapted_phrase_list: List[str] = []
        # if checker is meant
        if checker:
            # loop over self.phrase to get indexes of correct letters
            for index, letter in enumerate(self.phrase):
                # check letter and user_guess are equal
                if letter == user_guess:

                    # append the index into the indexes list
                    indexes.append(index)

            # loop through the hidden phrases with enumerate

            for index,  letter in enumerate(hidden_phrase):
                # if current index is in the indexes list
                if index in indexes:
                    # replace  the '_' with a letter in that index
                    letter: str = hidden_phrase[index].replace(letter, user_guess)
                    # append the letter to the phrase list

                    adapted_phrase_list.append(letter)

                else:
                    # we still add the incorrect guess to the guesses list
                    adapted_phrase_list.append(letter)
        # turn the list into a string of the type with correct guesses and underscores
        save_option = ''.join(adapted_phrase_list)
        # print the string  to the user
        print(save_option)
        # turn the string into a list to keep modifying the underscores for guessed letters
        hidden_phrase: List[str] = list(save_option)
        return hidden_phrase

    def check_complete(self, hidden_phrase):
        ''' checks to see if
        the whole phrase
        has been guessed.'''
        if '_' not in hidden_phrase:
            return True
        else:
            return False
