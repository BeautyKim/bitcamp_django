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
        year = int(input('연도 입력: '))
        a = year
        if a%4==0 and a%100!=0 or a%400==0:
            res = '윤년'
        else:
            res = '평년'
        return print(('#'*30)+f'\n{res}\n'+('#'*30))

    def quiz05grade(self):
        name = input('이름: ')
        kor = float(input('국어: '))
        eng = float(input('영어: '))
        math = float(input('수학: '))

        total = kor + eng + math
        avg = total/3
        gradePass = '합격' if avg >= 60 else '불합격'
        return print(('#'*30)+
                     f'\n학생 {name}은(는)\n'
                     f'총점: {total} 평균: {avg} 이므로\n'
                     f'{gradePass}입니다\n'
                     +('#'*30))

    def quiz06memberChoice(self):

        return print(('#'*30)+f'\n{random.choice(memberlist())}\n'+('#'*30))

    def quiz07lotto(self):
        pass

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        pass

    def quiz09gugudan(self):  # 책받침구구단
        pass