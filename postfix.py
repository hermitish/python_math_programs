ops = {'^': 3, '/': 2, '*': 2, '+': 1, '-': 1}

def push(x, stk):
    stk.append(x)

def pop(stk):
    return stk.pop() if stk != [] else None

def peek(stk):
    return stk[-1]

# in2post(): convert provided infix expression into postfix
def in2post(infix):
    stk = ['(']
    exp = ""
    ch_no = 1
    for ch in infix:
        if ch == '(':
            push(ch, stk)
        elif ch == ')':            
            while peek(stk) != '(' and stk != []:
                exp += pop(stk)
            pop(stk)
        elif ch not in ops:
            exp += ch
        elif ch in ops:
            if stk != [] and peek(stk) == '(':
                push(ch, stk)
            else:
                while (stk != []) and ((peek(stk) != '(') and (ops[peek(stk)] >= ops[ch])):
                    exp += pop(stk)
                push(ch, stk)
        else:
            print("could not parse character in expression: ", ch)        
        print(ch_no, ch, exp, stk, sep='\t')
        ch_no += 1
    while stk != [] and peek(stk) != '(':
        exp += pop(stk)
    return exp


print(in2post("(A+B)-C/D*B)"))
print(in2post("A+(B*C-(D/E^F)*G)*H"))
