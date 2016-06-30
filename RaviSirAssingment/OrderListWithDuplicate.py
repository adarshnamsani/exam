def sorted_list(lis1,lis2):
    n_lis = lis1+lis2
    curr =0
    curr_in_lis2 = 0
    if len(lis2) != len(lis1):
        print("Circular List")
        return


    while(lis1[curr] != lis2[curr_in_lis2]):
        curr_in_lis2 += 1
    if curr_in_lis2 > len(lis2)-1:
        print("Not Circular list")
        return

    while curr != curr_in_lis2:
        if curr_in_lis2 == len(lis1)-1:
            curr_in_lis2 = 0
        elif curr == len(lis1)-1:
            curr = 0

        elif lis1[curr] == lis2[curr_in_lis2]:
            curr = curr+1
            curr_in_lis2 = curr_in_lis2+1

        else:
            print("Not Circular")


sorted_list([1,2,3],[2,3,0])
