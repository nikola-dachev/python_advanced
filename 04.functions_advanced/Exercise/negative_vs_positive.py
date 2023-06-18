def bigger_sum(*args):
    negative_sum = 0
    positive_sum = 0

    for el in args:
        if el > 0:
            positive_sum += el
        else:
            negative_sum += el

    return negative_sum, positive_sum


numbers = [int(el) for el in input().split()]

negative_sum, positive_sum = bigger_sum(*numbers)

print(negative_sum)
print(positive_sum)

if positive_sum > abs(negative_sum):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")

# Another way
# def bigger_sum(positive_sum, negative_sum):
#     print(negative_sum)
#     print(positive_sum)
#
#     if positive_sum > abs(negative_sum):
#         print("The positives are stronger than the negatives")
#     else:
#         print("The negatives are stronger than the positives")
#
#
# numbers = [int(el) for el in input().split()]
# positive_list = sum([el for el in numbers if el > 0])
# negative_list = sum([el for el in numbers if el < 0])
#
# bigger_sum(positive_list, negative_list)
