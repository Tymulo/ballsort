#- wczytaj z pliku N lini z kolorami oddzielonymi przecinkami, wynikiem powinna byc sekwencja ruchow, które pozwola rozwiązać uklad.
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
def max_column_length(ball_pos, colors_list):
    num_col = len(colors_list)
    lenpoints = sum(len(column) for column in ball_pos)
    mxcllght = lenpoints // num_col
    return mxcllght
def balls_points(ball_pos, color_list, mxcllght):
    T = []
    for color in color_list:
        ilosc_pkt = 0
        for idx, balls in enumerate(ball_pos):
            if color in balls:
                ilosc_pkt += idx
        T.append(ilosc_pkt)
    return T, mxcllght
def least_pts(T,color_list):
    i = T.index(min(T))
    ball_color = color_list[i]
    return ball_color
if __name__ == "__main__":
    file_name = "kule.txt"
    pos_of_balls=(ball_pos(file_name))
    print(pos_of_balls)
    colors = balls_colors(pos_of_balls)
    print(colors)
    mxcllght = max_column_length(pos_of_balls, colors)
    print(mxcllght)
    points = balls_points(pos_of_balls, colors, mxcllght)
    print(points)