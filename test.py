print(' ━ ┃ ┏ ┓ ┛ ┗ ┣ ┳ ┫ ┻ ╋')

print('로컬에서 2번줄 수정')

print("┏━━━━━━━━━━━━━━━━━━━┓")
print("┃                   ┃")
print("┃   출금액: nnnn원   ┃")
print("┃                   ┃")
print("┃   남은돈: nnnn원   ┃")
print("┃                   ┃")
print("┗━━━━━━━━━━━━━━━━━━━┛")
money = 10000
print("┏━━━━━━━━━━━━━━━━━━━┓")
print("                     ")
print(f"   출금액: {money}원               ")
print("                     ")
print(f"   잔액: {money}원                ")
print("                     ")
print("┗━━━━━━━━━━━━━━━━━━━┛")
test = f"\x1b[32m       [입금] {money}원\x1b[0m"
print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print('            1.이름으로 송금')
# print('            [입금] 00000 nnnnnn원')
# print('            [출금] 00000 nnnnnn원')
# print('       [이체] 00000 to 00001 nnnnnn원')
print('\x1b[32m' + '       [이체] 00000 to 00001 nnnnnn원' + '\x1b[0m')
print('\x1b[31m' + '            [출금] 00000 nnnnnn원' + '\x1b[0m')
print('\x1b[31m' + '            [출금] 00000 nnnnnn원' + '\x1b[0m')
print('\x1b[36m' + '            [입금] 00000 nnnnnn원' + '\x1b[0m')
print('\x1b[32m' + '       [이체] 00000 to 00001 nnnnnn원' + '\x1b[0m')
print('\x1b[31m' + '            [출금] 00000 nnnnnn원' + '\x1b[0m')
print('\x1b[32m' + '       [이체] 00000 to 00001 nnnnnn원' + '\x1b[0m')
print('\x1b[31m' + '            [출금] 00000 nnnnnn원' + '\x1b[0m')
print('\x1b[31m' + '            [출금] 00000 nnnnnn원' + '\x1b[0m')
print('\x1b[32m' + '       [이체] 00000 to 00001 nnnnnn원' + '\x1b[0m')
print(test)
# print('\x1b[31m' + '        2.안녕' + '\x1b[0m')
# print('\x1b[31m' + '        2.안녕' + '\x1b[0m')
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")    
accounts = {}  # 계좌 정보를 저장할 딕셔너리

my_dict = {
    1: ["John", "password1"],
    2: ["Alice", "password2"],
    3: ["Bob", "password3"]
}

result_list = []
def add(a, b):
    """
    두 숫자의 합을 반환하는 함수.

    Args:
        a (int, float): 첫 번째 숫자.
        b (int, float): 두 번째 숫자.

    Returns:
        int, float: 입력된 두 숫자의 합.
    """
    return a + b
# # 딕셔너리의 값을 하나씩 직접 비교
# for item in my_dict:
#     print(item)

# # 딕셔너리를 0번부터 끝까지 비교
# for i in my_dict.items():
#     print(i)

# # 딕셔너리 -> 리스트 
# for key, value in my_dict.items():
#     result_list.append([key] + value)

# print(result_list)

# list_length = len(result_list)

# for i in range(list_length):
#     print(result_list[i][0])

if (my_dict.get(1)):
    print(my_dict.get(1))