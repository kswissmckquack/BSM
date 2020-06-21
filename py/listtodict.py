# Python3 program to Convert a  
# list to dictionary 
  
def Convert(lst): 
    it = iter(lst) 
    res_dct = dict(zip(it, it)) 
    return res_dct 