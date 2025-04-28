def remove_elements(list):
    if len(list)>5:
        del list[5]
        del list[4]
        del list[0]
    elif len(list)==5:
        del list[4]
        del list[0]
    elif len(list)==0:
        return []    
      
    else:
        del list[0]
    return list


def add_elements(list_to_add_elements):
    list_to_add_elements.append('Yellow')
    list_to_add_elements.insert(0, 'Pink')
    return list_to_add_elements
    

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1)>=3 and len(list_to_compare2)>=3:
       if list_to_compare1[2]== list_to_compare2[2]:
        return True
       else:
        return False
    else:
        return False   


def list_of_lists(list_of_lists_to_modify):
    list1=[]    
    if len(list_of_lists_to_modify[0])>1:
        list1.append(list_of_lists_to_modify[0][0:2])
    elif len(list_of_lists_to_modify[0])==1:
        list1.append([list_of_lists_to_modify[0][0]])
    else:
        list1.append([])   
        
    if len(list_of_lists_to_modify[1])>=4:
        list1.append(list_of_lists_to_modify[1][1:4])
    elif len(list_of_lists_to_modify[1])==3:
        list1.append(list_of_lists_to_modify[1][1:3])
    elif len(list_of_lists_to_modify[1])==2:  
        list1.append(list_of_lists_to_modify[1][1])  
    else:
        list1.append([])    
    
    if len(list_of_lists_to_modify[2])>0:
        list1.append(list_of_lists_to_modify[2][-2:])
        
    else:
        list1.append([])
    return list1
