def romanToInt(s):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        mylist=[]
        i=0
        while i <len(s):
         
          if i+1<len(s) and  s[i:i+2] in roman:
          
            mylist.append(roman[s[i:i+2]])
            i=i+2
      
          else:
        
            mylist.append(roman[s[i]])
            i=i+1
        return sum(list(mylist))
romanToInt("MCMXCIV")