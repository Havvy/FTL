def extra_lex(stream, target):
    for index, token in enumerate(stream):
        ix = index
        for desired in target:
            if not isinstance(stream[ix], desired):
                break
            ix += 1
        else:
            return index, ix

        #if token is target[ix]:
            #matched[ix] = token
            #ix += 1
