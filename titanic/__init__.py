# https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.models import TitanicModel
from titanic.templates import TitanicTemplates
from titanic.views import TitanicView

if __name__ == '__main__':
    view = TitanicView()
    model = TitanicModel(train_fname='train.csv', test_fname='test.csv')

    while 1:

        menu = input('1.템프릿 2.전처리')
        if menu == '1':
            print(' #### 1. 템플릿 #### ')
            templates = TitanicTemplates()

            # view.preprocess('train.csv', 'test.csv')
            break
        elif menu == '2':
            print(' #### 2. 전처리 #### ')
        else:
            break