def visiting_tree_iterative(tree: dict[int, list[int]], root: int):

    media_livelli: dict = {}
    livello: int = 0
    contenitore: float = 0
    count: float = 0
    stack: list[int] = [root]
    while stack: # while len(stack) != 0

        curr_node = stack.pop(0)
        livello += 1

        if curr_node:

            print(curr_node)
            left_child, right_child =\
                tree[curr_node]
            
            if left_child:

                stack.append(left_child)
                contenitore += left_child
                count += 1

            if right_child:

                stack.append(right_child)
                contenitore += left_child
                count += 1
        

        media: float = (contenitore)/count

        contenitore = 0
        count = 0

        media_livelli[livello] = media
            

    return media_livelli

tree: dict = {1: [2,3], 2: [4,5], 3: [None,None], 4: [None,None], 5: [None,None]}

media_livelli: dict = visiting_tree_iterative(tree, 1)

print(media_livelli)


"""
def visiting_tree_iterative(tree: dict[int, list[int]], root: int):
    stack: list[int] = [root]
    while stack: # while len(stack) != 0
        curr_node = stack.pop(0)
        if curr_node:
            print(curr_node)
            left_child, right_child =\
                tree[curr_node]
            if left_child:
                stack.append(left_child)
            if right_child:
                stack.append(right_child)
"""