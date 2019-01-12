from pystan import StanModel

from skstan.backend.stan import StanBackend
from tests.rootdir import TEST_DIR_ROOT


class TestStanBackend:

    def test_load_stan_model(self):
        # Test that a pickled stan model is loaded and deserialized.
        StanBackend.PKL_BASE_DIR = TEST_DIR_ROOT + '/sample_model'
        model_name = 'linear_regression'
        actual_model = StanBackend.load_stan_model(model_name)

        assert StanModel == type(actual_model)