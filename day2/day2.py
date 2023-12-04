
FILE = 'input.txt'

# Part 1: Find sum of ids of all possible games 
MAX = {
    'red' : 12,
    'green' : 13,
    'blue' : 14,
}

with open(FILE) as f:
    sum = 0

    for game_id, line in enumerate(f.readlines(), 1):
        rounds = line.strip().split(": ")[1].split("; ")

        flag = 1 #0 if game is not valid, 1 otherwise 

        for round in rounds:
            cubes = round.split(", ")

            for cube in cubes:
                num, col = cube.split(" ")

                if int(num) > MAX[col]:
                    flag = 0
                    break
            
            if flag == 0:
                break

        if flag == 1:
            sum += game_id
    
    print(sum)


#Part 2: Find the minimum number of each color needed for a game. 
# Find the power (the min number of red * min green * min blue)
# Find the sum of all of the powers of all games.

with open(FILE) as f:
    pow_sum = 0

    for line in f.readlines():
        rounds = line.strip().split(": ")[1].split("; ")
        min_bag = {'red':0, 'green':0, 'blue':0}

        for round in rounds:
            cubes = round.split(", ")

            for cube in cubes:
                num, col = cube.split(" ")

                min_bag[col] = max(min_bag[col], int(num))
        
        pow_sum += min_bag['red'] * min_bag['green'] * min_bag['blue']

    print(pow_sum)

