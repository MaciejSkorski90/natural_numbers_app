#!/usr/bin/env python
# coding: utf-8

# In[2]:


number = 20

N = [*range(0, (number + 1))]

final_list = [[a, b] for x, a in enumerate(N) for b in N[x + 1:] if a + b == number]

with open("final_list.txt", "w") as output:
    output.write(str(final_list))


##alternative solution
#
#import itertools
#
#final_list = [x for x in itertools.combinations(N, 2) if x[0] + x[1] == number]
#final_list

