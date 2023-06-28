import sys

def print_wall(N1, N2, N3, N4, N5):
    if N1*N2 < (3*N3 + 2*N2 + N1):
        print("Type 3 brick ")
        print_brick(15)
        print("Type 2 brick ")
        print_brick(10)
        print("Type 1 brick ")
        print_brick(5)
        print("\nThe Wall")
    else:
        print("CAN NOT BE DONE")

def print_brick(brick_width):
    a = brick_width * "*"
    b = "*" +(" " * (brick_width - 2)) + "*"
    brick = print(a + "\n" + b + "\n" + a)

def build_wall(N1, N2, N3, N4, N5):
    wall_width = N1
    brick_widths = [3, 2, 1]
    brick_numbers = [N3, N4, N5]
    wall = []
    for i in range(len(brick_widths)):
        brick_width = brick_widths[i]
        brick_number = brick_numbers[i]
        while wall_width >= brick_width and brick_number > 0:
            wall_width -= brick_width
            brick_number -= 1
            wall.append(brick_width)
            if brick_width == 3:
                N3 -= 1
            elif brick_width == 2:
                N4 -= 1
            else:
                N5 -= 1
    if wall_width == 0:
        line = ""
        line1 = ""
        for j in range(len(wall)):
            line += "*****" * wall[j]
            line1 += "*" + (" " * ((wall[j]*5)-2))+"*"
        print(line)
        print(line1)
        print(line)
    return N3, N4, N5

# Get command line arguments
if len(sys.argv) != 6:
    print("Usage: python filename.py N1 N2 N3 N4 N5")
    exit(1)

N1 = int(sys.argv[1])
N2 = int(sys.argv[2])
N3 = int(sys.argv[3])
N4 = int(sys.argv[4])
N5 = int(sys.argv[5])

print_wall(N1, N2, N3, N4, N5)

while (N3 + N4 + N5 > 0) and N2 != 0:
    N2 -=1
    N3, N4, N5 = build_wall(N1, N2, N3, N4, N5)
