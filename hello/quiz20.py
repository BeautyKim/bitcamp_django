import random
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

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

    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml
        # print(soup.prettify())
        # artist = soup.find_all(attrs={'class':'artist'})
        a = [i.get_text().strip() for i in soup.find_all('p', {'class':'artist'})]
        print(a[0:3]) #출력결과 -> ['MSG워너비(M.O.M)', '태연 (TAEYEON)', '멜로망스(MeloMance)']


        return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:

        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        print('\n'.join([i.get_text().strip() for i in soup.find_all('div',{'class':'ellipsis rank01'})][0:3]))
                                                                                                                #출력화면
                                                                                                                #INVU
                                                                                                                # 사랑은 늘 도망가
                                                                                                                # 취중고백
        return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None