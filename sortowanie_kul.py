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


def column_solved(column):
    if len(balls_colors(column)) == 1:
        print("column solved")
        return True
    else:
        print("column not solved")
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


def least_pts(points, color_list):
    lcost = (min(points))
    pts_index = points.index(lcost)
    ball_color = color_list[pts_index]
    return ball_color


def fill_empty_col(pos_of_balls, lst_pts_ball):
    for column in pos_of_balls:
        if column_empty(column) is True:
            empty_col = column
            for column in pos_of_balls:
                if column != empty_col:
                    if column[0] == lst_pts_ball:
                        empty_col.append(column[0])
                        del (column[0])
    return pos_of_balls


if __name__ == "__main__":
    file_name = "kule.txt"
    pos_of_balls = (ball_pos(file_name))
    print(pos_of_balls)
    colors = balls_colors(pos_of_balls)
    print(colors)
    mxcllght = max_col_lght(pos_of_balls, colors)
    print(mxcllght)
    points = balls_points(pos_of_balls, colors)
    print(points)
    lst_pts = least_pts(points, colors)
    print(lst_pts)
    empty = fill_empty_col(pos_of_balls, lst_pts)
    print(empty)
