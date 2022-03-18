import pandas as pd
from icecream import ic

from context.domains import Dataset
from context.models import Model
import numpy as np
import pandas


class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def preprocess(self, train_fname, test_fname):
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp','Parch','Ticket', 'Fare', 'Cabin', 'Embarked']
        # 데이터셋은 Train, Test, Validation 3종류로 나뉜다
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        this.id = this.test[feature[0]]
        this.label = this.train[feature[1]]
        this.train = this.train.drop(feature[1], axis=1)
        # Entity 에서 Object로 전환
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Cabin', 'Ticket')
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')

        # this = self.name_nominal(this)
        # self.kwargs_sample(name='이순신')
        # this = self.create_this(self.dataset)
        # this = self.create_train(this)
        # this = self.pclass_ordinal(this)

        self.df_info(this)
        return this

    @staticmethod
    def df_info(this):
        [print(f'{i.info()}') for i in [this.train, this.test]]
        ic(this.train.head(3))
        ic(this.test.head(3))

    @staticmethod
    def id_info(this):
        ic(f'id 의 타입  {type(this.id)}')
        ic(f'id 의 상위 3개 {this.id[:3]}')


    @staticmethod
    def drop_feature(this, *feature) -> object:
        # for i in feature:
        #     this.train = this.train.drop(i, axis=1)
        #     this.test = this.test.drop(i, axis=1)

        '''for i in [this.train, this.test]:
            for j in feature:
                i.drop(j, axis=1, inplace=True)
        '''
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]]


        return this

    '''@staticmethod
    def print_this(this):
        print('*'*100)
        ic(f'1. Train의 타입 :  {type(this.train)}\n')
        ic(f'2. Train의 컬럼 :  {this.train.columns}\n')
        ic(f'3. Train의 상위 1개 :  {this.train.head(1)}\n')
        ic(f'4. Train의 null의 개수 :  {this.train.isnull().sum()}\n')
        ic(f'5. Test의  타입 : {type(this.test)}\n')
        ic(f'6. Test의 컬럼 :  {this.test.columns}\n')
        ic(f'7. Test의 상위 1개 :  {this.test.head(1)}\n')
        ic(f'8. Test의 null의 개수 :  {this.test.isnull().sum()}\n')
        ic(f'9. Id의 타입 :  {type(this.id)}\n')
        ic(f'10. Id의 상위 10개 :  {this.id[:10]}\n')
        print('*'*100)'''


    def create_this(self, dataset) -> object:
        this = self.dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id
        return this

    @staticmethod
    def create_train(this) -> object:
        return this
    '''
    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        ic(type(kwargs))  # ic| type(feature): <class 'tuple'>
        {print(''.join(f'key:{i}, val:{j}')) for i, j in kwargs.items()}  # key:name, val:이순신

        self.sib_sp_garbage(this)
        self.parch_garbage(this)
        self.ticket_garbage(this)
        self.fare_garbage(this)
        self.cabin_garbage(this)
    '''


    # Categorical vs. Quantitative
    # Cate -> nominal (이름) vs. ordinal(순서)
    # Quan -> interval (상대) vs. ratio (절대)


    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def extract_title_from_name(this) -> None:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False) # [A-Za-z]반드시 대소문자가 포함되어야한다
        ic(this.train.head(5))
        return this

    @staticmethod
    def remove_duplicate(this) -> None:
        a = []
        for dataset in [this.train, this.test]:
            a += list(set(dataset['Title']))
        a = list(set(a))
        title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Mester': 4, 'Royal': 5, 'Rare': 6}
        return title_mapping
        # ['Lady', 'Mr', 'Dona', 'Mlle', 'Capt', 'Master', 'Jonkheer', 'Mrs', 'Countess',
        # 'Dr', 'Ms', 'Miss', 'Rev', 'Col', 'Sir', 'Major', 'Don', 'Mme'
        # Royal : ['Countess','Lady', 'Sir']
        # Rare : ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jjonkheer', 'Dona', 'Mme']
        # Mr : ['Mlle']
        # Ms : ['Miss']
        # Master
        # Mrs

    @staticmethod
    def title_nominal(this, title_mapping) -> object:
        for dataset in [this.train, this.test]:
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jjonkheer', 'Dona', 'Mme'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Mlle'], 'Mr')
            dataset['Title'] = dataset['Title'].replace(['Miss'], 'Ms')
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this


    @staticmethod
    def sex_nominal(this) -> object:
        gender_mapping = {'male': 0, 'female': 1}
        for dataset in [this.train, this.test]:
            dataset['Gender'] = dataset['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ratio(this) -> object:
        train = this.train
        test = this.test
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                       'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        for these in train, test:
            # pd.cut() 을 사용하시오. 다른 곳은 고치지 말고 다음 두 줄만 코딩하시오
            these['AgeGroup'] = pd.cut(these['Age'], bins, right=False, labels=labels)  # pd.cut() 을 사용
            these['AgeGroup'] = these['AgeGroup'].map(age_mapping)  # map() 을 사용
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        embarked_mapping = {'S': 1, 'C': 2, 'Q': 3}
        this.train = this.train.fillna({'Embarked': 'S'})
        for dataset in [this.train, this.test]:
            dataset['Embarked'] = dataset['Embarked'].map(embarked_mapping)
        return this

    @staticmethod
    def fare_ratio(this) -> object:
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        # print(f'qcut 으로 bins 값 설정 {this.train["FareBand"].head()}')
        bins = [-1, 8, 15, 31, np.inf]
        return






