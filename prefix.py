## this  a algoritheme to  get the common prefix of a list of string inputs

def longestCommonPrefix(strs):
        x=""
        for i in strs:
            if i=="":
                return ""
        for i in range(len(strs[0])):
            first=strs[0]
            trouve=True
            for j in strs[1:]:   
               
                if i < len(j):
                    if j[i] != first[i]:
                        trouve =False
                else:
                    trouve=False
            if trouve==True:
                x+=strs[0][i]
              
            else:
                return x
                
        return x
            
            
                
                    
print(longestCommonPrefix( ["ab","a"]))