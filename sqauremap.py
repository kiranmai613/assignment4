# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]
def s_n(num):
    return num*num
l_n=[4,5,2,9]
print("original is :",l_n)
result=map(s_n,l_n)
print("result is  " ,list(result))

