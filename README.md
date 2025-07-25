# Hangman in Python
    #### Video Demo: https://www.youtube.com/watch?v=eLf2DWSJFcE
    #### Description:
    My project code allows the game hangman to be played in the terminal.
    Players can choose from three difficulties, easy, medium and hard.
    This alters the number of wrong guesses allowed, with 12 at easy, 6 at medium and 4 at hard.
    Players can also choose from four categories of words, fruits, sports, colours and animals.
    Each category has its own library of words stored in their respective txt files.
    Each wrong guess causes a part of the hangman to be added.
    Players win if they guess all letters in the word before the hangman is completed, and lose otherwise.
    The code itself uses a couple of libraries, namely random and csv.
    random is used for randint, which helps to choose a word from the category chosen.
    csv helps in reading the txt files, also to choose a word from the chosen category.
    After running the programme, it prompts the user for a difficulty.
    If the user input does not correlate to any of the given difficulties, case-insensitively, it will re-prompt them.
    Likewise for the following category selection.
    Then the game starts, and the player is prompted for a letter.
    Again, if the input is not a single letter, that additionally has not been guessed before, the programme re-prompts them.
    If the guessed letter is correct, nothing is added to the hangman.
    If it is wrong, the hangman will be added to.
    The game ends when either the player has guessed all the letters, or the hangman is completed, resulting in a win or a loss respectively.
