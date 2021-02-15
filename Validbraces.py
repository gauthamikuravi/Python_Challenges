def validBraces(s):
    while '{}' in s or '()' in s or '[]' in s:
        s=s.replace('{}','').replace('[]','').replace('()','')
    return s==''
if __name__ == '__main__':

    print('Enter your braces ')
    s = input()
    valid_braces = validBraces(s)
    print(valid_braces)