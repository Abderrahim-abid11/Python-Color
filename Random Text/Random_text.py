import random
import time
import sys

list_color = ["\033[0;30m", 
        "\033[0;31m", 
        "\033[1;30m", 
        "\033[1;31m", 
        "\033[1;32m", 
        "\033[0;32m", 
        "\033[0;34m", 
        "\033[1;34m", 
        "\033[0;33m", 
        "\033[1;33m", 
        "\033[0;35m", 
        "\033[1;35m", 
        "\033[0;37m", 
        "\033[1;37m", 
        "\033[0m"]

print("\n\n")
for i in range(0,15):
    color_range = random.randint(0,14)
    print(list_color[color_range], end="")
    sys.stdout.write('\r' + f"\tHello, World!")
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write('\r')
    sys.stdout.flush()
