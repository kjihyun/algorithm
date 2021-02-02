input = 20


def find_prime_list_under_number(number):
    prime_list=[]
    for i in range(2, number + 1):  ## 2~20
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list


result = find_prime_list_under_number(input)
print(result)