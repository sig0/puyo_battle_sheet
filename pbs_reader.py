from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3
    yellow = 4
    purple = 5
    ojama = 6


class Field:

    def __init__(self):
        self.width = 6
        self.height = 14
        self.field = [0 for x in range(self.width * self.height)]
        self.field[10] = Color.blue.value

    def print_field(self):
        str_field = []
        for line in range(self.height):
            index = line * self.width
            linestr = "".join([str(x) for x in self.field[index:index + self.width]])
            str_field.append(linestr)
        reversed_height = [str(x) + "  " if x < 10 else str(x) + " " for x in reversed(range(self.height))]
        [print("".join(x)) for x in zip(reversed_height, reversed(str_field))]



if __name__ == "__main__":
    print("hey")
    print(Color.red.value)
    f = Field()
    f.print_field()
