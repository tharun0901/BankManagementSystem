def anagram(s1,s2):
    if len(s1)!= len(s2):
        print("Anagaram check is not possible")
    else:
        l1=[]
        l2=[]
        for ch in s1:
            l1.append(ch)
        for ch in s2:
            l2.append(ch)
        for i in range(len(s1)):
            found=False
            for j in range(len(s2)):
               if(l1[i]==l2[j]):
                   l2[j]="0"
                   found=True
                   break
            if not found:
                print("it is not a anagram")
                return
    print("It is a anagram number")
        
s1="silenm"
s2="listen"
anagram(s1,s2)