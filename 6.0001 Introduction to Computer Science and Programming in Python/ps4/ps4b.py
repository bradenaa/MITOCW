# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text
    

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]


    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        if shift >= 26 or shift < 0:
            return print("Please select a shift from 0 to 25")
        else:
            self.encryption_dict = {}
            
            letters = string.ascii_lowercase
            letters_seg1 = letters[0:shift]
            letters_seg2 = letters[shift:len(letters)]
            letters_shifted_low = letters_seg2 + letters_seg1
            letters_shifted_upper = letters_shifted_low.upper()
            
            letters_shifted = letters_shifted_low + letters_shifted_upper
            
            index = 0
            for l in string.ascii_letters:
                self.encryption_dict[l] = letters_shifted[index]
                index += 1
        
        return self.encryption_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        self.message_text_encrypted = ''
        for char in self.message_text:
            if char in self.encryption_dict:
                self.message_text_encrypted += self.encryption_dict[char]
            elif char not in self.encryption_dict:
                self.message_text_encrypted += char
        
        return self.message_text_encrypted
        
        
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        Message.build_shift_dict(self, shift)
        Message.apply_shift(self, shift)
        self.shift = shift

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict[:]
        
    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        Message.build_shift_dict(self, shift)
        Message.apply_shift(self, self.message_text, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        max_valid_words = 0
        best_shift = 0
        decrypted_message = ''
        
        for i in range(0, 25):
            Message.build_shift_dict(self, i)
            Message.apply_shift(self, i)
            
            valid_words = 0
            for word in self.message_text_encrypted.split():
                if is_word(self.valid_words, word):
                    valid_words += 1
                
            if valid_words > max_valid_words:
                max_valid_words = valid_words
                best_shift = i
                decrypted_message = self.message_text_encrypted
        
        
        return (best_shift, decrypted_message)
        

if __name__ == '__main__':
    
    print()
    print("+++++++++++++++++++++++++++++++++")
    print()

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    
    print('')

#    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    
    print()
    print("+++++++++++++++++++++++++++++++++")
    print()
    
    #Example2 test case (PlaintextMessage)
    plaintext2 = PlaintextMessage('hello I would like to shop today', 5)
    print('Expected Output: mjqqt N btzqi qnpj yt xmtu ytifd')
    print('Actual Output:', plaintext2.get_message_text_encrypted())
    
    print("")
    
    ciphertext2 = CiphertextMessage('mjqqt N btzqi qnpj yt xmtu ytifd')
    print('Expected Output:', (21, 'hello I would like to shop today'))
    print('Actual Output:', ciphertext2.decrypt_message())
    
    print()
    print("+++++++++++++++++++++++++++++++++")
    print()
    
    #Example3 test case (PlaintextMessage)
    plaintext3 = PlaintextMessage('I have a to exercise today or I will be fat and unhealthy', 11)
    print('Expected Output: T slgp l ez pipcntdp ezolj zc T htww mp qle lyo fysplwesj')
    print('Actual Output:', plaintext3.get_message_text_encrypted())
    
    print("")
    
    ciphertext3 = CiphertextMessage('T slgp l ez pipcntdp ezolj zc T htww mp qle lyo fysplwesj')
    print('Expected Output:', (15, 'I have a to exercise today or I will be fat and unhealthy'))
    print('Actual Output:', ciphertext3.decrypt_message())

    #TODO: best shift value and unencrypted story 
    story_cyphertext = CiphertextMessage(get_story_string())
    print(story_cyphertext.decrypt_message())
    
    
