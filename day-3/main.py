with open("input", "r") as f:
    numbers = [l.strip() for l in f.readlines()]

res = []

# part 1
for i in range(0, len(numbers[0])):
    bits = [x[i] for x in numbers]
    zeros = [x for x in bits if x == '0']
    ones = [x for x in bits if x == '1']
    if len(zeros) > len(ones):
        res.append(0)
    else:
        res.append(1)

inv = [(x + 1) % 2 for x in res]
res = ''.join([str(x) for x in res])
inv = ''.join([str(x) for x in inv])

a = int(res, 2)
b = int(inv, 2)
print(a * b)

# part 2: TODO
