import random


class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print("리스트1\n", list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])

        list2 = ['math', 'english']
        # print('리스트2\n',list2[0])
        print(list2[0])

        list3 = [1, '2', [1, 2, 3, ]]
        print('리스트3\n', list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print('리스트4, 5\n', list4 + list5)
        print(2 * list4)

        list4.append(list5)
        print('리스트 append\n', list4)

        list4[-2:] = []
        print('리스트[-2:]\n', list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print('리스트6\n', c)
        print('리스트7\n', )

        return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str: return None

    def quiz24zip(self) -> str: return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27(self) -> str: return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None