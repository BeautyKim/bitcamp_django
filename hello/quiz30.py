import random
import string

import numpy as np
import pandas as pd
from icecream import ic

from hello.domains import my100, myRandom


class Quiz30:
    '''
        데이터프레임 문제 Q02
    ic| df:     A   B   C
            1   1   2   3
            2   4   5   6
            3   7   8   9
            4  10  11  12
    '''
    def quiz30_df_4_by_3(self) -> str:
        # df = pd.DataFrame([[1,2,3],
        #                   [4,5,6],
        #                   [7,8,9],
        #                   [10,11,12]], index=range(1,5), columns=['A','B','C'])

        # 위 식을 리스트결합 형태로 분해해서 조립하시오
        ls = [[i for i in range(1, 13)[i*3:(i+1)*3]] for i in range(4)]
        print(ls)
        df = pd.DataFrame(ls, index=range(1, 5), columns=['A', 'B', 'C'])
        ic(df)

        return None

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''

    def quiz31_rand_2_by_3(self) -> str:
        df = pd.DataFrame([[myRandom(10, 100) for i in range(3)] for i in range(2)])
        # 넘파이 사용한 예제
        # df = pd.DataFrame(np.random.randint(10, 100, size=(2, 3)))
        ic(df)
        return None

    '''
            데이터프레임 문제 Q04.
            국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
             단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

              ic| df4:        국어  영어  수학  사회
                        lDZid  57  90  55  24
                        Rnvtg  12  66  43  11
                        ljfJt  80  33  89  10
                        ZJaje  31  28  37  34
                        OnhcI  15  28  89  19
                        claDN  69  41  66  74
                        LYawb  65  16  13  20
                        QDBCw  44  32   8  29
                        PZOTP  94  78  79  96
                        GOJKU  62  17  75  49
    '''
    @staticmethod
    def id(chr_size) -> str: return ''.join([random.choice(string.ascii_letters) for i in range(chr_size)])
    def quiz32_df_grade(self) -> object:
        ls = np.random.randint(0, 100, (10, 4))
        idx = [self.id(chr_size=5)for i in range(10)]
        col = ['국어', '영어', '수학', '사회']
        df1 = pd.DataFrame(ls, index=idx, columns=col)
        ic(df1)

        # ls2 = {i:j for i, j in zip(idx, ls)}
        ls2 = dict(zip(idx, ls))
        df2 = pd.DataFrame.from_dict(ls2, orient='index', columns=col)
        ic(df2)

        return None

    def quiz33_df_loc(self) -> str:
        # d = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
        #      {'a': 100, 'b': 200, 'c': 300, 'd': 400},
        #      {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
        # df = pd.DataFrame([dict(zip(['A', 'B', 'C', 'D'], np.random.randint(1, 100, 4))) for _ in range(3)])
        df = self.createDf(keys=['a', 'b', 'c', 'd'],
                           vals=np.random.randint(1, 100, 4),
                           len=3)
        ic(df)
        return None

    @staticmethod
    def createDf(keys, vals, len):
        return pd.DataFrame ([dict(zip(keys, vals)) for _ in range(len)])

    def quiz34(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None