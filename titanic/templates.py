from context.domains import Dataset
from context.models import Model


class TitanicTemplates(object):
    def __init__(self):
        self.model = Model()
        self.dataset = Dataset()

        self.a = self.model.new_model()
        self.b = self.model.save_model()
