#Q. 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻이다. 예를 들어

#()() 또는 (())() 는 올바르다. )()( 또는 (()( 는 올바르지 않다.

#이 때, '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 True 를 반환하고 아니라면 False 를 반환#하시오.

##[0, 0, 2, 2, 4]
##맨뒤부터 없어진다 !!--> 스택


top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights :
        height =heights.pop()
        for idx in range(len(heights)-1,-1,-1) :
            print(idx)
            if heights[idx] > height :
                answer[len(heights)] = idx +1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!