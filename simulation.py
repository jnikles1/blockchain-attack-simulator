import random
# inputs
# t = alotted number of trials
# q = the amount of computing resources owned by attacker
# z = the number of blocks that the attacker is behind

def does_hacker_win(z, target):
    count = 0
    while ( count < 100 ):    
        random_num = random.randrange(0, 99)
        if random_num < target:
            z = z - 1
            # winner, decrement z
        else:
            z = z + 1
            # loser, increment count
        if z == 0:
            return(True)
        count = count + 1
    return(False)

q = .40
target = q * 100
z = 5
t = 10000

# calculate poisson
p = 1 - q



# for each trial, pick random number between 0 and 99. 
# if number is less than target, the attacker wins the block and z is decremented
# otherwise, z is incremented

count = 0 
wins = 0
while (count < t):
    if does_hacker_win(z, target):
        wins = wins + 1
    count = count + 1
probability_of_catching_up = wins / t
print(f"z={z} P={probability_of_catching_up}")