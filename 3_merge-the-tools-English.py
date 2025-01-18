def merge_the_tools(string, k):
    n=len(string)
    
    #split the string into parts 
    for num in range(0,n,k):
    
    #add the string into empty list 
        trim=[]               
        for letters in string[num:num+k]:
            if letters not in trim:
                trim.append(letters)
        print(''.join(trim))
    
    

            
                
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


 