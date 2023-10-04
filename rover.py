class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def status_report(self):
        return f"Rover is at: ({self.x}, {self.y}), Facing: {self.direction}."

class MarsGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def has_obstacle(self, x, y):
        return (x, y) in self.obstacles

class MarsRover(Rover):
    DIRECTIONS = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0),
    }

    TURN_LEFT = {
        'N': 'W',
        'S': 'E',
        'E': 'N',
        'W': 'S',
    }

    TURN_RIGHT = {
        'N': 'E',
        'S': 'W',
        'E': 'S',
        'W': 'N',
    }

    def __init__(self, grid, x, y, direction):
        super().__init__(x, y, direction)
        self.grid = grid

    def move(self):
        move_x, move_y = self.DIRECTIONS[self.direction]
        next_x, next_y = self.x + move_x, self.y + move_y
        if 0 <= next_x < self.grid.width and 0 <= next_y < self.grid.height:
            if not self.grid.has_obstacle(next_x, next_y):
                self.x, self.y = next_x, next_y
    def turn_left(self):
        self.direction = self.TURN_LEFT[self.direction]

    def turn_right(self):
        self.direction = self.TURN_RIGHT[self.direction]

    def execute_commands(self, commands):
        for command in commands:
            if command == 'M':
                self.move()
            elif command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
        print(f"Final Position: ({self.x}, {self.y}, {self.direction})")
grid = MarsGrid(10,10)
grid.add_obstacle(2,2)
grid.add_obstacle(3,5)
rover = MarsRover(grid, 0, 0, 'N')
commands = ['M','M','R','M','L','M']
rover.execute_commands(commands)
print(rover.status_report())