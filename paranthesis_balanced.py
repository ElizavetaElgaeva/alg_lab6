    
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from stack import Stack, StackOverflowError, StackIsEmptyError

d = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}

def is_paranthesis_balanced(s):
    
    if (len(s) == 0):
        return(True)
    
    elif (len(s)%2 != 0):
        return(False)
        
    else:
        stack = Stack(len(s))
        stack.push(s[0])
        for i in range(1, len(s)):
            if (d.get(stack.peek()) == s[i]):
                stack.pop()
            else:
                stack.push(s[i])
        if (len(stack) == 0):
            return(True)
        else:
            return(False)
            
    pass