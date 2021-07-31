# time complexity O(n)
def is_brackets(string):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for c in string:
        if c in brackets.keys():
            stack.append(c)
        # stacks use  LIFO - Last In First Out - brackets.get(stack[-1])
        elif len(stack) > 0 and brackets.get(stack[-1]) == c:
            #print(brackets.get(stack[-1]))
            stack.pop()
        else:
            return False

    return stack == []

print(is_brackets("{[]}")) # true
print(is_brackets("{(])}"))
print(is_brackets("{[(]}"))
print(is_brackets("{[()]}")) # true
print(is_brackets("{[}]}"))
print(is_brackets("{[{}]}")) # true
