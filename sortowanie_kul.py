# wczytaj z pliku N lini z kolorami oddzielonymi przecinkami,
# wynikiem powinna byc sekwencja ruchow, które pozwola rozwiązać uklad.


def ball_pos(file_name):
    pos_of_balls = []
    with open(file_name, 'r') as file:
        for line in file:
            balls_in_line = line.strip().split()
            pos_of_balls.append(balls_in_line)
    return pos_of_balls


def balls_colors(ball_pos):
    color_list = []
    for i in ball_pos:
        for j in i:
            if j not in color_list:
                color_list.append(j)
    return color_list


def near_to_solve(column, mxcllght):
    color_list = []
    for j in column:
        if j not in color_list:
            color_list.append(j)
    if len(color_list) == 1 and len(column) < mxcllght:
        return True
    else:
        return False


def column_solved(column, mxcllght):
    color_list = []
    for j in column:
        if j not in color_list:
            color_list.append(j)
    if len(color_list) == 1 and len(column) == mxcllght:
        return True
    else:
        return False
    

def column_empty(column):
    if len(column) == 0:
        return True


def max_col_lght(ball_pos, colors_list):
    num_col = len(colors_list)
    lenpoints = sum(len(column) for column in ball_pos)
    mxcllght = lenpoints // num_col
    return mxcllght


def balls_points(ball_pos, color_list):
    points = []
    for color in color_list:
        ball_points = 0
        for column in (ball_pos):
            for idx, ball in enumerate(column):
                if ball == color:
                    ball_points += idx
        points.append(ball_points)
    return points


def higst_pts(points, color_list):
    mcost = (max(points))
    pts_index = points.index(mcost)
    ball_color = color_list[pts_index]
    return ball_color

def lwst_pts(points, color_list):
    mcost = (min(points))
    pts_index = points.index(mcost)
    ball_color = color_list[pts_index]
    return ball_color

def pos_solved(pos_of_balls, mxcllght):
    for column in pos_of_balls:
        if column_solved(column, mxcllght) or len(column) == 0:
            continue
        else:
            return False
    return True


def empty_col_color(pos_of_balls, mxcllght, color_list):
    for a in range(len(color_list)):
        crpts = balls_points(pos_of_balls, color_list)
        ball_color = higst_pts(crpts, color_list)
        for eidx, empty_col in enumerate(pos_of_balls):
            if column_empty(empty_col) is True:
                for cidx, column in enumerate(pos_of_balls):
                    while len(column) > 0 and column[-1] == ball_color and cidx != eidx:
                        if near_to_solve(column, mxcllght) is True:
                            break
                        print("column ", cidx, " to column ", eidx)
                        empty_col.append(column[-1])
                        del (column[-1])
        if len(crpts) > 1:
            hptsidx = (color_list.index(ball_color))
            del(crpts[hptsidx], color_list[hptsidx])
            crpts = balls_points(pos_of_balls, color_list)
            ball_color = higst_pts(crpts, color_list)
    return pos_of_balls


# def filling_columns(pos_of_balls, mxcllght, color_list):
#     for a in range(len(color_list)):
#         for ntslvidx, ntslv in enumerate(pos_of_balls):
#             if near_to_solve(ntslv, mxcllght) is True:
#                 ball_color = ntslv[-1]
#                 for cidx, column in enumerate(pos_of_balls):
#                     while len(column) > 0 and column[-1] == ball_color and cidx != ntslvidx:
#                         print("column ", cidx, " to column ", ntslvidx)
#                         ntslv.append(column[-1])
#                         del (column[-1])
#     return pos_of_balls


# def sorting_balls(pos_of_balls, mxcllght, color_list):
#     balls_pts = balls_points(pos_of_balls, color_list)

#     for a in range(len(color_list)):
#         color_listcp = color_list.copy()
#         crpts = balls_pts.copy()
#         ball_color = higst_pts(crpts, color_listcp)

#         for fmidx, fm_col in enumerate(pos_of_balls):
#             if len(fm_col) > 0 and fm_col[-1] == ball_color:
#                 for tcidx, to_col in enumerate(pos_of_balls):
#                     if to_col[-1] == ball_color and tcidx != fmidx:
#                         print("bjnfgrwsbbhsrgfhjbvfsrhvjfrshjvgjvh")

#                         while mxcllght != len(to_col) and tcidx != fmidx and to_col[-1] == ball_color and fm_col[-1] == ball_color:
#                             print("column ", fmidx, " to column ", tcidx)
#                             to_col.append(fm_col[-1])
#                             del (fm_col[-1])

#         if len(crpts) > 1:
#             hptsidx = (color_listcp.index(ball_color))
#             del(crpts[hptsidx], color_listcp[hptsidx])

#     return pos_of_balls


# important
def check_moves(pos_of_balls, mxcllght):

    all_posible_moves = []

    for fmidx, from_col in enumerate(pos_of_balls):

        if column_solved(from_col, mxcllght) != True:

            if len(from_col) > 0:
                
                for tcidx, to_col in enumerate(pos_of_balls):
                    ball_move = []

                    if len(to_col) == 0 or to_col[-1] == from_col[-1]:
                        if tcidx != fmidx and  len(to_col) < mxcllght:
                            ball_move.append(fmidx)
                            ball_move.append(tcidx)
                            all_posible_moves.append(ball_move)
    return all_posible_moves


def make_move(pos_of_balls, move):            
    pos_of_balls = copy.deepcopy(pos_of_balls)
            
    pos_of_balls[move[1]].append(pos_of_balls[move[0]][-1])
    del pos_of_balls[move[0]][-1]
    print("column ", move[0], " to column ", move[1])
    return pos_of_balls
                    


def make_n_move(pos_of_balls, mxcllght, last_move, count):
    all_posible_moves = check_moves(pos_of_balls, mxcllght)
    for move in all_posible_moves:
        m_puzzle = make_move(pos_of_balls, move)
        print(m_puzzle)
        if last_move != None and [last_move[1], last_move[0]] == move:
            count += 1
            if count > 5:
                count = 0
                break
                
        last_move = move
        if pos_solved(m_puzzle, mxcllght) == True:
            return m_puzzle
        
        if len(check_moves(m_puzzle, mxcllght)) != 0:
            cp_puzzle = copy.deepcopy(m_puzzle)
            make_n_move(cp_puzzle, mxcllght, last_move, count)


# def count_moves(moves):
#     count = 0
#     for move in moves:
#         for move_2 in moves:
#             if move == move_2 or [move[1], move[0] == move_2]:
#                 count += 1
#                 if count >


if __name__ == "__main__":

    import copy

    file_name = "data.txt"
    mod_pos = [['pink', 'lime', 'blue', 'red'], ['pink', 'pink', 'red', 'blue', 'green'], ['lime', 'lime', 'pink', 'green', 'pink'], ['orange', 'purple', 'purple', 'orange', 'blue'], ['blue', 'green', 'light_blue', 'purple', 'gray'], ['green', 'lime', 'green', 'blue', 'orange'], ['light_blue', 'light_blue', 'orange', 'light_blue', 'red'], ['light_blue', 'purple', 'red', 'red', 'lime'], ['gray', 'gray', 'orange', 'purple', 'gray'], ['gray'], []]

    pos_of_balls = (ball_pos(file_name))
    print(pos_of_balls)

    color_list = balls_colors(pos_of_balls)
    # print(color_list)

    mxcllght = max_col_lght(pos_of_balls, color_list)
    # print(mxcllght)

    points = balls_points(pos_of_balls, color_list)
    print(f'Column points {points}')

    hig_pts = higst_pts(points, color_list)
    

    possible_moves = check_moves(pos_of_balls, mxcllght)
    # mod_possible_moves = check_moves(mod_pos, mxcllght)
    print(f'possible moves: {possible_moves}')
    # print(f'mod possible moves: {mod_possible_moves}')
    solve = make_n_move(pos_of_balls, mxcllght, None, 0)
    print(solve)
    # print(f'puzzle after moves: {pos_of_balls}')
    
    # all_moves = check_moves(pos_of_balls, mxcllght)
    # mak = make_move(pos_of_balls, mxcllght)
    # print(mak)