import copy


def detect_copy():
    obj = [[1, 2], [3, 4]]
    copy_obj = copying_machine(obj)
    for i in obj:
        for j in copy_obj:
            if id(i) == id(j):
                return 'shallow copy'
    return 'deep copy'
