import numpy as np


class Perceptron(object):
    """Perceptron classifier:
    Parameters:
    learning_rate: float : Learning Rate
    num_iter: int : Number of iterations
    random_state: int: Random number generator seed

    Attributes:
    weight_af: [Number of features+1]:  Weight after fitting 
    errors: list : Misclassifications in each epoch. 
    """

    def __init__(self, learning_rate=0.01, num_iter=50, random_state=1):
        self.learning_rate = learning_rate
        self.num_iter = num_iter
        self.random_state = random_state
        self.errors = []

    def fit(self, X, y):
        """ 
        X: [num_examples, num_features]
        y: [num_examples]
        """

        random_state_gen = np.random.RandomState(self.random_state)
        self.weight_af = random_state_gen.normal(
            loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.errors = []
        for i in range(self.num_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                # print("i: update:xi:target:predict ", i, update, xi, target,self.predict(xi))
                self.weight_af[1:] += update * xi
                self.weight_af[0] += update
                # print("weight:", self.weight_af)
                errors += int(update != 0.0)
            self.errors.append(errors)
        return self

    def net_input(self, X):
        """ Calculate the net total: matrix multiplication of X to weights:
        [1, 2, 3, 4] [w1, w2, w3] +[w0] """
        return np.dot(X, self.weight_af[1:]) + self.weight_af[0]

# Step function, compares true class labels to the predicted class labels
    def predict(self, X):
        """ Return label """
        total_error = self.net_input(X)
        # print("Total error: ", total_error)
        return np.where(total_error > 0.0, 1, -1)
