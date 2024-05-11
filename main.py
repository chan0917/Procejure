import random
import time
all_account = {}
account =[]

def Generate_Random_Numbers():

    new_number = random.randint(10000, 99999)  
    if new_number not in account:  
        account.append(new_number)
        return new_number

def Make_Account(): #1.1, 1.3번 개인 계좌 개설
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

def Delete_Account(): #1.2번 개인 계좌 확인
    global all_account
    customer_name = str(input('해지할 계좌의 이름을 입력하세요: '))

    valueList = []
    for key, value in all_account.items():
        valueList.append([key] + value) #[계좌번호, 이름, 비밀번호, 잔액]

    list_length = len(valueList)

    for i in range(list_length): # 리스트 길이만큼 반복 
        if (customer_name == valueList[i][1]): #1번째 리스트의 이름과 일치하면
            customer_password = (input('비밀번호를 입력하세요: '))   
            if (customer_password == valueList[i][2]):
                del all_account[valueList[i][0]]
                print('계좌해지 성공')
            else:
                print('비밀번호 틀림')
        else:
            print('해당하는 이름의 계좌가 없습니다 처음부터 다시 시작해 주세요')        
    
    time.sleep(1)
    lobby()

def Check_Account(): #[미구현] 2번 개인 계좌 확인
    global all_account

    time.sleep(1)
    lobby()

def Make_CorporateAccount(): #[미구현] 3번
    global all_account

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
    if bank_work == 1:
        Make_Account()

    elif bank_work == 2:
        all_account[10000] = ['test', '0000', 10000]
        Delete_Account()

    elif bank_work == 0:
        Debug_print_accounts()



def lobby():
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print('       1.개좌 개설\t2.개좌 해지\t3.입금           ')
    print('       4.개좌 개설\t5.개좌 해지\t6.입금           ')
    print('       7.개좌 개설\t8.개좌 해지\t9.입금           ')
    print('       0.개발자 \t 2.개좌 해지\t3.입금           ')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print(all_account)
    work(int(input()))


lobby()



