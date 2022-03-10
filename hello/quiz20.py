import random
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

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

    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')
        cls_names = ['artist', 'titles']
        # a = [i for i in cls_names]
        ls1 = self.music_chart(soup, 'title')
        ls2 = self.music_chart(soup, 'artist')
        # self.dict1(ls1, ls2)
        # self.dict2(ls1,ls2)
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)


    def print_music_list(self,soup) -> None:
        artist = soup.find_all('p', {'class':'artist'})
        artist = [i.get_text() for i in artist]
        titles = soup.find_all('p', {'class':'titles'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))
        return None

    def find_rank(self, soup) -> None:
        for i, j in enumerate(['artist', 'titles']):
            for i, j in enumerate(self.music_chart(soup, j)):
                print(f'{i}위: {j}')
        return None

    @staticmethod
    def music_chart(soup, cls_nm) -> []:
        return [i.get_text().strip() for i in soup.find_all('p', {'class': cls_nm})]

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        ls1 = self.melon_music_chart(soup, 'ellipsis rank01')
        ls2 = self.melon_music_chart2(soup, 'checkEllipsis')
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)
        return dict

        return None

    @staticmethod
    def melon_music_chart(soup, cls_nm) -> []:
        return [i.get_text().strip() for i in soup.find_all('div',{'class': cls_nm})]

    @staticmethod
    def melon_music_chart2(soup, cls_nm) -> []:
        return [i.get_text().strip() for i in soup.find_all('span',{'class': cls_nm})]

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')


    def quiz29dataframe2(self) -> None:
        dict = self.quiz27melon()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/melon.csv', sep=',', na_rep='NaN')