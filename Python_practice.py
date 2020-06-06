def average(numList):
    num_count = len(numList)
    num_sum = sum(numList)

    return num_sum/num_count, len(numList)

num1 = [2,3,4]
print(average(num1))

def sqr(num):
    sqr_num = num ** 2
    return sqr_num

print(sqr(3))