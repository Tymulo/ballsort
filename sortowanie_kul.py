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

4r2tfggt53y
# def sorting_balls(pos_of_balls, mxcllght, color_list):
#     for a in range(len(color_list)):
#         crpts = balls_points(pos_of_balls, color_list)
#         ball_color = higst_pts(crpts, color_list)
#         for ntslvidx, ntslv in enumerate(pos_of_balls):
#             print(near_to_solve(ntslv, mxcllght), ntslv[-1], ball_color )
#             if near_to_solve(ntslv, mxcllght) is True and ntslv[-1] == ball_color:
#                 for cidx, column in enumerate(pos_of_balls):
#                     while len(column) > 0 and column[-1] == ball_color and cidx != ntslvidx:
#                         print("column ", cidx, " to column ", ntslvidx)
#                         ntslv.append(column[-1])
#                         del (column[-1])
#         if len(crpts) > 1:
#             hptsidx = (color_list.index(ball_color))
#             del(crpts[hptsidx], color_list[hptsidx])
#             crpts = balls_points(pos_of_balls, color_list)
#             ball_color = higst_pts(crpts, color_list)
#     return pos_of_balls


if __name__ == "__main__":
    file_name = "kule.txt"
    pos_of_balls = (ball_pos(file_name))
    print(pos_of_balls)
    color_list = balls_colors(pos_of_balls)
    print(color_list)
    mxcllght = max_col_lght(pos_of_balls, color_list)
    print(mxcllght)
    points = balls_points(pos_of_balls, color_list)
    print(points)
    hig_pts = higst_pts(points, color_list)
    print(hig_pts)
    empty = empty_col_color(pos_of_balls, mxcllght, color_list)
    print(empty)
    # srt_blls = sorting_balls(pos_of_balls, mxcllght, color_list)
    # print(srt_blls)
    