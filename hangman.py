import random
name=input("enter your name")
print("HEY",name,"WELCOME TO OUR HANGMAN GAME")
IMAGES= ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /    |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''', '''
	
''']


def get_word():
    file=open("hangman_words.txt","r")
    data=file.read().split()
    empty=[]
    for i in data:
        empty.append(i)
    word=random.choice(empty)
    return word.lower()
def hangman():
    print("please try to guess the word")
    secret_word=get_word()
    tries=len(secret_word)
    a=secret_word
    b=[]
    for i in range(len(a)):
        b.append(a[i])
    print(b)
    print(secret_word)
    lenword=""
    for i in range(len(secret_word)):
        lenword=lenword+"_"
    print(lenword)
    lenwordlist=[]
    for i in lenword:
        lenwordlist.append(i)
    a=len(secret_word)
    guessmade=""
    guess_list=[]
    turn=9
    while 8>0:
        guess=input("please guess a letter")
        if len(guess)==1 and guess.isalpha():
            if guess in  guess_list:
                print("you already gussed the word",guess)
            else:
                guess_list.append(guess)
            if guess in secret_word:
                print("good job you guess the word")
                for i in range(len(secret_word)):
                    if secret_word[i]==guess:
                        lenwordlist[i]=guess
                print("YOUR GUESSING WORD=",lenwordlist)
                print("    ")
                if b==lenwordlist:
                    print("you won")
                    break
                # if guessmade==secret_word:
                #     print("********* CONGRATULATION YOU WON ********")
            elif guess not in secret_word:
                print("OPPS! YOUR GUESS LETTER",guess,"NOT IN SECRET WORD AND YOU HAVE LOST ONE CHANSE")
                turn=turn-1
                if turn==8:
                    print("NOW YOU HAVE ONLY",turn,"ARE LEFT")
                    print(IMAGES[0])
                if turn==7:
                    print("NOW YOU HAVE ONLY",turn,"ARE LEFT")
                    print(IMAGES[1])
                if turn==6:
                    print("NOW YOU HAVE ONLY",turn,"ARE LEFT")
                    print(IMAGES[2])
                if turn==5:
                    print("NOW YOU HAVE ONLY",turn,"ARE LEFT")
                    print(IMAGES[3])
                if turn==4:
                    print("NOW YOU HAVE ONLY",turn,"ARE LEFT")
                    print(IMAGES[4])
                if turn==3:
                    print("NOW YOU HAVE ONLY",turn,"ARE LEFT")
                    print(IMAGES[5])
                if turn==2:
                    print("NOW YOU HAVE ONLY",turn,"ARE LEFT")
                    print(IMAGES[6])
                if turn==1:
                    print("you Are loose The Game")
                    print(IMAGES[7])
                    print("OPPS!, SOORY YOU ARE A LOOSER . TRY NEXT TIME")
                    break
             
        else:
            print("soory! it is not valid",guess," PLEASE GUESS ONLY ONE LETTER")
        a=a-1     
hangman()                  
def play_again():
    while True:
        again=input("do you want to play again y/n*****")
        if again=="y":
            hangman()
        else:
            break
play_again()

    
    
    