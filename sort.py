def Sort_Tuple(lst1): 
   

    lst1.sort(key = lambda x: x[-1]) 
    return lst1 
  
lst1=['2','4','1','3',]
lst2 = ['great','hello','hiyo','abc'] 


lst2.sort(key=lambda x:x[-2])
print((Sort_Tuple(lst1)),lst2)