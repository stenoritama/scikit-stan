import numpy as np

from skstan.regression.linear_models.linear_model_v2 import LinearRegression


def liner_regression():
    x = np.array([[1, 2, 5, 3, 2], [6, 5, 1, 1, 1]])
    y = np.array([1, 0])

    glm = LinearRegression(shrinkage=10, chains=8)

    stanfit = glm.fit(x, y)
    print(stanfit)


if __name__ == '__main__':
    liner_regression()