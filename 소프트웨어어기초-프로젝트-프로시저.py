##임시
while True:
    print("-----------------------------------------------------------------")
    print('1.개좌 개설\t2.개좌 해지\t3.입금')
    bank_work = int(input())

    all_account = {}
    ## 1눌렀을 때
    ### 1-1
    if bank_work == 1:
        try:
            customer_name = str(input('이름을 입력하세요.:'))
            customer_password = (input('비밀번호를 설정하세요.:'))
            first_cost = int(input('최초 입금액 10,000원 이상을 입금하세요.(,를 제외한 정수만 입력하세오.):'))
        except:
            print('형식이 올바르지 않습니다. 다시 시도하세요.')
            continue
        if first_cost >= 10000:
            print("학생이신가요? (y/n)")
            checking_student = str(input())
            if checking_student == ('y' or "Y"):      #학생일 경우
                first_cost += 10000
                print(first_cost) #임시 출력
                all_account['계좌번호'] = [customer_name,customer_password, first_cost]
                print(all_account)      ####---------------------(확인용 출력)
            elif checking_student == ('n' or 'N'):        #아닐 경우 그냥 진행 
                print('학생X')
                print(first_cost)
                all_account['계좌번호'] = [customer_name,customer_password, first_cost]
                print(all_account)      ####---------------------(확인용 출력)
                continue
            else:
                continue
        else: 
            print("최초 입금액 10,000원 이상이 필요합니다. 다시 시도하세요.")
            continue
            
    #2눌렀을 때
    ## 1-2 
    elif bank_work == 2:
        if 
            print('똥')
    else:
        pass

