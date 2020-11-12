import random


obstacle_lst = []
obst_check = False
def create_random_obstacles():
    """
    Randomizes the amount and position of obstacles
    """
    global obstacle_lst
    
    obstacle_lst = [(random.randint(-99,99), random.randint(-199, 199)) for i in range(random.randint(1,10))]
    return obstacle_lst


def is_position_blocked(x, y):
    """
    Makes sure robot cannot occupy the same space as the robot
    """
    global obst_check
    for i in range(len(obstacle_lst)):
        x_check = obstacle_lst[i][0]
        y_check = obstacle_lst[i][1]
        if y_check <= y <= (y_check + 4) and x_check <= x <= (x_check + 4):
            obst_check = True
            return True
    obst_check = False
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    -Blocks the robot from skipping the obstacles
    -Returns true if there is an obstacles
    """
    global obstacle_lst
    global obst_check
    obst_check = True
    for i in obstacle_lst:
        obs_x = i[0]
        obs_y = i[1]
        if x1 == x2 and (obs_x <= x1 and x1 <= obs_x + 4):
            if y2 < obs_y:
                return y1 >= obs_y
            elif y2 > obs_y + 4:
                return y1 <= obs_y + 4
        elif y1 == y2 and (obs_y <= y1 and y1 <= obs_y + 4):
            if x2 < obs_x:
                return x1 >= obs_x
            elif x2 > obs_x + 4:
                return x1 <= obs_x + 4
    obst_check = False
    return False

# random_


maze = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXX         X           X",
"X X XXXXX XXXXXX XXXXXX X",
"X X    TX        X      X",
"X XXXXXXX XXXXXXXXXXXXX X",
"X         X  TX X     X X",
"XXXXX XXXXX XXX X XXXXX X",
"X   X X     X X         X",
"X X X   XXXXX X XXXXXXXXX",
"X X XXXXX               X",
"X X       XXXXXXXXX XXX X",
"X XXXXXX XX       X XTX X",
"X      X  X  XXXX X X X X",
"XXXXXX XX X     X X X X X",
"X       XTX XX XXXX X X X",
"X XXXXXXXXX X     X X   X",
"X X     X   XXXXX X XXXXX",
"X XXX X X X X  TX X    TX",
"X     X X X X XXX XXXXXXX",   
"XXXXX X   X X   X X     X",
"X   X XXXXXXXXX X   XXX X",
"X XTX X       X XXXXX   X",
"X XXX XXXXX X X   XTX   X",
"X           X   X   X   X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]
def get_obstacles():
    global obstacle_lst
    setup_maze()
    return obstacle_lst

def setup_maze():
    global obstacle_lst
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            character = maze[y][x]

            screen_x = -96 + (x * 8)
            screen_y = 196 - (y * 16)

            if character == 'X':
                obst = (screen_x,screen_y)
                obst1 = (screen_x - 4, screen_y)
                obst2 = (screen_x, screen_y -4)
                obst3 = (screen_x - 4, screen_y -4)
                obst4 = (screen_x, screen_y -8)
                obst5 = (screen_x -4, screen_y -8)
                obst6 = (screen_x -4, screen_y -12)
                obst7 = (screen_x , screen_y -12)

                obstacle_lst.append(obst)
                obstacle_lst.append(obst1)
                obstacle_lst.append(obst2)
                obstacle_lst.append(obst3)
                obstacle_lst.append(obst4)
                obstacle_lst.append(obst5)
                obstacle_lst.append(obst6)
                obstacle_lst.append(obst7)
                

                
    return obstacle_lst
