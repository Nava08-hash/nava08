# from unittest import result


# list=[1,2,3,45,2]
# print(list[4])
# print(list[:4])

# #concatenation operator
# a=[1,2,3]
# b=[4,5]
# print(a+b)
# #repetiton operator
# num=[1,2]
# print(num*3)
# #membership operator(in,not-in)-->returns bool value
# fruits=["apple","banana","grapes"]
# print("apple" in fruits)
# print("orange" not in fruits)
# #comparsion operator
# listone=[1,2,3]
# listtwo=[1,2,4]
# print(listone==listtwo)
# print(listone<listtwo)

# #list methods
# #1)append()-element will be merged at last
# num=[1,2,3]
# num.append(4)
# print(num)
# #insert()method 
# num.insert(2,5)
# print(num)
# #extend()method
# num.extend([6,7])
# print(num)
# #remove()method
# num=[1,2,3,4]
# num.remove(4)
# print(num)
# #pop()method
# num=[5,6,7,8]
# num.pop(1)
# print(num)
# #clear()method
# num=[4,8,12,16]
# num.clear()
# print(num)
# #count(method)
# print(num.count(2))
# #sort(method)
# a=[4,5,34,9,23]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# #reverse
# a.reverse()
# print(a)
# #copy()
# b=a.copy()
# print(b)
# #map(),filter() and list()
# #should use it on list
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, numbers))
# print(squared)
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(result)
# 
#partition--A value that reads the same backward and forward

#1st method-->slicing 
# word=input("enter a word:")
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")
# #without slicing
# word=input("enter a word:") #madam
# rev=""
# for ch in word: 
#     rev=ch+rev   

# if word==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

#without slicing-->only for numbers

num=int(input("enter a number:"))
original=num
rev=0
while num>0:
    digit=num%10 #1
    rev=rev*10+digit #1
    num=num//10      #12
print(rev)
if original==rev:
    print("palindrome")
else:
    print("not palindrome")

digit        rev           num
                           121    
1            1             12
2            12            1


def remove_duplicates(sorted_list):
    if not sorted_list:
        return []

    # Initialize result with the first element
    result = [sorted_list[0]]

    # Iterate through the list
    for i in range(1, len(sort


