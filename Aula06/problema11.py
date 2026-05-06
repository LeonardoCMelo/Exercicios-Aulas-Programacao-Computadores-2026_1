def has_duplicates(s_splitted:list):
    for s in s_splitted:
        if s_splitted.count(s)>1:
            return True
    return False
