from icecream import ic

from context.domains import Dataset
from context.models import Model
import matplotlib.pyplot as plt

from titanic import TitanicModel

'''
데이터 시각화
엔티티(개체)를 차트로 표현하는 것

모든 feature 를 다 그려야 하지만, 시간 관계상
Survived, Pclass, Sex, embarked 4개만 그리겠습니다.
템플릿 메소드 패턴으로 구성하시오

'''
class TitanicTemplates(object):
    dataset = Dataset()
    model = Model()
    def __init__(self, fname):
        self.entity = self.model.new_model(fname)
        this = self.entity
        ic(f'트레인의 타입: {type(this)}')
        ic(f'트레인의 컬럼: {this.columns}')
        ic(f'트레인의 상위5행: {this.head()}')
        ic(f'트레인의 하위5행: {this.tail()}')

    def visualize(self) -> None:
        this = self.entity
        self.draw_survived(this)
        self.draw_pclass(this)
        self.draw_sex(this)
        self.draw_embarked(this)

    @staticmethod
    def draw_survived(this) -> None:
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived']
        plt.show()

    @staticmethod
    def draw_pclass(this) -> None:
        plt.show()

    @staticmethod
    def draw_sex(this) -> None:
        plt.show()

    @staticmethod
    def draw_embarked(this) -> None:
        plt.show()







