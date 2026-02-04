# Robot Maze Navigator (PyCharm Version)

maze = [
    ['S', '.', '#', '.'],
    ['#', '.', '#', '.'],
    ['.', '.', '.', '.'],
    ['#', '#', '.', 'G']
]

robot_position = [0, 0]  # starting at 'S'


def display_maze():
    for row in maze:
        print(" ".join(row))
    print()


def at_goal():
    row, col = robot_position
    return maze[row][col] == 'G'


def move_down():
    if robot_position[0] + 1 < len(maze) and maze[robot_position[0] + 1][robot_position[1]] != '#':
        robot_position[0] += 1


def move_right():
    if robot_position[1] + 1 < len(maze[0]) and maze[robot_position[0]][robot_position[1] + 1] != '#':
        robot_position[1] += 1


def move_up():
    if robot_position[0] - 1 >= 0 and maze[robot_position[0] - 1][robot_position[1]] != '#':
        robot_position[0] -= 1


def move_left():
    if robot_position[1] - 1 >= 0 and maze[robot_position[0]][robot_position[1] - 1] != '#':
        robot_position[1] -= 1


# Simple logic to reach goal
display_maze()

while not at_goal():
    move_right()
    move_down()
    display_maze()

print("🎉 Robot reached the goal!")
