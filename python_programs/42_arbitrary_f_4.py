# 3) create function that has arbitary arguments of string type and it display all strings into lower case.
# toLowerCase('Apple','bAnana','ManGO','KIWI','graps')
# output 
#     apple banana mango kiwi graps


def tolower(*str):
    l = []
    for i in str:
       l.append(i.lower())
       r= " ".join(l)
    return r   

d = tolower("kp","hh","HY","GG") 
print(d)