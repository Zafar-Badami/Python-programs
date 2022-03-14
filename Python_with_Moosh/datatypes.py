# numbers = [2,4,15,6,4,9,2,4]
# max = 0

# for num in numbers:
#     print(num)
#     if num>=max:
#         max=num
# print(f"Largest number is {max}")
# unique=[]
# numbers = [8,9,8,1,2,4,2,3,5,6,8]
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(numbers)
# print(unique)   

num_words= {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
    }
word=""
phone = input("Phone : ")
for digit in phone:
    # word.append(num_words.get(digit))
    word += num_words.get(digit,"!") + " "
print(word)