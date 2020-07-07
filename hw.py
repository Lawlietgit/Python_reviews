"""
Given a list [6, 8, 9, 2, 4, 1, -3, 0]
replace every number by the maximum number on its right,
for the last number replace it with -1
[9, 9, 4, 4, 0, 0, -1]
Req:
    1. Your program should be general for all lists
        edge cases like [] --> [], [1] --> [-1]
    2. it should work as expected
    3. do the time complexity analysis
"""

def replace_nums(a):

    replaced_nums=[]

    if(len(a)!=0):

        for i in range(len(a)-1):
            r=a[(i+1):]

            replaced_nums.append(max(r))

        replaced_nums.append(-1)

        return replaced_nums
    
    else:    
        return a


print(replace_nums([1,5,63,-1,-4,-2]))
print(replace_nums([4,12,124,623,-214,-21,-42,-523]))
print(replace_nums([]))
print(replace_nums([1]))

def replace_nums2(num_list):
    new_list=[-1]
    if len(num_list)!=0:
        list_max=min(num_list)
        for i in range(len(num_list)-1,-1,-1):
        
            if num_list[i]>list_max:
                list_max=num_list[i]
            else:
                num_list[i]=list_max
        
            new_list.insert(0,num_list[i])
        new_list.pop(0)
        return(new_list)
    
    else:
        return([])

print(replace_nums2([4,12,124,623,-214,-21,-42,-523]))
print(replace_nums2([]))
print(replace_nums2([1]))
print(replace_nums2([1,5,63,-1,-4,-2]))
