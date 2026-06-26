def analyze_str(s):
    if s =="":
        print("Empty String")
        return
    print("Length :",len(s))
    print("Reverse :",s[::-1])
    vowels = 0
    for ch in s:
        if ch.lower() in "aeiouAEIOU":
                vowels += 1
    print("Total vowels :",vowels)
    for i in range(len(s)):
        print(s[i],"Positive:",i,"Neative",i-len(s))
text=input("Enter a String :")
analyze_str(text)