from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()
    def __init__(self, train_fname, test_fname):
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        print(type(self.test))
        # self.id = self.test['PassengerId']
        # ic(f'트레인 컬럼 {self.train.columns}')
        # ic(f'트레인 헤드 {self.train.head()}')
        # id 추출


    def preprocess(self):
        this = self.dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id

        this = self.drop_feature(this)
        this = self.create_train(this)
        this = self.create_label(this)
        this = self.name_nominal(this)
        this = self.pclass_ordinal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.embarked_nominal(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        ic(f'1. Train의 타입 :  {type(this.train)}\n')
        ic(f'2. Train의 컬럼 :  {this.train.columns}\n')
        ic(f'3. Train의 상위 1개 :  {this.train.head(1)}\n')
        ic(f'4. Train의 null의 개수 :  {this.train}\n')
        ic(f'5. Test의  타입 : {type(this.test)}\n')
        ic(f'6. Test의 컬럼 :  {this.test.columns}\n')
        ic(f'7. Test의 상위 1개 :  {this.test.head(1)}\n')
        ic(f'8. Test의 null의 개수 :  {this.test.notnull().sum()}\n')
        print('*'*100)

    @staticmethod
    def create_label(df) -> object:
        return df

    @staticmethod
    def create_train(df) -> object:
        return df

    def drop_feature(self, df) -> object:

        '''
        self.sib_sp_garbage(df)
        self.parch_garbage(df)
        self.ticket_garbage(df)
        self.fare_garbage(df)
        self.cabin_garbage(df)
        '''
        return df
    '''
    Categorical vs. Quantitative
    Cate -> nominal (이름) vs. ordinal(순서)
    Quan -> interval (상대) vs. ratio (절대)
    '''

    @staticmethod
    def pclass_ordinal(df) -> object:
        return df

    @staticmethod
    def name_nominal(df) -> object:
        return df

    @staticmethod
    def sex_nominal(df) -> object:
        return df

    @staticmethod
    def age_ratio(df) -> object:
        return df

    @staticmethod
    def embarked_nominal(df):
        return df






