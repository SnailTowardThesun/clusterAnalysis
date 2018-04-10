def single_cluster(input_matrix):
    #    ret = [
    #        [1, 2, 3, 4, 5],
    #        [4, 7, 9, 11],
    #        [6, 8]
    #    ]
    ret = []
    ret_dic = {}
    group_dic = {}
    group_num = 0

    # do simple linkage
    for i in input_matrix:
        if len(ret_dic) == 0:
            ret_dic[group_num] = i
            for j in i:
                group_dic[j] = group_num
            group_num += 1
            continue

        is_linked = False
        for j in i:
            key = group_dic.get(j)
            if key is not None:
                for k in i:
                    ret_dic[key].append(k)
                is_linked = True
                break
        if is_linked is not True:
            ret_dic[group_num] = i
            group_num += 1

    # remove the repeat element
    for key, value in ret_dic.items():
        tmp = []
        for v in value:
            if v not in tmp:
                tmp.append(v)
        ret.append(tmp)

    return ret
