import random
import os

def show_board():
	print ("        ||        ||     ")
	print ("   {}    ||   {}    ||   {}                   ".format(tablica[0],tablica[1],tablica[2]))
	print ("        ||        ||      ")
	print ("============================")
	print ("        ||        ||     ")
	print ("   {}    ||   {}    ||   {}                   ".format(tablica[3],tablica[4],tablica[5]))
	print ("        ||        ||      ")
	print ("============================")
	print ("        ||        ||      ")
	print ("   {}    ||   {}    ||   {}                   ".format(tablica[6],tablica[7],tablica[8]))
	print ("        ||        ||      ")
  
def turn():
	if(who_s_turn==1):
		print('It is player {} turn.'.format(who_s_turn))
	else:
		print('It is player {} turn.'.format(who_s_turn))


def check_win():
	for i in range (0,3):
		if(tablica[i]==tablica[i+3]==tablica[i+6] and tablica[i]!=' '):
			return True
	for i in range (0,9,3):
		if(tablica[i]==tablica[i+1]==tablica[i+2]and tablica[i]!=' '):
			return True
	if((tablica[0]==tablica[4]==tablica[8] or tablica[2]==tablica[4]==tablica[6]) and tablica[4]!=' '):
		return True
	return False



game_is_on=True


while (game_is_on):
	player_two_mark='0'
	player_one_mark='0'
	pozycje={1:player_one_mark,2:player_two_mark}
	print('Welcome to the Tic tac toe game players.')
	input('Press ENTER to draw who starts.')
	os.system("cls")
	los=random.randint(1,2)
	print('Player {} starts and chooses X or O'.format(los))
	if(los==1):
		player_one_mark=input("Choose your mark: ")

		if (player_one_mark!='X' and player_one_mark!='O'):
			player_one_mark=input('You can only choose between X and O: ')

		if(player_one_mark=='X'):
			player_two_mark='O'
		else:
			player_two_mark='X'
	else:
		player_two_mark=input("Choose your mark: ")

		if (player_two_mark!='X' and player_two_mark!='O'):
			player_two_mark=input('You can only choose between X and O: ')

		if(player_two_mark=='X'):
			player_one_mark='O'
		else:
			player_one_mark='X'

	pozycje={1:player_one_mark,2:player_two_mark}

	tablica=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
	who_s_turn=los
	win=False
	licznik=0
	while (not win):
		os.system("cls")
		show_board()
		turn()
		x=int(input('\nChoose your position (1-9): '))
		if tablica[x-1]!=' ':
			print('This position is ocuppied, choose one more time')
			continue
		tablica[x-1]=pozycje[who_s_turn]

		if(check_win()):
			win=True
			os.system("cls")
			show_board()
			print('\nCONGRATULATIONS PLAYER {}, YOU WON.'.format(who_s_turn))
			y=input('Do you want to play again (Yes OR No) ?: ')
			if(y=='Yes'):
				os.system("cls")
				break
			else:
				game_is_on=False
				break
    
    
		if(who_s_turn==1):
			who_s_turn=2
		else:
			who_s_turn=1
		licznik+=1
		if(licznik==9):
			win=True
			os.system("cls")
			show_board()
			print('\nIt is a draw')                                                                                       
			x=input('Do you want to play again (Yes OR No) ?: ')
			if(y=='Yes'):
				os.system("cls")
				break
			else:
				game_is_on=False





os.system("cls")
print("Thank you for playing.")
input('Press Enter to exit')

