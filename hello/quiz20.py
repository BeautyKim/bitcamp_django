import random


class Quiz20:

    def quiz20list(self) -> str:
        print('#'*30)
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])

        list2 = ['math', 'english']
        print(list2[0])

        list3 = [1, '2', [1, 2, 3, ]]
        print(list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)

        list4.append(list5)
        print(list4)

        list4[-2:] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print()
        print('#' * 30)

        return None

    def quiz21tuple(self) -> str:
        print('#' * 30)



        print('#' * 30)
        return None

    def quiz22dict(self) -> str:
        print('#' * 30)

        print('#' * 30)
        return None

    def quiz23listcom(self) -> str:
        print('-----------------legacy----------------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('-----------------Comprension----------------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> str: return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27(self) -> str: return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None