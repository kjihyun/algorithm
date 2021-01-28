#1. 만약 메모에 그 값이 있다면 바로 반환한다.
#2. 피보나치 값을 처음 구했다면 메모에 그 값을 기록한다.
#메모는 fibo_memo 를 사용

input = 50

# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

print(fibo_dynamic_programming(input, memo))