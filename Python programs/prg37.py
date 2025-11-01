def count_letters(str):
    count={} #name of dictionary
    for ch in str:
        if ch in count:
            count[ch]+=1
        else:
            count[ch]=1
    return count
st=input("Enter a string of your choice:")
print("Occurence of each character is as follows:-")
print(count_letters(st))