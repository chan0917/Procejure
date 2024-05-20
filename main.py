import random
import time
all_account = {} # 0.이름, 1.비밀번호, 2.잔액
account =[] # 모든 계좌번호

def Generate_Random_Numbers():#[기능완성] 계좌번호 생성기

    new_number = random.randint(10000, 99999)  
    if new_number not in account:  
        account.append(new_number)
        return new_number

def Make_Account(): #[기능완성] 1.1, 1.3번 개인 계좌 개설
    global all_account
    print(all_account)
    customer_name = str(input('이름을 입력하세요: '))
    customer_password = (input('비밀번호를 설정하세요: '))
    first_cost = int(input('최초 입금액 10,000원 이상을 입금하세요(,를 제외한 정수만 입력하세오): '))

    if first_cost >= 10000:
            
        checking_student = str(input("학생이신가요? (y/n) "))
        if checking_student == ('y' or "Y"):      #학생일 경우
                first_cost += 10000
        else:
                print('입력오류') 

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
    
    time.sleep(1)
    lobby()

def Delete_Account(): #[기능완성] 1.2번 개인 계좌 해지
    global all_account
    customer_name = str(input('해지할 계좌의 이름을 입력하세요: '))

    valueList = []
    for key, value in all_account.items():
        valueList.append([key] + value) #[계좌번호, 이름, 비밀번호, 잔액]

    list_length = len(valueList)

    for i in range(list_length): # 리스트 길이만큼 반복 
        if (customer_name == valueList[i][1]): #리스트의 1번째 변수인 이름과 일치하면
            customer_password = (input('비밀번호를 입력하세요: '))   
            if (customer_password == valueList[i][2]):
                del all_account[valueList[i][0]]
                print('계좌해지 성공')

                time.sleep(1)
                lobby()
            else:
                print('비밀번호 틀림')

                time.sleep(1)
                lobby()
        
    print('해당하는 이름의 계좌가 없습니다 처음부터 다시 시작해 주세요')# 이름찾기 if문이 다 끝나면 자동 탈출        
    
    time.sleep(1)
    lobby()

def Check_Account(): #[기능완성] 2번 개인 계좌 확인: 잔액
    global all_account

    customer_account = int(input('계좌번호를 입력해주세요: '))
    if(all_account.get(customer_account)):
        customer_info = all_account.get(customer_account)
        print(f'계좌번호: {customer_account}')
        print(f'잔액: { customer_info[2]}')
    else:
        print('존재하지않는 계좌번호 입니다')

    time.sleep(1)
    lobby()

def Deposit_Account(): #[기능완성] 2번 개인 계좌 입금
    global all_account

    customer_account = int(input('계좌번호를 입력해주세요: '))
    if(all_account.get(customer_account)):
        customer_info = all_account.get(customer_account)
        cost = int(input('입금액을 입력하세요(,를 제외한 정수만 입력하세오): '))
        customer_info[2] += cost
        
        all_account[customer_account] = customer_info
        print('입금 완료')
    else:
        print('존재하지않는 계좌번호 입니다')

    time.sleep(1)
    lobby()    

def Withdraw_Account(): #[기능완성] 2번 개인 계좌 출금
    global all_account

    customer_account = int(input('계좌번호를 입력해주세요: '))
    if(all_account.get(customer_account)):
        customer_info = all_account.get(customer_account)
        cost = int(input('출금액을 입력하세요(,를 제외한 정수만 입력하세오): '))
        customer_info[2] -= cost
        
        all_account[customer_account] = customer_info
        print('출금 완료')
    else:
        print('존재하지않는 계좌번호 입니다')

    time.sleep(1)
    lobby() 

def Make_Corporate_Account(): #[미구현] 3번
    global all_account
    print('기능없음')
    time.sleep(1)
    lobby()

def Select_Make_Account(): #[분기점][기능완성] 계좌 개설 분기점
    global all_account
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('       1.개인 계좌 개설')
    print('       2.법인 계좌 개설')
    print('       3.돌아가기')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛") 

    bank_work = int(input())
    if bank_work == 1:
        Make_Account()

    elif bank_work == 2:

        Make_Corporate_Account()
        
    elif bank_work == 3:
        lobby()

def Transfer_With_Name(): #[미구현] 이름으로 송금
    global all_account

    customer_account = int(input('계좌번호를 입력해주세요: ')) # 내 계좌번호 확인
    if (all_account.get(customer_account)):
        customer_info = all_account.get(customer_account)

        receiver_name = str(input('송금할 이름을 입력해주세요: '))# 송금할 계좌번호 확인

        valueList = []
        for key, value in all_account.items():
            valueList.append([key] + value) #[계좌번호, 이름, 비밀번호, 잔액]
        list_length = len(valueList)

        for i in range(list_length):
            if (receiver_name == valueList[i][1]):
                money = int(input('송금할 금액을 정해주세요(,를 제외한 정수만 입력하세오): '))
                if (customer_info[2] >= money): #현재잔액으로 송금할수 있을경우
                    customer_info[2] -= money
                    valueList[i][3] += money

                    all_account[customer_account] = customer_info
                    all_account[valueList[i][0]] = [valueList[i][1], valueList[i][2], valueList[i][3]]
                    print('송금 완료')

                    time.sleep(1)
                    lobby()
                else:
                    print('잔액부족')

                    time.sleep(1)
                    lobby()
            
        print('해당하는 이름의 계좌가 없습니다 처음부터 다시 시작해 주세요')# 이름찾기 if문이 다 끝나면 자동 탈출        
    else:
        print('존재하지않는 계좌번호 입니다')

    time.sleep(1)
    lobby()

def Transfer_With_Account(): #[미구현] 계좌번호로 송금
    global all_account

    customer_account = int(input('계좌번호를 입력해주세요: ')) # 내 계좌번호 확인
    if (all_account.get(customer_account)):
        customer_info = all_account.get(customer_account)

        receiver_account = int(input('송금할 계좌번호를 입력해주세요: '))# 송금할 계좌번호 확인
        if (all_account.get(receiver_account)):
            receiver_info = all_account.get(receiver_account)
            #이제 송금 시작
            money = int(input('송금할 금액을 정해주세요(,를 제외한 정수만 입력하세오): '))
            if (customer_info[2] >= money): #현재잔액으로 송금할수 있을경우
                customer_info[2] -= money
                receiver_info[2] += money

                all_account[customer_account] = customer_info
                all_account[receiver_account] = receiver_info
                print('송금 완료')
            else:
                print('잔액이 부족합니다')
        else:
            print('존재하지않는 계좌번호 입니다')
    else:
        print('존재하지않는 계좌번호 입니다')

    time.sleep(1)
    lobby()

def Transfer_Money(): #[분기점][기능완성] 6번 송금 분기점
    global all_account
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('        1.이름으로 송금')     
    print('        2.계좌로 송금')     
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    
    bank_work = int(input())
    if bank_work == 1:
        Transfer_With_Name()

    elif bank_work == 2:
        Transfer_With_Account()

    else:
        print('입력오류')
        time.sleep(1)
        lobby()

def Debug_print_accounts():
    print("계좌 목록:")
    for account_number, name in all_account.items():
        print(f"계좌번호: {account_number}, 이름: {name}")
    
    time.sleep(1)
    lobby()

def work(bank_work):

    global all_account
    all_account[10000] = ['test', '0000', 0] #여기서 돈을 초기화 하니 주의
    all_account[10001] = ['test2', '0000', 0]
    if bank_work == 1:
        Select_Make_Account()

    elif bank_work == 2:

        Delete_Account()
        
    elif bank_work == 3:
        Check_Account()

    elif bank_work == 4:
        Deposit_Account()

    elif bank_work == 5:
        Withdraw_Account()

    elif bank_work == 6:
        Transfer_Money()

    elif bank_work == 7:
        Deposit_Account()

    elif bank_work == 8:
        Deposit_Account()

    elif bank_work == 9:
        Deposit_Account()

    elif bank_work == 0:
        Debug_print_accounts()

def lobby():
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('       1.계좌 개설\t2.계좌 해지\t3.계좌 확인')
    print('       4.계좌 입금\t5.개좌 출금\t6.계좌 이체')
    print('       7.개좌 개설\t8.개좌 해지\t9.입금')
    print('       0.개발자   \t2.개좌 해지\t3.입금')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print('DEBUG로비', all_account)
    work(int(input()))


lobby()



