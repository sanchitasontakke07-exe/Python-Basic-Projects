text=input("Enter a String :")
count = 0
for ch in text :
    if ch in "aeiouAEIOU" :
        count += 1
print("Total vowels :",count)