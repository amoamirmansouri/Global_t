#import math
lst1 = [1,4,6,7,10]
lst2 = [2,3,5,8]
lst3 = list()
len1 =len(lst1) 
len2 =len(lst2)
#print(dir(math))
i = j = 0
while i < len1 and j < len2:
    if lst1[i]<lst2[j]:
        lst3.append(lst1[i])
        i+=1
    else:
        lst3.append(lst2[j])
        j += 1

lst3 += lst1[i:]
lst3 += lst2[j:]
print(lst3)
