input = "abcba"

## solve 1
def is_palindrome(string):
    n= len(string)
    print(n)
    for i in range(n) :
        if string[i] != string[n-1-i] :
            return False
    return True


print(is_palindrome(input))

##solve 2 
## 재귀로 풀기 
def is_palindrome(string):
    print(len(string))
    if string[0] != string[-1] :
        return False
    if len(string) <=1 :
        return True
    return is_palindrome(string[1:-1])
