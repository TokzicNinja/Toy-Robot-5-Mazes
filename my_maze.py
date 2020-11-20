import random
import turtle
from maze import obstacles


# this is to help with resizing the maze
step = 10

def is_position_blocked(x,y):
    """This function checks if the position falls inside the obstacle"""
    
    for obstacle in list_obstacles:
        x_min = min(obstacle[0][0],obstacle[1][0])
        y_min = min(obstacle[0][1],obstacle[1][1])
        x_max = max(obstacle[0][0],obstacle[1][0])
        y_max = max(obstacle[0][1],obstacle[1][1])

        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    """This function checks if there is an obstacle inline with the turtle"""
    
    for obstacle in list_obstacles:
        x_min = min(x1,x2)
        y_min = min(y1,y2)
        x_max = max(x1,x2)
        y_max = max(y1,y2)
        
        if x1 == x2:
            for i in range(y_min, y_max + 1):
                if is_position_blocked(x1, i):
                    return True
        elif y1 == y2:
            for i in range(x_min, x_max + 1):
                if is_position_blocked(i, y1):
                    return True
        else:
            return False


def all_coords():
    """This function finds all co0rdinates of a list"""
    global coordinates
    coordinates  = []
    for x in range(-90,100,step):
        for y in range(-190, 200,step):
            if not (-10 < x < step and -10 < y < step):
                coordinates.append((x,y))
    return coordinates

 
def is_neighbours(x,y,visited):
    """
    This function looks for possible neighbors
    """
    possible_neightbors = []
    if (x+step,y) in coordinates and (x+step,y) not in visited:
        possible_neightbors.append((x+step,y))
    if (x-step,y) in coordinates and (x-step,y) not in visited:
        possible_neightbors.append((x-step,y))
    if (x,y+step) in coordinates and (x,y+step) not in visited:
        possible_neightbors.append((x,y+step))
    if (x,y-step) in coordinates and (x,y-step) not in visited:
        possible_neightbors.append((x,y-step))
    if len(possible_neightbors) == 0:
            return False, []
    return True, random.choice(possible_neightbors)


def create_obstacle(old_node,current_node):
    """
    This function connects the node by drawing a line
    """
    turtle.delay(0)
    line = turtle.Turtle()
    line.speed(0)
    line.color("red")
    line.pensize(3)
    line.up()
    line.goto(old_node)
    line.down()
    line.goto(current_node)
    line.hideturtle()
    return [old_node,current_node]
   
def get_obstacles():
    """
    This function gets a list of obstacles
    """
    global list_obstacles
    list_obstacles = []
    all_coords()
    x,y = -20,-20
    current_node = (x,y)
    stack = [current_node]
    visited = [current_node]
    while True:
        is_neighbour,next_node = is_neighbours(current_node[0],current_node[1],visited)
        if is_neighbour:
            old_node = current_node
            current_node = next_node
            stack.append(current_node)
            visited.append(current_node)
            create_obstacle(old_node,current_node)
            list_obstacles.append([old_node,current_node])
        elif not is_neighbour:
            current_node = stack.pop()
        if len(visited) == len(coordinates):
            break
    return list_obstacles
  
     
def boarder():
    """This function creates the boarder"""
    t1 = turtle.Turtle()
    t1.left(90)
    t1.pencolor("red")
    t1.pensize(5)
    t1.speed(0)
    t1.up()
    t1.goto(-100,-200)
    t1.down()
    t1.goto(100,-200)
    t1.goto(100,200)
    t1.goto(-100,200)
    t1.goto(-100,-200)  
    t1.hideturtle() 


boarder()

