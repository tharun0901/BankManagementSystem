def non_repeat(s):
 count=0
 for i in range(len(s)):
  for j in range(len(s)):
   if s[i]==s[j]:
    return -1
   else:
    count+=1
 return count
  


 
    



print(non_repeat("leetcode"))
