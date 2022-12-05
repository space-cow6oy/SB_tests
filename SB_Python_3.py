def integerPartition(num):


    num = num + 1


    pM = [ [0] * num for x in range(num) ]


    for sum_inx in range(0, num):
        pM[sum_inx][0] = 1


    for sum_inx in range(1, num):
        for num_inx in range(1, num):
            
            if sum_inx > num_inx:


                pM[sum_inx][num_inx] = pM[sum_inx - 1][num_inx]

            else:

                combos_without_summand = pM[sum_inx - 1][num_inx]


                combos_with_summand = pM[sum_inx][num_inx - sum_inx]

                pM[sum_inx][num_inx] = combos_without_summand + combos_with_summand


    num = num - 1


    return pM[num][num]





