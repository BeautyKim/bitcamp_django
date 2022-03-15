from icecream import ic

from context.domains import Dataset
from context.models import Model
from titanic import TitanicModel


class TitanicTemplates(object):
    def __init__(self, train_fname, test_fname):
        self.dataset = Dataset()
        self.model = Model()
        self.titanic = TitanicModel(train_fname, test_fname)

