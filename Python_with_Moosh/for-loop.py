# prices=[10,20,30]
# total=0
# for i in prices:
#     total += i
#     print(i)
# print("Total: " + str(total))

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

numbers = [5,2,5,2,2]
# for num in numbers:
#     print(f"x"*num)
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output +='x'
    print(output)
