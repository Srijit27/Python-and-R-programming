def sum(lst):
    even_p=[lst[i] for i in range(1,len(lst),2)]
    odd_p=[lst[i] for i in range (0,len(lst),2)]
    print("Even position elements are:",even_p)
    print("Odd position elements are:",odd_p)
    even_p_sort=sorted(even_p)
    odd_p_sort=sorted(odd_p)
    if len(even_p_sort)<2 or len(odd_p_sort)<2:
        print("Enter more elements..!!")
        return None
    sec_lar=even_p_sort[-2]
    sec_sma=odd_p_sort[1]
    return sec_lar+sec_sma

Lst=[10,5,4,1,8,9,7,6,3,2]
result=sum(Lst)
if result is not None:
    print("The sum is:",result)