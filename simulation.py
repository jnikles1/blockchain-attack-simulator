import math
def get_probability(blocks_behind: int, attacker_resources: float, sum=0, index=0):
    # y is lambda
    honest_resources = 1 - attacker_resources
    y = blocks_behind * (attacker_resources / honest_resources)
    poisson_density = (y**index * math.exp(-y))/ math.factorial(index)
    catchup_probability = 1 - ((attacker_resources / honest_resources)**(blocks_behind - index))
    new_sum = sum + (poisson_density * catchup_probability)
    if index < blocks_behind:
        return get_probability(blocks_behind, attacker_resources, sum=new_sum, index=index + 1)
    else:
        return(1 - new_sum)

q = 0.1
z_nums = 11
z_inc = 1
print(f"q={q}")
for i in range(z_nums):
    z = i * z_inc
    surpass = z + 1
    probability = get_probability(surpass, q)
    print(f"z={z} P={probability}")
