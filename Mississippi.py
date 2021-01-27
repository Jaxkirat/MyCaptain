def most_frequent(string):
    d = dict()
    for key in string:
       if key not in d:
           d[key] = 1
       else:
           d[key] += 1
    a= sorted(d.items(), key =lambda x:x[1] , reverse = True) 

    return a
    
print (most_frequent("Mississippi"))
            
