def mergeSort(input_list: list[int]):

    if len(input_list) == 1:

        return input_list

    mid_point: int = len(input_list) // 2

    input_list_sx: list[int] = mergeSort(input_list = input_list[:mid_point])
    input_list_dx: list[int] =mergeSort(input_list = input_list[mid_point:])

    return merge(input_list_sx, input_list_dx)


def merge(input_list_sx: list[int], input_list_dx: list[int]):

    i: int = 0
    j: int = 0

    merge_list: list[int] = [None for _ in range(len(input_list_sx + input_list_dx))]

    for k in range(len(merge_list)):

        if (input_list_sx[i] == None):

            merge_list[k] = input_list_dx[j]
            input_list_dx[j] = None


            if j+1 < len(input_list_dx):
                j += 1

        elif (input_list_dx[j] == None):

            merge_list[k] = input_list_sx[i]
            input_list_sx[i] = None


            if i+1 < len(input_list_sx):
                i += 1

        elif(input_list_sx[i] > input_list_dx[j]):

            merge_list[k] = input_list_dx[j]
            input_list_dx[j] = None


            if j+1 < len(input_list_dx):
                j += 1
        
        else:

            merge_list[k] = input_list_sx[i]
            input_list_sx[i] = None


            if i+1 < len(input_list_sx):
                i += 1

    return merge_list


if __name__ == '__main__':

    lista: list[int] = [31,52,856,314,22,13]
    #lista: list[int] = [0,1,2,3,4,5,6,7]

    print(mergeSort(lista))


