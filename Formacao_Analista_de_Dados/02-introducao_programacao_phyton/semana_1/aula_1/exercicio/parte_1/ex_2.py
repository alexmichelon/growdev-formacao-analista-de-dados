import numpy as np

total_area = np.array(
    [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'BB'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B'],
[' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', 'B', ' ', 'B'],
[' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', 'B', ' ', 'B'],
[' ', ' ', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', 'B'],
[' ', ' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B'],
[' ', ' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B'],
[' ', ' ', 'B', ' ', 'B', 'B', 'B', ' ', ' ', ' ', ' '],
[' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
)

positions_visited = np.array(
[
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'BB'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'B'],
[' ', ' ', ' ', ' ', ' ', ' ', 'B', 'B', 'B', ' ', 'B'],
[' ', ' ', ' ', ' ', ' ', ' ', 'B', ' ', 'B', ' ', 'B'],
[' ', ' ', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', 'B'],
[' ', ' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B'],
[' ', ' ', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B'],
[' ', ' ', 'B', ' ', 'B', 'B', 'B', ' ', ' ', ' ', ' '],
[' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', 'B', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]
)


line = 11
column = 0
list_visited_positions = []

def check_up(line, column):
    if ([line-1,column] not in list_visited_positions):
        if (total_area[line-1,column] == 'B') or (total_area[line-1,column] == 'BB'):
            positions_visited[line-1,column] = 'X'
            list_visited_positions.append([line-1,column] )            
            return True
    return False
    
def check_right(line, column):
    if([line,column+1] not in list_visited_positions):
        if (total_area[line,column+1] == 'B') or (total_area[line,column+1] == 'BB'):
            positions_visited[line,column+1] = 'X'
            list_visited_positions.append([line,column+1])
            return True
    return False

def check_left(line, column):
    if([line,column-1] not in list_visited_positions):
        if (total_area[line,column-1] == 'B') or (total_area[line,column-1] == 'BB'):
            positions_visited[line,column-1] = 'X'
            list_visited_positions.append([line,column-1])
            return True
    return False

def check_down(line, column):
    if([line+1,column] not in list_visited_positions):
        if (total_area[line+1,column] == 'B') or (total_area[line+1,column] == 'BB'):
            positions_visited[line+1,column] = 'X'
            list_visited_positions.append([line+1,column])
            return True
    return False


while(total_area[line, column] != 'BB'):
    while(total_area[line, column] != 'BB'):
        if(check_up(line,column) == True):
            line = line - 1
            break

        elif(check_right(line, column) == True):
            column = column + 1
            break

        elif(check_left(line, column) == True):
            column = column - 1
            break

        elif(check_down(line, column) == True):
            line = line + 1
            break
        else:            
            [line, column] = list_visited_positions[list_visited_positions.index([line, column])-1]
    if (total_area[line, column] == 'BB'):
        print('\n\nORIGINAL PATH\n' + str(total_area))
        print('\n\nPATH TRAVELLED\n' + str(positions_visited))
        print('\nPOSITIONS VISITED (BESIDE)\n' + str(list_visited_positions))
        print('\nPOSITIONS VISITED (UNDER)')
        [print(position_list) for position_list in list_visited_positions]
        break            

