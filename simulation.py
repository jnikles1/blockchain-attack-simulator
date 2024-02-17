import math
def get_probability(blocks_behind: int, attacker_resources: float, sum=0, index=0):
    # y is lambda
    honest_resources = 1 - attacker_resources
    y = blocks_behind * (attacker_resources / honest_resources)
    blocks_to_surpass = blocks_behind + 1
    poisson_density = (y**index * math.exp(-y))/ math.factorial(index)
    catchup_probability = 1 - ((attacker_resources / honest_resources)**(blocks_to_surpass - index))
    new_sum = sum + (poisson_density * catchup_probability)
    if index < blocks_to_surpass:
        return get_probability(blocks_behind, attacker_resources, sum=new_sum, index=index + 1)
    else:
        return(1 - new_sum)

q = 0.32
z_nums = 11
z_inc = 1
print(f"q={q}")
for i in range(z_nums):
    z = i * z_inc
    probability = get_probability(z, q)
    print(f"z={z} P={probability}")
