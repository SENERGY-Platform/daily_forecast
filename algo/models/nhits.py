from darts.models import NHiTSModel
from .helper import create_darts_encoder
from algo.operator import Operator

class DartNHITS(Operator):
    def __init__(self, config):
        super()
        kwargs = {}
        if config['add_time_covariates']:
            encoders = create_darts_encoder()
            kwargs['add_encoders'] = encoders

        self.model = NHiTSModel(num_stacks=3, num_blocks=2, num_layers=1, **kwargs)

    def fit(self, train_ts):
        self.model.fit(train_ts)
        
    def predict(self, number_steps):
        return self.model.predict(number_steps)