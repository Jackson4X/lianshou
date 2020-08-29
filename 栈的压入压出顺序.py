def validateStackSequences(pushed, popped):
    """
    :type pushed: List[int]
    :type popped: List[int]
    :rtype: bool
    """
    if (len(pushed) != len(popped)):
        return False
    if (len(pushed) == 0 and len(popped) == 0):
        return True
    for idx_o in range(len(popped) - 2):
        if (len(pushed) == 0):
            return True
        idx_u = pushed.index(popped[idx_o])
        if idx_u == 0:
            pushed.remove(pushed[idx_u])
            continue
        elif (popped[idx_o + 1] == pushed[idx_u - 1] or popped[idx_o + 1] in pushed[idx_u + 1:]):
            pushed.remove(pushed[idx_u])
            continue

        else:
            return False
    return True


pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print(validateStackSequences(pushed, popped))