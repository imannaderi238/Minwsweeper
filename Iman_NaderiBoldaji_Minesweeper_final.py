import string as st
import random as rnd
import colorama as clr
import time 

#This fuction Get a correct number from User.   user must be input interger number , in this program just use it
#everything else ** interger number > 2 *** is incorrect and show alram to user
def get_number_user(title_msg ,wrong_msg):
    # this function able give the differt message
    temp_lower_tuple = tuple (st.ascii_lowercase)
    user_num = 0 
    user_input = input(title_msg)
    # in the loop we want to get a correct number between 1 to n and if user input incorrect number,show a message
    try:   
        while True:
            result_input = 0
            for x in range(0 ,len(user_input)  ):
                #print (user_input[x])
                if user_input[x] in temp_lower_tuple:
                    result_input += 1
                    #print(result_input)
                    print(f'{clr.Fore.YELLOW}{wrong_msg}{clr.Fore.WHITE}')
                    user_input = input(title_msg)
                    break
                if result_input ==0:
                    user_num = int (user_input)
            if user_num > 2 :
                return user_num
                break
            else:
                print(f'{clr.Fore.YELLOW}{wrong_msg}{clr.Fore.WHITE}')
                user_input = input(title_msg)
    except ValueError as val_error:
        print(f'{clr.Fore.YELLOW}{wrong_msg}{clr.Fore.WHITE}')
        user_input = input(title_msg)

#This fuction create a squar board for playground  ****** With list Comperhension  *********
def new_matrix(mdim_number , chr_for_show):
    #************ list comperhension ***********
    matrix = [list(range(mdim_number)) for i in range(0 ,mdim_number)]
    # matrix = []
    # for i in range(0 ,mdim_number):
    #     matrix.append(list(range(mdim_number)))

    #Fill multidimention with a favorite character that  it get from user
    #************ list comperhension ***********
    matrix =[[ chr_for_show for k in range(mdim_number)] for j in range(mdim_number)] 
    # for j in range(mdim_number):
    #     for k in range(mdim_number):
    #         matrix[j][k] = chr_for_show
    return matrix

#This fuction use to show playground
def show_matrix(name_of_matrix ):
    #Show the numbers above the playing field. so User can choose easily
   
    print('   ' ,end='')
    for i in range(1 ,board_size + 1):
        if i < 10:
            print(clr.Fore.RED,f'{i} ' ,end='')
        else :
            print(clr.Fore.RED,f'{i}' ,end='')
    print()
    #create a list from uppercase charater for showing in the playing feild
    list_ch = list(st.ascii_uppercase)
    for i in range(board_size):
        print(clr.Fore.BLUE,f'{list_ch[i]}' , clr.Fore.WHITE,end = '')  
        for j in range(board_size):
            if name_of_matrix[i][j] == 9 :
                print(f'{clr.Fore.RED} {name_of_matrix[i][j]} {clr.Fore.WHITE}' ,end = '')
            else :
                print(f' {name_of_matrix[i][j]} ' ,end = '')
        print()

#input from user to show places of playground and check everything . User must be input correct format like (a1 ,A1) that it is ok 
# and (12 ,2s ,ss ,Sh ,Ha ,sdsd ,312321 ,adasdsad13123213) is not ok and show alarm to user
#   ****************   used list coperhension ********** Tuple ********
def choose_user(choose_user ,board_matrix ,user_matrix):
    try :
        number_tuple = tuple(range(10))
        chr_tuple = tuple(st.ascii_uppercase)
        #************ list comperhension ***********
        # chr_list =[]
        # for x in range(0 , len(board_matrix)):
        #     chr_list.append(chr_tuple[x])
        #print(chr_list)
        chr_list = [chr_tuple[x] for x in range (0 ,len(board_matrix))]
        for i in range(len(chr_list)):
                if chr_list[i] == choose_user[0].upper() :
                    row = i
        
        if (1 < len(choose_user) < 3) and (choose_user[0].upper() in chr_list) and ( 0 < int(choose_user[1]) <= len(board_matrix)) :
                col = int(choose_user[1])  - 1
                return result_choose_user(board_matrix ,user_board ,row , col)
        if (2 < len(choose_user) < 4) and (choose_user[0].upper() in chr_list) and (int(choose_user[1]) in number_tuple) and (int(choose_user[2]) in number_tuple) and ( 0 < int(choose_user[1]+choose_user[2]) <= len(board_matrix)) :
            col = int(choose_user[1]+choose_user[2]) - 1
            return result_choose_user(board_matrix ,user_board ,row , col)
        else:
             print(clr.Fore.GREEN ,'Dear user you must input correct format. for exapmle (A1,B2). \n (the uper or lower character is not important ) \n' )    
    except ValueError as val:
        print(f'{clr.Fore.GREEN}Dear user you must input correct format. for exapmle (A1,B2). \n (the uper or lower character is not important ) \n  {clr.Fore.WHITE} ')

        
def result_choose_user(board_matrix ,user_matrix ,row ,column):
    number_tuple = tuple(range(9))
    if board_matrix[row][column] == 9:#Suppose that ,this number is mine
        print(f'{clr.Fore.RED}   ( Escape!  bomb  ) ') # change color promt
        user_matrix[row][column] ='*'
        time.sleep(1.2)
        print()
        show_matrix(user_matrix)
        print()
        print(f'{clr.Fore.LIGHTRED_EX}  GAME OVER ):  BY BY  (Try more)   ')
        time.sleep(2)
        print()
        print(f'{clr.Fore.CYAN} Minesweeper game answer was (Bomb = 9): ')
        show_matrix(board_matrix)
        print(clr.Fore.WHITE)
        return False
    #show the place that it has number and it will be show for user
    elif 0 < board_matrix[row][column] < 9:
        user_matrix[row][column] = board_matrix[row][column]
    #show the plase that it has nothing and it will be show all placese arounde the this selected plase for user
    elif board_matrix[row][column] == 0 :
        neighbors_find(user_matrix , board_matrix ,row ,column)

#This function random put mines in the playground ** I like it **   In my program mine is '9' 
def put_mines(mines ,matrix):
    #Create a list for showing number of all cells that will be in playing field
    temp_list_square = list(range(2 ,(len(matrix) * len(matrix)) + 1))
    temp_list_rnd = rnd.sample(temp_list_square ,mines)
    #this variable is used for when the number of mines put on the playing feild ,loop stop
    counter = 0
    for i in range (0,len(matrix)):
        for j in range (0 ,len(matrix)):
            counter +=1
            for k in range (0 ,len(temp_list_rnd)):
                if counter == temp_list_rnd[k]:
                    matrix[i][j] = 9 # 9 is mine    
     

#The following three function are  important  this program that calculate all value of places in playground *** Used dectionary ***
def game_calculator_position(top_row ,buttom_row ,left_row ,right_row):
    top_row ,buttom_row ,left_row , right_row = top_row ,buttom_row ,left_row ,right_row
    temp_dic ={
        'top':top_row ,
        'buttom':buttom_row ,
        'left':left_row ,
        'right':right_row
    }
    return temp_dic


def game_calculator(matrix ,board_size):
    try:
        temp_dic = {}
        for i in range (board_size):
            for j in range (board_size):
                if matrix[i][j] == 9: #Suppose that ,this number is mine
                    # This condition just use for first row
                    if i == 0 and j == 0:
                        temp_dic = game_calculator_position( i -1 ,i + 1 ,j ,j + 1)
                    #This condition use first column
                    elif i < 3 and j == 0:
                       temp_dic = game_calculator_position( i + 1 ,i - 1 ,j ,j + 1)
                    #This condition use last column
                    elif i >= 0 and j == board_size - 1:
                        temp_dic = game_calculator_position( i -1 ,i + 1 ,j - 1 ,j )
                    #This condition use last row
                    elif i == 3 and j >= 0:
                        temp_dic = game_calculator_position( i -1 ,i + 1 ,j - 1 ,j + 1)
                    elif i >= 0 and  j >= 0:
                        temp_dic = game_calculator_position( i -1 ,i + 1 ,j -1  ,j + 1)
                    #this condition is just last row and first column
                    if temp_dic['left'] < 0 :
                        temp_dic['left'] = 0
                    game_calculator_places(matrix ,temp_dic ,i)
                    
    except ValueError as error:
        print(error)


def game_calculator_places(matrix ,dic_location ,row_count):
    
    for i in range(dic_location['left'] ,dic_location['right'] + 1  ):
        if matrix[dic_location['top']][i] != 9 :
            if 0 <= dic_location['top'] < len(matrix) :
                matrix[dic_location['top']][i] += 1
    
    for j in  range (dic_location['left'] ,dic_location['right']  + 1 ):
        #print(f'{left_row} , {j }) = {matrix[left_row][j]}')
        if 0 <= dic_location['buttom'] < len(matrix) :
            if matrix[dic_location['buttom']][j] != 9 :
                matrix[dic_location['buttom']][j] += 1
    
    if matrix[row_count][dic_location['right']] != 9:
        #print(f'r {righ_row} , {i}) = {matrix[righ_row][i]}')
        if 0 <= dic_location['right'] <  board_size:
            matrix[row_count][dic_location['right']] += 1
    
    if matrix[row_count][dic_location['left']] != 9:
        #print(f' l {left_row} , {i}) = {matrix[left_row][i]}')
        if 0<= dic_location['left'] < board_size:
            matrix[row_count][dic_location['left']] += 1

#the follwing three function are used find ,check and show empty places in playground    *** used list comperhension  ****
def neighbors_find (user_matrix ,game_matrix , location_row ,location_column): 
    result = neighbors_check(user_matrix ,game_matrix , location_row ,location_column)
    row_list = []
    col_list = []
    if result == False:
        row = location_row
        column = location_column
        #Initial values
        start_row = row - 1
        end_row = row + 2
        start_column = column - 1
        end_column = column + 2
        #print(f'start row  ={start_row}   end row ={end_row } start column ={start_column} end column={end_column }')
        if (end_row > len(game_matrix)) and (end_column > len(game_matrix)):
            end_column = len(game_matrix) 
            end_row = len(game_matrix) 
            neighbors_fill(user_matrix ,game_matrix ,start_row ,end_row ,start_column  ,end_column)
        elif end_row > len(game_matrix): 
            end_row = len(game_matrix)
            neighbors_fill(user_matrix ,game_matrix ,start_row ,end_row ,start_column  ,end_column)                    
        elif end_column > len(game_matrix):
            end_column = len(game_matrix)
            neighbors_fill(user_matrix ,game_matrix ,start_row ,end_row ,start_column  ,end_column)          
        else :
            neighbors_fill(user_matrix ,game_matrix ,start_row ,end_row ,start_column  ,end_column)
    for i in range (0 , len(user_matrix)):
        for j in range (0 , len(user_matrix) ):
            if user_matrix[i][j] == 0 :
                row_list.append(i)
                col_list.append(j) 
                show_empty_place(game_matrix ,user_matrix ,row_list ,col_list)

def neighbors_check (user_matrix ,game_matrix , location_row ,location_column):
    row = location_row
    column = location_column
    start_row = row - 1
    end_row = row + 2
    start_column = column - 1
    end_column = column + 2
    #print(f'start row  ={start_row}   end row ={end_row } start column ={start_column} end column={end_column }')
    if (end_row > len(game_matrix)) and (end_column > len(game_matrix)):
        end_column = len(game_matrix) 
        end_row = len(game_matrix) 
        neighbors_list = [game_matrix[i][j] for i in range (start_row , end_row) for j in range(start_column ,end_column) if i>=0 and j >= 0]
        # for i in range (start_row ,end_row ):
        #     for j in range (start_column  , end_column ):
        #        # print(f' numbers is : {game_matrix[i][j]}  ** ({i} , {j})')
        #         if (i >= 0  and j >= 0 ) :
        #             temp_list.append(game_matrix[i][j])
    elif end_row > len(game_matrix): 
        end_row = len(game_matrix)
        neighbors_list = [game_matrix[i][j] for i in range(start_row, end_row) for j in range(start_column, end_column) if i >= 0 and j >= 0]
    elif end_column > len(game_matrix):
        end_column = len(game_matrix)
        neighbors_list = [game_matrix[i][j] for i in range (start_row , end_row) for j in range(start_column ,end_column) if i>=0 and j >= 0]
    else :
        neighbors_list = [game_matrix[i][j] for i in range (start_row , end_row) for j in range(start_column ,end_column) if i>=0 and j >= 0]
    state_mines = False
    for x in (0 ,len(neighbors_list) - 1 ):
        if neighbors_list[x] == 9 :
            state_mines == True
            break
    return state_mines

def neighbors_fill (user_matrix ,game_matrix ,start_row ,end_row ,start_column  , end_column):
    for i in range (start_row ,end_row ):
        for j in range (start_column  , end_column ):
            if (i >= 0  and j >= 0 ) :
                user_matrix[i][j] = (game_matrix[i][j])

def show_empty_place(game_matrix ,user_matrix ,row_list , col_list):
    #print(f'{row_list} , {col_list}')
    for x in range(0 ,len(row_list)):
        row = row_list[x]
        column = col_list[x]
        #Initial values
        start_row = row - 1
        end_row = row + 2
        start_column = column - 1
        end_column = column + 2
        #print(f'start row  ={start_row}   end row ={end_row } start column ={start_column} end column={end_column }')
        if (end_row > len(game_matrix)) and (end_column > len(game_matrix)):
            end_column = len(game_matrix) 
            end_row = len(game_matrix) 
            neighbors_fill(user_matrix ,game_matrix ,start_row ,end_row ,start_column  ,end_column)
        elif end_row > len(game_matrix): 
            end_row = len(game_matrix)
            neighbors_fill(user_matrix ,game_matrix ,start_row ,end_row ,start_column  ,end_column)
        elif end_column > len(game_matrix):
            end_column = len(game_matrix)
            neighbors_fill(user_matrix ,game_matrix ,start_row ,end_row ,start_column ,end_column)
        else :
            neighbors_fill(user_matrix ,game_matrix ,start_row ,end_row ,start_column  ,end_column)


# I would like use timer but I don't know where place my program called this function .But i try to solve it
def show_timer ():
    second ,minute ,counter ,temp_minute = 0 ,0 ,0 ,0
    while True:
        counter += 1
        time.sleep(1)
        second = counter % 60
        minute = counter // 60
        print(f'{minute}:{second}',end= '\r')

#This function calculate win . If the numbers of revealed  + numbers of mines == all places => you win
def game_win (get_matix ,Get_number_mines):
    #list of number that use in play 
    tuple_number = (0,1,2,3,4,5,6,7,8)
    counter = 0
    #counter = [counter + 1  for i in range(0 ,len(get_matix)) for j in range (0 , len(get_matix)) if get_matix[i][j] in tuple_number ]
    for i in range(0 ,len(get_matix) ):
        for j in range (0 , len(get_matix) ):
            if get_matix[i][j] in tuple_number :
                counter +=1
    counter = counter + Get_number_mines
    if counter == (len(get_matix) * len(get_matix)):
        show_matrix(get_matix)
        print()
        print(clr.Fore.GREEN , ' You Win . Perfect Job!')
        time.sleep(2)
        print(clr.Fore.WHITE)
        exit()
             
#************************************************************************************************************************************
#Start main program
#This program is Minessweeper. Enjoy it
#*************************************************

#This part of my program to initialize all varible
board_size = get_number_user('How big the board should be? ' ,'Be attention, Input a integer number bigger than two !!')
mines = get_number_user('How many mines are to be placed? ' ,'Be attention, Input a integer number bigger than two !!')
print()
print(f'You must enter the correct format and find the mines.\n For example (A3 ,B2 ,...). \n no matter the uppercase or lowercase character \n \n {clr.Fore.GREEN}   {chr(10020)}  Good Luck {chr(10020) } {clr.Fore.WHITE}   ')
game_matrix = new_matrix(board_size ,0)
put_mines(mines ,game_matrix)
game_calculator(game_matrix ,board_size)
user_board = new_matrix(board_size ,chr(10047))
exit_program = True

#*****************************************************************
#if enable this line you can see all caculations of the game online
#show_matrix(game_matrix)
#*****************************************************************

show_matrix(user_board)
while True:
    print()
    msg_show = f'{clr.Fore.GREEN} {chr(10020)}{clr.Fore.YELLOW}  What field to reveal : {clr.Fore.WHITE}'
    exit_program = choose_user(input(msg_show) ,game_matrix ,user_board )
    game_win(user_board ,mines)
    if exit_program == False:
        break
    show_matrix(user_board)
    
# This is the first program in my life. I really enjoyed it . Thank you
