# 4 basic python data types:
    # string, boolean, int, float
    # str(), bool(), int(), float()
    # bool("False") --> True
    # bool("") --> False
    # bool(10.2351236) --> True
    # bool(0.0) --> False
    # bool(object/[1,2,3]) --> True
    # bool([]) --> False
    # bool(None) --> False

# FIFO --> queue data structure
# LIFO --> stack
a = [1,2,3]
# queue:
for _ in range(len(a)):
    print(a.pop(0))
print(a)

a = [1,2,3]
# while len(a) > 0:
while a:
    print(a.pop(0))
print(a)

# stack:
a = [1,2,3]
while a:
    print(a.pop())
print(a)

# class/objects (scalable/extensible)
# e.g. build a system for a library
    # people can register as a user/member
    # members can check-out and return books
    # books should be classified by generics

class Books:
    attrs: cost/n_stocks/popularity/theme
    methods:

#class MusicBooks(Books):
#    attrs:

class Users:
    attrs: member_id(KEY)/account balance/age/email/dob/name
    methods: check_out(book)/return_book(book)

# time complexity (big O notation)
# space complexity (big O notation)
# 2 types of problems:
    # P - Polynomial (O(N), O(N^2), O(N^p))
    # NP - not possible for Poly time
        # NP - problem itself cannot be solved in P, but verifying the problem takes P
        # NP hard - verifying it takes more than P (postman)
        # A

        # B

        # C

        #   A  B   C
        #A  0  21  
        #B 21  0   40
        #C     40   0
        # A - B --> 21 km
        # B - C --> 40 km ...
        # A --> A search for the best route (shortest total distance) to connect all the towns,
        # and return to A.
        # loop (keep visiting a town many times)
    # N --> infinity
    # O(a*N^c + b) a, b, c are constants --> O(N^c)

# dictionary/sets
# visit element time O(1)
# a = [1,2,3, 3,3,3,3,3], a[0]
# check if 3 is in a:
# a_set = {1,2,3}
# check if 3 is in a set:
# in a set, the elements have to be unique
# a set can be used as the key set for a dictionary
# a_dic = {0:2, 1:2} k:v a_dic[0] -->2
"""
print(3 in a) --> True O(N)
print(3 in a_set) --> True O(1)
a_lis.append(), .remove(), .pop(), .insert()
a_set.add(), .remove()
a_dic[new_key] = new_value, a_dic.remove(key)
"""



