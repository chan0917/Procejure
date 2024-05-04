##임시
while True:
    print("-----------------------------------------------------------------")
    print('1번')



    #####
    class BankServer:  # 1번 조건 객체, 1.1 개인고객이 본인 계좌의 개설에 필요한 정보는 '고객이름, 비밀번호, 최초 입금액' 이다. 
        def __init__(self, name=None, password=None, price=None, age=None):
            if (name is not None and password is not None and price is not None) or age is not None:
                self.server = {
                    'name': str(name),
                    'password': password,
                    'price': int(price),#(수정사항) 최초 입금액 10000원 이상
                }
                if age is not None:
                    self.server['age'] = int(age)
            else:
                print("이름 또는 비밀번호 또는 최초 입금액이 입력 되지 않았습니다.")
            #(수정사항) 계좌번호 만들기

        def set_value(self, key, value):
            if key in self.server:
                self.server[key] = value
            else:
                print(f" '{key}' 가 존재 하지 않습니다.")
            
    b1 = BankServer('오승재', '1234', 100, 22)
    print(b1.server)

    #  1.3 학생이 본인 계좌를 개설할 경우, 은행은 신규 가입 선물로 학생의 최초 입금액에 만원(10,000원)을 추가하여 개설한다.
    if 8 < b1.server.get('age') < 20:
        b1.server['price'] += 10000
    print(b1.server)

