class Hangman:

    ''' The game Hangman is played by entering 1 alphabetical letter which will be shown, if guessed well, in a string
     on the correspondending place in the word to be guessed. The other characters remain hidden with an underscore (_)
     if they aren't guessed yet'''

    def __init__(self, possible_words, word_to_find, lives, correctly_guessed_letters, wrongly_guessed_letters,
                 turn_count, error_count, guessed_letter)
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = list(random.choice(possible_words))
        self.lives = 5
        self.correctly_guessed_letters = []
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        self.guessed_letter = ''
        self.to_display = list(len(word_to_find) * "_")
        self.word_is_found = False