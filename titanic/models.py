from icecream import ic

from context.domains import Dataset
from context.models import Model


class TitanicModel(object):
    model = Model()
    dataset = Dataset()
    def __init__(self, train_fname, test_fname):
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출


    def preprocess(self):
        df = self.train
        ic(f'트레인 컬럼 {self.df.columns}')
        ic(f'트레인 헤드 {self.df.head()}')
        ic(df)
        df = self.drop_feature(df)
        df = self.create_train(df)
        df = self.create_label(df)
        return df


    def create_label(self, df) -> object:
        self.name_nominal(df)
        self.pclass_ordinal(df)
        self.sex_nominal(df)
        self.age_ratio(df)
        self.embarked_nominal(df)
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






