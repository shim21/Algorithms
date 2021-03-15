import random

def muliple(data):
    """
    재귀용법을 활용한 1~data까지의 곱을 출력하는 함수
    """
    if data>1:
        return data*muliple(data-1)
    else:
        return data

def sum_list(lst):
    """
    재귀용법을 활용한 리스트의 합을 구하는 함수
    """
    if len(lst)<=1:
        return lst[0]
    else:
        # 리스트의 슬라이싱을 활용할 수 있음
        return lst[0]+sum_list(lst[1:])

def palindrome_mine(string):
    """
    회문인지 아닌지를 판단하는 함수
    내가 짬
    """
    if len(string) <=1 :
        return string[0]
    else:
        return palindrome_mine(string[1:]) + string[-len(string)]

def judge_word(string, palindrome_mine):
    palin = palindrome_mine(string)
    if string == palin:
        return True
    else:
        return False

def palindrome(string):
    """
    회문인지 아닌지를 판단하는 함수
    강의 코드
    """
    if len(string) <=1 :
        return True
    
    # 중간을 기준으로 앞 뒤로 일치하는지 확인하면서 재귀적 용법을 활용
    if string[0] == string[-1]: 
        return palindrome(string[1:-1])
    else:
        return False

def main():
    print(f"1~n까지 재귀용법을 활용한 합 : {muliple(10)}")
    
    data = random.sample(range(100),10)
    string = "LEVEL"
    print(f"랜덤으로 생성된 리스트 : {data}")
    print(f"재귀용법을 활용한 리스트의 합 : {sum_list(data)}")
    print(f"회문 판독기 입력 문자열 : {string}")
    print(f"회문 판독기1 : {judge_word(string, palindrome_mine)}")
    print(f"회문 판독기2 : {palindrome(string)}")

if __name__ == "__main__":
    main()
