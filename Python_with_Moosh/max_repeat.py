max_repeat=0
repeat=0
numbers=[1,2,10,3,5,6,7,10,8,3,7,7,10,12,11]
print(numbers)
# sorted_numbers=numbers # sorted(numbers)
# print(sorted_numbers)
for i in numbers:
    repeat=sorted_numbers.count(i)
    if repeat >= max_repeat:
        max_repeat = repeat
        result = i

print(f"Number : {result} , Repeats : {max_repeat}")