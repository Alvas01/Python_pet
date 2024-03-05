print("=" * 5, " Tic-Tac-Toe ", "=" * 5)

space = list(range(1,10))

def grid(space):
   print("-" * 13)
   for i in range(3):
      print("|", space[0+i*3], "|", space[1+i*3], "|", space[2+i*3], "|")
      print("-" * 13)


def place_mark(player_token):
   valid = False
   while not valid:
      player_move = input("Where will you place " + player_token + "? ")
      
      try:
         player_move = int(player_move)
      except:
         print("Incorrect input. Are you sure you entered a number?")
         continue
      
      if player_move >= 1 and player_move <= 9:
         if(str(space[player_move-1]) not in "XO"):
            space[player_move-1] = player_token
            valid = True
         else:
            print("This cell is already occupied!")
      else:
        print("Incorrect input. Enter a number between 1 and 9.")


def win_sequence(space):
   win_combination = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_combination:
       if space[each[0]] == space[each[1]] == space[each[2]]:
          return space[each[0]]
   return False


def main(space):
    counter = 0
    win = False
    while not win:
        grid(space)
        if counter % 2 == 0:
           place_mark("X")
        else:
           place_mark("O")
        counter += 1
  
        if counter > 4:
           tmp = win_sequence(space)
           if tmp:
              print(tmp, "has won!")
              win = True
              break
        
        if counter == 9:
            print("Draw!")
            break
    grid(space)
main(space)