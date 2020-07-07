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



"""
hw2:
    class RangeSum:
        def __init___(self, input_list):
            pass

        def update(self, index, new_value):
            pass

        def rsum(self, start, end):
            pass

rangesum = RangeSum([1,2,3,4])
rangesum.update(0,5)
--> [5,2,3,4]
rangesum.rsum(0,1) --> 7
rangesum.rsum(1,3) --> 9
rangesum.update()

extra req:
    think of a senario, when you do lots lots of rsums,
    how would you improve your RangeSum object?
hint:
    any rangesum is a subtraction of 2 sums
    sum(2) - sum(0) ---> rsum(1,2)
    access these sums efficiently?
"""

