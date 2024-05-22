import random
import time
all_account = {} # 0.이름, 1.비밀번호, 2.잔액, 3.법인 대표, 4.담당직원
account =[] # 모든 계좌번호
customer_account = 0 #로그인 한뒤에 쓸 계좌번호
bank_log = [] # 돈이 이동하는 기록들을 저장 

def Generate_Random_Numbers():#[완료] 계좌번호 생성기
    new_number = random.randint(10000, 99999)  
    if new_number not in account:  
        account.append(new_number)
        return new_number
    else:
        return Generate_Random_Numbers()
    
def Generate_Log(work, account, money, other_account = ''): #[완료] 로그생성
    """
    로그를 생성하는 함수\n
    자기 계좌, 금액, 다른사람 계좌\n
    Work Input:
        1: [입금]로그 생성.
        2: [출금]로그 생성.
        3: [이체]로그 생성.
    """
    global bank_log
    if work == 1:
        deposit_string = f"\x1b[36m       [입금] {account} {money}원\x1b[0m"
        bank_log.append(deposit_string)

    elif work == 2:
        deposit_string = f"\x1b[31m       [출금] {account} {money}원\x1b[0m"
        bank_log.append(deposit_string)
        
    elif work == 3:
        deposit_string = f"\x1b[32m       [이체] {account} to {other_account} {money}\x1b[0m"
        bank_log.append(deposit_string)

def Make_Account(): #[완료] 1.1, 1.3번 개인 계좌 개설
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
        all_account[accountNumber] = [customer_name,customer_password, first_cost, '개인계좌', '개인계좌']
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

def Delete_Account(): #[완료] 1.2번 개인 계좌 해지
    global all_account
    input_password = input('계좌를 해지려변 비밀번호를 입력하세요: ')

    if all_account[customer_account][1] == input_password:

        if all_account[customer_account][3] != '개인계좌': #법인계좌인 겨우 3번과 4번비교
            input_master_name = input('계좌 대표자의 이름을 입력하세요: ')
            input_administer_name = input('담당직원의 이름을 입력하세요: ')

            if all_account[customer_account][3] == input_master_name and all_account[customer_account][4] == input_administer_name:
                del all_account[customer_account]
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(f'           계좌가 해지되었습니다          ')
                print(f'          처음 화면으로 돌아갑니다          ')
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

                input("계속하려면 Enter 키를 누르세요...")
                start()
            else:
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(f'           비밀번호가 틀렸습니다          ')
                print(f'            다시 시도해 주십시오         ')
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

                input("계속하려면 Enter 키를 누르세요...")
                lobby()
        else:    #일반계좌이니 그냥 진행
            del all_account[customer_account]
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(f'           계좌가 해지되었습니다          ')
            print(f'          처음 화면으로 돌아갑니다          ')
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
            print('')

            input("계속하려면 Enter 키를 누르세요...")
            lobby()
    else:
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f'           비밀번호가 틀렸습니다          ')
        print(f'            다시 시도해 주십시오         ')
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

        input("계속하려면 Enter 키를 누르세요...")
        start()    
    
def Check_Account(): #[완료] 2번 개인 계좌 확인: 잔액
    print(f'잔액: {all_account[customer_account][2]}')
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f'           이름: {all_account[customer_account][0]}          ')
    print(f'           계좌번호: {customer_account}          ')
    print(f'           잔액: {all_account[customer_account][2]}         ')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    input("계속하려면 Enter 키를 누르세요...")
    lobby()

def Deposit_Account(): #[완료] 2번 개인 계좌 입금
    global all_account
    print('입금액을 입력하세요: ',end = '')
    cost = digit()
    all_account[customer_account][2] += cost
    Generate_Log(1, customer_account, cost)
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f'      입금이 성공적으로 완료되었습니다      ')
    print(f'           입금액: {cost}          ')
    print(f'           잔액: {all_account[customer_account][2]}         ')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    input("계속하려면 Enter 키를 누르세요...")
    lobby()    

def Withdraw_Account(): #[완료] 2번 개인 계좌 출금
    global all_account
    print('출금액을 입력사에요: ', end = '')
    cost = digit()
    if (all_account[customer_account][2] >= cost):

        all_account[customer_account][2] -= cost
        Generate_Log(2, customer_account, cost)
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f'      출금이 성공적으로 완료되었습니다      ')
        print(f'           입금액: {cost}          ')
        print(f'           잔액: {all_account[customer_account][2]}         ')
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    else:
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f'           출금에 실패하였습니다           ')
        print(f'                잔액부족          ')
        print(f'           잔액: {all_account[customer_account][2]}         ')
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    input("계속하려면 Enter 키를 누르세요...")
    lobby() 

def Make_Corporate_Account(): #[완료] 3번
    global all_account
    customer_name = str(input('이름을 입력하세요: '))
    customer_password = (input('비밀번호를 설정하세요: '))
    master_name = (input('대표자 이름을 입력하세요: '))
    administer_name = (input('담당직원 이름을 입력하세요: '))
    print('최초 입금액 10,000원 이상을 입금하세요.')
    first_cost = digit()

    if first_cost >= 10000:

        first_cost += 100000 

        accountNumber = Generate_Random_Numbers()
        all_account[accountNumber] = [customer_name,customer_password, first_cost, master_name, administer_name]
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f'            계좌번호: {accountNumber}')
        print(f'            이름: {customer_name}')
        print(f'            법인 대표 이름: {master_name}')
        print(f'            관리자 이름: {administer_name}')
        print(f'            비밀번호: {customer_password}')
        print(f'            잔액: {first_cost}')
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    else: 
        print("최초 입금액 10,000원 이상이 필요합니다. 다시 시도하세요.")
    
    input("계속하려면 Enter 키를 누르세요...")
    start()

def Select_Make_Account(): #[분기점][완료] 계좌 개설 분기점
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
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print('            오류')     
        print('   유효하지 않은 입력입니다.')     
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        input("계속하려면 Enter 키를 누르세요...")

        start()

def Transfer_With_Name(): #[완료] 이름으로 송금
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
                Generate_Log(3, customer_account, money, key)
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(f'      송금이 성공적으로 완료되었습니다      ')
                print(f'           입금액: {money}          ')
                print(f'           잔액: {all_account[customer_account][2]}         ')
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

                input("계속하려면 Enter 키를 누르세요...")
                lobby()
            else:
                print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
                print(f'           송금에 실패하였습니다           ')
                print(f'                잔액부족          ')
                print(f'           잔액: {all_account[customer_account][2]}         ')
                print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

                input("계속하려면 Enter 키를 누르세요...")
                lobby()


    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f'           송금에 실패하였습니다           ')
    print(f'            등록되지 않은 이름          ')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")       
    input("계속하려면 Enter 키를 누르세요...")
    lobby()

def Transfer_With_Account(): #[완료] 계좌번호로 송금
    global all_account
    print('송금할 계좌번호를 입력해주세요: ', end= '')
    receiver_account = digit()
    if (all_account.get(receiver_account)):
        print('송금할 금액을 정해주세요: ', end ='' )
        money = digit()
        if (all_account[customer_account][2] >= money + 1000): #현재잔액으로 송금할수 있을경우
            all_account[customer_account][2] -= money + 1000
            all_account[receiver_account][2] += money
            Generate_Log(3, customer_account, money, receiver_account)
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(f'      송금이 성공적으로 완료되었습니다      ')
            print(f'           입금액: {money}          ')
            print(f'           잔액: {all_account[customer_account][2]}         ')
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

            input("계속하려면 Enter 키를 누르세요...")
            lobby()
        else:
            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print(f'           송금에 실패하였습니다           ')
            print(f'                잔액부족          ')
            print(f'           잔액: {all_account[customer_account][2]}         ')
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

            input("계속하려면 Enter 키를 누르세요...")
            lobby()
    else:
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print(f'           송금에 실패하였습니다           ')
        print(f'         존재하지않는 계좌번호 입니다          ')
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")    

    input("계속하려면 Enter 키를 누르세요...")
    lobby()

def Transfer_Money(): #[분기점][완료] 6번 송금 분기점
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
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print('            오류')     
        print('   유효하지 않은 입력입니다.')     
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        input("계속하려면 Enter 키를 누르세요...")
        lobby()

def Administor_Manage(): # 관리자 모드 마완
    global all_account
    global bank_log
    # 적당히 비밀번호 입력 
    print('은행 정산을 시작합니다.')     
    print(bank_log)
    bank_accounts = len(all_account)
    idle_customer = 0
    corporate_customer = 0
    bank_money = 0

    for account_number, info in all_account.items():
        name, password, money, master, admin = info
        bank_money += money
        if master != '개인계좌':
            idle_customer += 1
        else:
            corporate_customer += 1
    
    for item in bank_log:
        print(item)
    print(bank_accounts, idle_customer, corporate_customer, bank_money)
    input("계속하려면 Enter 키를 누르세요...")
    lobby()

def work(bank_work): # lobby분기점[완료]
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

    elif bank_work == '0':
        logout()
        start()
    
    else:
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print('            오류')     
        print('   유효하지 않은 입력입니다.')     
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        input("계속하려면 Enter 키를 누르세요...")
        lobby()

def lobby(): #[완료]
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("            지누 은행에 오신것을 환영합니다 ")
    print("            원하시는 서비스를 선택해 주세요. ")
    print("")
    print('       1.계좌 개설\t2.계좌 해지\t3.계좌 확인')
    print('       4.계좌 입금\t5.개좌 출금\t6.계좌 이체')    
    print("")
    print("                                        0.로그아웃")
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

def login(): #[완료]
    global customer_account
    print('계좌번호를 입력해주세요.: ', end = '')
    customer_account = digit()
    if (all_account.get(customer_account)): 
        for i in range(5):
            customer_password = input('비밀번호를 입력해주세요: ')
            if all_account[customer_account][1] == customer_password:
                lobby()

            print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
            print('            오류')     
            print('비밀번호가 일치하지 않습니다.')   
            print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
        customer_account = 0
        print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print('    비밀번호 입력을 5회 실패하였습니다.')     
        print('   5분 후 다시 접속하여 주시길 바랍니다.')   
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

        input("계속하려면 Enter 키를 누르세요...")
        start()
    customer_account = 0
    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print(f'        등록되지 않은 계좌번호입니다.           ')
    print(f'             다시 시도하세요       ')
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")    
    input("계속하려면 Enter 키를 누르세요...")
    start()

def logout(): #[완료]
    global customer_account
    customer_account = 0
    start()

def start(): #[완료]
    global all_account
    all_account[10000] = ['test', '0000', 0, '개인계좌', '개인계좌'] #여기서 돈을 초기화 하니 디버깅시 주의
    all_account[10001] = ['test2', '0000', 0, 'EAE', 'U']

    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("            지누 은행에 오신것을 환영합니다 ")
    print("            원하시는 서비스를 선택해 주세요. ")
    print("")
    print('       1.로그인   \t2.계좌 개설\t3.관리자 모드')  
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    bank_work = input()
    if bank_work == '1':
        login()
    elif bank_work == '2':
        Select_Make_Account()
    else:
        Administor_Manage()

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

# 법인모드 만들어서 로그인이나 계좌생성에 차별점을 준뒤에 법인모드일경우 계좌해지만 다르게 하면될듯 4번과 5번이 비어있는게 아니면 법인이니 더 입력해라고 하기?
