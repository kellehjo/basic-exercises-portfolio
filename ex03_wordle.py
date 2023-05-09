"""Ex03 - Wordle - What word could it be? """
"""Part 1"""

def contains_char(searched_str: str, single_searched_char: str) -> bool:
    """Checking if single character found in searched word"""
    assert len(single_searched_char) == 1
    check_each_letter = 0

    '# while checking each character is less then the length of the searched string, we look to see if #'
    '# the single character is in the searched string. If found, returns True, if not returns False #'

    while check_each_letter < len(searched_str):
        if searched_str[check_each_letter] == single_searched_char:
            return True
        else:
            check_each_letter = check_each_letter + 1
    return False

"""Part 2"""
def emojified(guessed_word: str, secret_word: str) -> str:
    """return a string of emoji depending on location and character"""
    assert len(guessed_word) == len(secret_word)
    '#creating emoji characters to be printed out later'
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    check_each_letter = 0
    emoji: str = ""
    
    '# while the length of the secret word is less than our checking character indicator, #'
    '# I am checking that if the contain_char funcation is false, white emoji box is used. If true, #'
    '# then I am going to check if the letter is in the exact postion (green box) or incorrect position (yellow box)#'
    
    while check_each_letter < len(secret_word):
        if not contains_char(secret_word, guessed_word[check_each_letter]):
            emoji = emoji + WHITE_BOX 
        else:
            if guessed_word[check_each_letter] == secret_word[check_each_letter]:
                emoji = emoji + GREEN_BOX
            else:
                emoji = emoji + YELLOW_BOX
        check_each_letter = check_each_letter + 1
    return(emoji)

"""Part 3"""
def input_guess(exp_length: int) -> str:
    """ask user for guess of the expected length"""
    user_guess: str = input(f"Enter a {exp_length} character word: ")
    
    '# While the user does not give a word of the correct length, the user #' 
    '# is prompted to give a word of the correct length, until they do #'

    while len(user_guess) != exp_length:
        user_guess = input(f"That wasn't {exp_length} chars! Try again: ")

    '# when the user finally gives a word of the correct length it is returned'
    return user_guess

"""Part 4"""
def main() -> None:
    """The entrypoint of the program and main game loop."""
    '# creating a secret word variable, counting number of turns variable, and setting a winner to stop the game #'
    '# if the correct word is picked before the user runs out of turns'
    
    secret_word: str = "codes"
    num_of_turns = 1  
    win_ner: bool = False
    max_turns: int = 7
    
    '# while the game is less than 7 turns and the correct word is not chosen, the game will run #'
    while num_of_turns < max_turns and not win_ner:
        '# expressing number of turns, asking a user for a guess using input_guess function, and printing emojis #'
        '# using the eomjified function based on whether the characters exist in the word and if they are placed properly. #'
        
        print(f"=== Turn {num_of_turns}/6 ===")
        guessed = input_guess(len(secret_word))
        print(emojified(guessed, secret_word)) 
        
        '# If the secret word is guessed the game ends and the user to told the number of turns it took #'
        if secret_word == guessed:
            win_ner = True
            print(f"You won in {num_of_turns}/6 turns!")
        else:
            num_of_turns += 1
    
    '# If the user cannot guess the word in the specified number of tries, then the user to prompted to try again tomomorow'
    if secret_word != guessed:
        print(f"X/6 - Sorry, try again tomorrow!")

'# allowing the main function to be used in the terminal and not just the REPL. #'
if __name__ == "__main__":
    main()
