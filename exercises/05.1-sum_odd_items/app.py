my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds():
    sum_odd_numbers = 0

    for i in range(0, len(my_list)):
        if my_list[i] % 2 != 0:
            sum_odd_numbers += my_list[i]
    return sum_odd_numbers

print(sum_odds())
