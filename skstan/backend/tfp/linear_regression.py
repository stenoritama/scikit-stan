from abc import ABCMeta
from abc import abstractmethod

import tensorflow as tf
from tensorflow_probability import distributions as tfd
from tensorflow_probability import edward2 as ed

from skstan.backend.tfp import BaseTFPModel


class BaseTFPLinearRegression(BaseTFPModel, metaclass=ABCMeta):
    """
    Abstract base class for Linear regression using TensorFlow Probability.
    """

    def log_join_fn(self):
        return ed.make_log_joint_fn(self.posterior_dist)

    @abstractmethod
    def posterior_dist(self, features):
        pass


class TFPLinearRegression(BaseTFPLinearRegression):
    """
    Linear regression implementation using TensorFlow Probability.
    """

    def __init__(self):
        pass

    def posterior_dist(self, features):
        """

        Parameters
        ----------
        features

        Returns
        -------

        """
        pass


class TFPLogisticRegression(BaseTFPLinearRegression):
    """
    Logistic regression implementation using TensorFlow Probability.
    """

    def __init__(self):
        pass

    def set_params(self):
        pass

    def posterior_dist(self, features) -> tfd.Distribution:
        """

        Parameters
        ----------
        features

        Returns
        -------

        """
        coeffs = ed.Normal(loc=0.0,
                           scale=1.0,
                           sample_shape=features.shape[1],
                           name='coeffs')
        outcomes = ed.Bernoulli(
            logits=tf.tensordot(features, coeffs, [[1], [0]]),
            name='outcomes')
        return outcomes


class TFPPoissonRegression(BaseTFPLinearRegression):
    """
    Poisson regression implementation using TensorFlow Probability.
    """

    def __init__(self):
        pass

    def posterior_dist(self, features):
        """

        Parameters
        ----------
        features

        Returns
        -------

        """
        pass
