import sys
import random
import time
#from package import progress as pg #functions and packages

def progress():
	animation = "|/-\\" 
	for i in range(100):
		time. sleep(0.01) #
		sys. stdout. write("\r" + animation[i % len(animation)]) 
		sys

def typing(txt):
        for word in txt:
        	print(word, end='')
        	sys.stdout.flush()
        	time.sleep(0.05)
        return('')

def speed(txt):
	for word in txt:
		print(word, end='')
		sys.stdout.flush()
		time.sleep(0.03)
	print('')

def loading(text, delay=0.2):
    print(end=text)
    n_dots = 0
    count = 9
    while count > 0:
        if n_dots == 3:
            print(end='\b\b\b', flush=True)
            print(end='   ',    flush=True)
            print(end='\b\b\b', flush=True)
            n_dots = 0
        else:
            print(end='.', flush=True)
            n_dots += 1
            count-=1
        time.sleep(delay)


typing("\n\t\t**RULES FOR THE GAME**\n\t1.) Do not enter anything that is not in list below, \tdoing so will give your opponet a score\n\t2) just enjoy playing")
#list
game_tools = ["rock","paper","scissors"]
game_kit = ['name',"rock","paper","scissors"]
bot_win_exp = 'hahaha yippee am the best at this game hallelujah dub this ain\'t the last one '

#string
typing(f'\n\n\tlist: {game_kit}')
usr = input('\nEnter your name: ')
progress()
typing('\nMy name is bot')

#int
bot =0
usr_score=0
pattern = 10 * "*"

#count
gamecount = True
count = int(input(('\nhow many rounds do you wish to have? '))) 
progress()

#loops
while gamecount:
	typing(f'\n{usr}:{usr_score} \t\t  bot:{bot} \t remaining:{count} rounds')
	usr_prompt = input(typing('\nits your turn> '))
	bot_prompt = random.choice(game_tools)
	count -= 1
	if count < 1:
		gamecount = False
	# if,elif and else statements 
	if usr_prompt == bot_prompt:
		progress()
		typing(f'\n{usr_prompt} and {bot_prompt}')
		time.sleep(1)
		typing('\njudge: ')
		loading('typing\n')
		progress()
		typing('\n damn!, it\'s a draw')
		bot += 1
		usr_score += 1
		
	elif usr_prompt != bot_prompt:
		loading('loading')
		typing('\ni think you can win\n')
		progress()
		typing(f'\n{usr}: {usr_prompt}\n bot:{bot_prompt}')
		
		if usr_prompt == 'rock'and bot_prompt == 'paper':
			print('\nbot typing ...')
			progress()
			typing('\npaper covers rock, i win')
			bot += 1
			
		elif usr_prompt == 'paper' and bot_prompt == 'rock':
			typing(f'\nbot: you just got luck {usr}!')
			usr_reply = input(f'\n{usr}: ')
			progress()
			typing('\nbot: ok kid next round am taking you down.')
			usr_score += 1
		
		elif usr_prompt == 'rock' and bot_prompt == 'scissors':
			typing(f'\njudge: {usr} your rock can\'t  be cut by bot\'s {game_tools[-1]}\n')
			progress()
			typing(f'\nbot: you just got lucky {usr}!')
			print('...')
			progress()
			usr_reply = input(f'\n{usr}: ')
			print('...')
			progress()
			typing('\nbot: ok kid next round am taking you down.')
			usr_score += 1
			
		elif usr_prompt  == 'scissors' and bot_prompt =='rock':
			typing(f'\nbot: this game is mine {usr}')
			print('...')
			progress()
			usr_reply = input(f'\n{usr}: ')
			print('...')
			progress()
			typing('\nbot: here i go again')
			bot += 1
						
		elif usr_prompt  == 'paper' and bot_prompt == 'scissors':
			typing('\nbot: let me first cut you into pieces')
			print("...")
			progress()
			usr_reply = input(f'\n{usr}: ')
			print("...")
			progress()
			typing('bot: ok')
			bot += 1
		elif usr_prompt  == 'scissors' and bot_prompt == 'paper':
			typing(f'\nbot: i dare you to cut me {usr}')
			print('...')
			progress()
			usr_reply = input(f'\n{usr}: ')
			print("...")
			progress()
			typing('\nbot: ok')
			usr_score += 1

		elif usr_prompt not in game_tools:
				typing('\ninvalid entry')
				bot += 1

if usr_score > bot:
	typing(f'\n{usr}: {usr_score}\n\t\t{pattern} {usr} wins {pattern}\n')

	typing(' rock-paper-scissors game developed by John Delvin from Solo learn\n\tbeginners can try reading my code')
	exit()

else:
	typing(f'\nbot: {bot}\n \t\t{pattern} bot wins {pattern}\n')
	typing(f'\n{bot_win_exp}')
	typing('\n rock-paper-scissors game developed by John Delvin from Solo learn\n \t beginners can try reading my code')
	exit()				
