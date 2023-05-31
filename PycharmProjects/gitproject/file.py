# Find Common Elements in Multiple Lists:
# python
"""
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
list3 = [3, 4, 5, 8]
l = []
for i,j,k in zip(list1,list2,list3):
    l.append(i)
    l.append(j)
    l.append(k)
for ele in l:
    if l.count(ele)>1:
        print(ele)
"""
# Checking for Anagrams
s = "listen"
s1 = "silent"
f = 0
for index in s:
    if index not in s1:
        f=1
if f == 0:
    print("anagram")
else:
    print("not anagram")

# wap to print Sum of List Elements
l = [1,2,3,4]
print(sum(l))