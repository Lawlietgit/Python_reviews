"""
hw1:
    implement a simple counter, take a list [1,1,2,1,3,3,4,2,1]
    count the number of times that each element appears, and store the
    result in a dictionary
    result_dic:
    {1:4,
     2:2,
     3:2,
     4:1}
    do this without the .count() function, do it with a single for loop 

syntax hint:
    1.create a new entry:
      dic[new_key] = new_value
    2.check if some key is in the dictionary:
      if key in dic:
         O(1)
    3.update the value of a key:
      dic[new_key] = updated_value
      dic = {1:0}
      dic[1] = dic[1] + 5
      --> dic = {1:5}
"""
#HW1:
def counter(l):
    dic={}

    for c in l:
        
        if c in dic:
            print("Yes")
            dic[c]=dic[c]+1
        else:
            print("No") 
            dic[c]=1

    print(dic)


#HW2:
class RangeSum:
    def __init__(self, input_list=[]):
        self.input_list = input_list

    def update(self, index, new_value):
        
        self.input_list[index]=new_value
        print(self.input_list)

    def rsum(self, start, end):
        s=self.input_list[start]
        f=self.input_list[end]
        total1=0
        total2=0
        for a in range(start,end+1,1):
            total1=total1+self.input_list[a]
        
        if start>0:
            for b in range(start-1):
                total2=total2+self.input_list[b]
        print(total1-total2)

counter([1,2,3,1,2,3])

rangesum = RangeSum([1,2,3,4])
rangesum.update(0,5)
rangesum.update(1,1)
rangesum.rsum(1,2)



#[5,2,3,4]
#rangesum.rsum(0,1) --> 7
#rangesum.rsum(1,3) --> 9
#rangesum.update()
"""
extra req:
    think of a senario, when you do lots lots of rsums,
    how would you improve your RangeSum object?
hint:
    any rangesum is a subtraction of 2 sums
    sum(2) - sum(0) ---> rsum(1,2)
    access these sums efficiently?
"""

