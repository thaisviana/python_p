def get_total(my_tuple):
    total = 0
    
    for idx, t in enumerate(my_tuple):
        sum = 0
    
        for i in t:
            total += i
            sum += i
        print(f"{idx}: {sum}")

    return total

my_tuple = ((1,5,6,10), (2,4,6,8), (2,), (10,20,30,10,80))
print(my_tuple)
    
total = get_total(my_tuple)
average = total / len(my_tuple)
print(f"A média da tupla atual é {average}")