#Write a Python program to check whether a specified value is contained in a group of values. Test Data : 3 -> [1, 5, 8, 3] : True -1 -> [1, 5, 8, 3] : False

def grp_mem(group_data, n):
 return n in group_data

print(grp_mem([1, 5, 8, 3], 3))
print(grp_mem([1, 5, 8, 3], -1))
   
