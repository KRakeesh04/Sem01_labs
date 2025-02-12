def tail(text :str) :
    text = text[1:]
    return text

def head(text :str) :
    return text[0]

def lev(text01,text02) :
    if len(text02) == 0 :
        count = len(text01)
        return count
    elif len(text01) == 0 :
        count = len(text02)
        return count
    elif head(text01) == head(text02) :
        count = lev(tail(text01),tail(text02))
        return count
    else :
        count = 1 + min( lev(tail(text01), text02), lev(text01, tail(text02)), lev(tail(text01), tail(text02)) )
        return count




msg = input("Enter Input: ").split()
distance = lev(msg[0], msg[1])
print(distance)
    