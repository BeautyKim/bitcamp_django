import random

from hello import Member
from hello.domains import my100, myRandom, memberlist


class Quiz00:
    def quiz00calculator(self) -> float:
        a = my100()
        b = my100()
        o = ['+','-','*','/','%']
        c = random.choice(o)
        if(c =='+'):
            res = a + b
        elif(c == '-'):
            res = a - b
        elif(c == '*'):
            res = a * b
        elif(c == '/'):
            res = a / b
        elif(c == '%'):
            res = a % b
        print(('#'*30)+f'\n{a} {c} {b} = {res}\n'+('#'*30))

        return None

    def quiz01bmi(self):
        this = Member()
        this.name = input('이름: ')
        this.height = float(input('키: '))
        this.weight = float(input('몸무게: '))
        bmi = this.weight / (this.height * this.height) * 10000
        if bmi < 18.5:
            res = '저체중'
        elif bmi < 23:
            res = '정상'
        elif bmi < 25:
            res = '과체중'
        elif bmi < 30:
            res = '경도 비만(1단계 비만)'
        elif bmi < 35:
            res = '중도 비만(2단계 비만)'
        else:
            res = '고도 비만'
        return print(('#'*30)+f'\n{this.name}님의 BMI지수는 {res}입니다\n'+('#'*30))

    def quiz02dice(self):
        return print(('#'*30)+f'\n{myRandom(1, 6)}\n'+('#'*30))

    def quiz03rps(self):
        comList = ['가위', '바위', '보']
        c = random.choice(comList)
        p = input('가위, 바위, 보')
        if p == c:
            res = '무승부'
        elif (p == '가위' and c == '보') or (p == '바위' and c == '가위') or (p == '보' and c == '바위'):
            res = '승리'
        else:
            res = '패배'
        return print(('#'*30)+f'\n플래이어: {p} 컴퓨터: {c} 결과: {res}\n'+('#'*30))


    def quiz04leap(self):
        y = myRandom(2000, 2022)
        res = '윤년' if y%4==0 and y%100!=0 or y%400==0 else '평년'
        print(('#' * 30) + f'\n{y}년은 {res}\n' + ('#' * 30))
        '''
        Java Style(y%4==0 && 4== y%100!=0 || y&400==0) ? "윤년":"평년";
        '''

        return None

    def quiz05grade(self):
        name = input('이름: ')
        kor = my100()
        eng = my100()
        math = my100()

        total = kor + eng + math
        avg = total/3
        gradePass = '합격' if avg >= 60 else '불합격'
        return print(('#'*30)+
                     f'\n학생 {name}은(는)\n'
                     f'총점: {total} 평균: {avg} 이므로\n'
                     f'{gradePass}입니다\n'
                     +('#'*30))

    def quiz06memberChoice(self):
        return memberlist()[myRandom(0,23)]
        #return random.choice(memberlist())

    def quiz07lotto(self):
        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        Account.main()

    def quiz09gugudan(self):  # 책받침구구단
        #Comprension [i for i in range()]
        gugudan = [[i, j, i*j] for i in range(2,6) for j in range(1,10)]
        for i in gugudan:
            print(f'{i[0]}*{i[1]}={i[2]}')

        '''
        #for문 활용(,end= '\t' -> 문자열을 가로로 나열)
        for i in range(1, 10):
            for j in range(2,6):
                print(f'{j} * {i} = {j*i}',end = '\t')
            print(' ')
        print(' ')
        for i in range(1, 10):
            for j in range(6,10):
                print(f'{j} * {i} = {j*i}',end = '\t')
            print('')
        '''
'''
08번 문제 해결을 위한 클래스는 다음과 같다.
[요구사항(RFP)]
은행이름은 Bitbank
임금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
123-12-123456
금액은 100만원 ~ 999만원 사이로 랜덤하게 입금된다.
'''
class Account(object):
    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = Quiz00().quiz06memberChoice() if name == None else name
        #self.account_number = f'{myRandom(0,1000):0>3}-{myRandom(0,100):0>2}-{myRandom(0,1000000):0>6}'
        self.account_number = self.creat_account_number()
        self.money = myRandom(100, 1000)


    def to_string(self):
        return f'은행: {self.BANK_NAME}\n' \
               f'입금자: {self.name}\n' \
               f'계좌번호: {self.account_number}\n' \
               f'금액: {self.money}만원'

    #[i for i in range]
    def creat_account_number(self):
        '''
        ls = [str(myRandom(0,10)) for i in range(3)]
        ls.append('-')
        ls += [str(myRandom(0,10)) for i in range(2)]
        ls.append('-')
        ls += [str(myRandom(0,10)) for i in range(6)]
        '''
        return ''.join(['-' if i==3 or i==6 else str(myRandom(0,10)) for i in range(13)])
    def del_account(self, ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]
    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌해지')
            if menu =='0':
                break
            if menu =='1':
                acc = Account(None, None, None)
                print(f'{acc.to_string()} ...개설 되었습니다')
                ls.append(acc)
            elif menu =='2':
                print( '\n'.join([i.to_string() for i in ls]))
            elif menu =='3':
                account_number = input('입금할 계좌번호')
                deposit = input('입금액')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        pass

            elif menu =='4':
                account_number = input('출금할 계좌번호')
                money = input('출금액')
                #추가코드 완성
            elif menu == '5':
                account_number = input('탈퇴할 계좌번호')
            else:
                print('Wrong Number... Try Again')
                continue

