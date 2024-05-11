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

print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
print('        1.이름으로 송금')
print('        1.이름으로 송금')
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")    
accounts = {}  # 계좌 정보를 저장할 딕셔너리

my_dict = {
    1: ["John", "password1"],
    2: ["Alice", "password2"],
    3: ["Bob", "password3"]
}

result_list = []

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