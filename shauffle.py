def restoreString( s, indices):
        tmp=list(s)
        for i in range(len(s)):
    
            tmp[indices[i]]=s[i]
        return "".join(tmp)
print(restoreString("codeleet",[4,5,6,7,0,2,1,3]))