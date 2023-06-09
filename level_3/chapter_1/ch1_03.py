"""
Chapter 1 - Python Advanced (1) : Shallow & Deep copy
Keywords : shallow & deep copy
"""
# imports ==============================================================================================================
import copy
# ======================================================================================================================
"""  # =================================================================================================================
Types of copying object: Copy, Shallow Copy, Deep Copy
mutable : list, set, dict
"""  # =================================================================================================================

# Copy =================================================================================================================
# Ex 1 -----------------------------------------------------------------------------------------------------------------
# Call by value, Call by Reference, Call by Share
a_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b_list = a_list  # copy reference
print("Ex 1 > ", id(a_list))
print("Ex 1 > ", id(b_list))  # same id -> same object

b_list[2] = 100
print("Ex 1 > ", a_list)
print("Ex 1 > ", b_list)  # same results

b_list[3][2] = 100
print("Ex 1 > ", a_list)
print("Ex 1 > ", b_list)  # same results
# a and b point to same object (copy reference)
# Copy -> copy reference

# immutable : int, str, float, bool, unicode, ...
print()
# ======================================================================================================================

# Shallow Copy =========================================================================================================
# Ex 2 -----------------------------------------------------------------------------------------------------------------
# import copy
c_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
d_list = copy.copy(c_list)  # shallow copy - copy value
print("Ex 2 > ", id(c_list))
print("Ex 2 > ", id(d_list))  # different id

d_list[1] = 100
print("Ex 2 > ", c_list)
print("Ex 2 > ", d_list)

d_list[3].append(1000)
d_list[4][1] = 10000
print("Ex 2 > ", c_list)
print("Ex 2 > ", d_list)
# 리스트 안에 요소로써 존재하는 리스트는 복사할 때 값이 아닌 주소값을 가져옴
print("Ex 2 > ", id(c_list[3]))
print("Ex 2 > ", id(d_list[3]))
print()
# ======================================================================================================================

# Deep Copy ============================================================================================================
# Ex 3 -----------------------------------------------------------------------------------------------------------------
e_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
f_list = copy.deepcopy(e_list)  # deep copy
print("Ex 3 > ", id(e_list))
print("Ex 3 > ", id(f_list))

f_list[1] = 100
print("Ex 3 > ", e_list)
print("Ex 3 > ", f_list)

f_list[3].append(1000)
f_list[4][1] = 10000
print("Ex 3 > ", e_list)
print("Ex 3 > ", f_list)
# 리스트 안에 요소로써 존재하는 리스트도 완전 사본으로 복사
print("Ex 3 > ", id(e_list[3]))
print("Ex 3 > ", id(f_list[3]))
# ======================================================================================================================
