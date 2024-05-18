import random
import time
all_account = {} # 0.이름, 1.비밀번호, 2.잔액
account =[] # 모든 계좌번호
customer_account = 0
def Generate_Random_Numbers():#[기능완성] 계좌번호 생성기

    new_number = random.randint(10000, 99999)  
    if new_number not in account:  
        account.append(new_number)
        return new_number
    else:
        return Generate_Random_Numbers()

def Make_Account(): #[기능완성] 1.1, 1.3번 개인 계좌 개설
    global all_account
    print(all_account)
    customer_name = str(input('이름을 입력하세요: '))
    customer_password = (input('비밀번호를 설정하세요: '))
    print('최초 입금액 10,000원 이상을 입금하세요.')
    first_cost = digit()

    if first_cost >= 10000:
            
        checking_student = str(input("학생이신가요? (y/n) "))
        if checking_student == ('y' or "Y"):      #학생일 경우
            first_cost += 10000 

        accountNumber = Generate_Random_Numbers()
        all_account[accountNumber] = [customer_name,customer_password, first_cost]
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f'            계좌번호: {accountNumber}')
        print(f'            이름: {customer_name}')
        print(f'            비밀번호: {customer_password}')
        print(f'            잔액: {first_cost}')
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    else: 
        print("최초 입금액 10,000원 이상이 필요합니다. 다시 시도하세요.")
    
    input("계속하려면 Enter 키를 누르세요...")
    start()

def Delete_Account(): #[기능완성] 1.2번 개인 계좌 해지
    global all_account
    input_password = input('계좌를 해지려변 비밀번호를 입력하세요: ')
    if all_account[customer_account][1] == input_password:
        del all_account[customer_account]
        print('계좌해지 성공')

        input("계속하려면 Enter 키를 누르세요...")
        lobby()
    else:
        print('비밀번호 틀림')
        input("계속하려면 Enter 키를 누르세요...")
        lobby()    
    

def Check_Account(): #[기능완성] 2번 개인 계좌 확인: 잔액
    print(f'잔액: {all_account[customer_account][2]}')
    input("계속하려면 Enter 키를 누르세요...")
    lobby()

def Deposit_Account(): #[기능완성] 2번 개인 계좌 입금
    global all_account
    print('입금액을 입력하세요: ',end = '')
    cost = digit()
    all_account[customer_account][2] += cost
    print('입금 완료')
    input("계속하려면 Enter 키를 누르세요...")
    lobby()    

def Withdraw_Account(): #[기능완성] 2번 개인 계좌 출금
    global all_account
    print('출금액을 입력사에요: ', end = '')
    cost = digit()
    all_account[customer_account][2] -= cost
    print('출금 완료')
    input("계속하려면 Enter 키를 누르세요...")
    lobby() 

def Make_Corporate_Account(): #[미구현] 3번
    global all_account
    print('기능없음')
    input("계속하려면 Enter 키를 누르세요...")
    lobby()

def Select_Make_Account(): #[분기점][기능완성] 계좌 개설 분기점
    global all_account
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('       1.개인 계좌 개설')
    print('       2.법인 계좌 개설')
    print('       3.돌아가기')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛") 

    bank_work = input()
    if bank_work == '1':
        Make_Account()

    elif bank_work == '2':

        Make_Corporate_Account()
        
    else:
        start()

def Transfer_With_Name(): #[미구현] 이름으로 송금
    global all_account
    print('이체 수수료는 1000원 입니다.')
    receiver_name = input('송금할 이름을 입력해주세요: ')# 송금할 이름 확인
    for key in all_account:
        if all_account[key][0] == receiver_name:
            print('송금할 금액을 정해주세요: ', end ='' )
            money = digit()
            if (all_account[customer_account][2] >= money + 1000): #현재잔액으로 송금할수 있을경우
                all_account[customer_account][2] -= money + 1000
                all_account[key][2] += money

                print('송금 완료')

                input("계속하려면 Enter 키를 누르세요...")
                lobby()
            else:
                print('잔액부족')

                input("계속하려면 Enter 키를 누르세요...")
                lobby()


    print('등록되지 않은 이름 입니다.')        
    input("계속하려면 Enter 키를 누르세요...")
    lobby()

def Transfer_With_Account(): #[미구현] 계좌번호로 송금
    global all_account
    print('송금할 계좌번호를 입력해주세요: ', end= '')
    receiver_account = digit()
    if (all_account.get(receiver_account)):
        print('송금할 금액을 정해주세요: ', end ='' )
        money = digit()
        if (all_account[customer_account][2] >= money + 1000): #현재잔액으로 송금할수 있을경우
            all_account[customer_account][2] -= money + 1000
            all_account[receiver_account][2] += money
            print('송금 완료')

            input("계속하려면 Enter 키를 누르세요...")
            lobby()
        else:
            print('잔액부족')

            input("계속하려면 Enter 키를 누르세요...")
            lobby()
    else:
        print('존재하지않는 계좌번호 입니다')
    input("계속하려면 Enter 키를 누르세요...")
    lobby()

def Transfer_Money(): #[분기점][기능완성] 6번 송금 분기점
    global all_account
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('        1.이름으로 송금')     
    print('        2.계좌로 송금')     
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    
    bank_work = input()
    if bank_work == '1':
        Transfer_With_Name()

    elif bank_work == '2':
        Transfer_With_Account()

    else:
        print('입력오류')
        input("계속하려면 Enter 키를 누르세요...")
        lobby()

def Debug_print_accounts():
    print("계좌 목록:")
    for account_number, name in all_account.items():
        print(f"계좌번호: {account_number}, 이름: {name}")
    
    input("계속하려면 Enter 키를 누르세요...")
    lobby()

def work(bank_work):

    global all_account
    all_account[10000] = ['test', '0000', 0] #여기서 돈을 초기화 하니 주의
    all_account[10001] = ['test2', '0000', 0]
    if bank_work == '1':
        Select_Make_Account()

    elif bank_work == '2':

        Delete_Account()
        
    elif bank_work == '3':
        Check_Account()

    elif bank_work == '4':
        Deposit_Account()

    elif bank_work == '5':
        Withdraw_Account()

    elif bank_work == '6':
        Transfer_Money()

    elif bank_work == '7':
        Deposit_Account()

    elif bank_work == '8':
        Deposit_Account()

    elif bank_work == '9':
        Deposit_Account()

    elif bank_work == '0':
        Debug_print_accounts()
    
    else:
        input("유효하지 않은 입력입니다. \n계속하려면 Enter 키를 누르세요...")
        lobby()

def lobby():
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('       1.계좌 개설\t2.계좌 해지\t3.계좌 확인')
    print('       4.계좌 입금\t5.개좌 출금\t6.계좌 이체')
    print('       7.개좌 개설\t8.개좌 해지\t9.입금')
    print('       0.개발자   \t2.개좌 해지\t3.입금')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print('로비', all_account)
    work(input())

def digit(): # 숫자만을 입력받아 반환하는 함수
    s = input()
    if s.isdigit():
        return int(s)
    else:
        print(',를 제외한 정수만을 입력하세요: ')
        return digit()

def login():
    global customer_account
    print('계좌번호를 입력해주세요.: ', end = '')
    customer_account = digit()
    if (all_account.get(customer_account)): 
        for i in range(5):
            customer_password = input('비밀번호를 입력해주세요: ')
            if all_account[customer_account][1] == customer_password:
                lobby()
            print('비밀번호가 일치하지 않습니다.')
    customer_account = 0
    print('비밀번호 입력을 5회 실패하였습니다.\n5분 후 다시 접속하여 주시길 바랍니다.')
    input("계속하려면 Enter 키를 누르세요...")
    start()

def logout():
    global customer_account
    customer_account = 0
    start()

def start():
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('                1.로그인  2.계좌 개설 ')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    bank_work = input()
    if bank_work == '1':
        login()
    else:
        Select_Make_Account()

start()

# 수정 필요

# 로비에 로그아웃 추가

# 11. 시스템은 지누은행의 관리자(예: 부행장)가 매일 오후 6시 이후 당일 은행 계좌를 가진 전체 고객 수, 개인고객 수, 법인고객 수, 당일의 은행 전체 잔액(잔고), 전체 입출금이 담긴 보고서를 볼 수 있는 서비스를 제공한다. 



# 수정사항

# 10. 시스템은 사용자가 정확하지 않은 값을 입력해도 오류 없이 잘 작동해야 한다. 
# work, make_account, transfer_money, Select_Make_Account함수 수정

# time.sleep(1)
# 은 너무 빠르게 화면이 넘어간다.
# input("계속하려면 Enter 키를 누르세요...")
# 로 변경한다

# def Generate_Random_Numbers
# 겹치는 계좌번호가 만들어졌을 경우 수정

# 8. 시스템은 고객이 제공한 비밀번호가 일치하지 않을 경우, 비밀번호 일치 여부를 5회까지 시도하고, 그래도 비밀번호가 일치하지 않을 경우, 적절한 메시지를 출력하고, 해당 고객이 5분 후 접속할 수 있도록 안내메시지를 제공한다. 
# login 함수 만들고, 다른 함수에 적용

# 금액이 양의 정수일때 작동
# digit 함수 추가

# 이체수수료 1000원
# Transfer_With_Account, Transfer_With_Money 함수 수정

# Delete_Account 수정