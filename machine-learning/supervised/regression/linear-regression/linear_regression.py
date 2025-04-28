import numpy as np

class linearRegression:
  def __init__(self,lr,iterations):
    self.iter = iterations
    self.lr = lr
    self.weights = 0
    self.bias = 0

  def fit(self, X_train, y):
    number_of_samples, number_of_features = X_train.shape # 500 x 13 means 500 samples and 13 features.
    self.weights = np.zeros(number_of_features)
    self.bias = 0

    # Implementing gradient descent
    for i in range(self.iter):
      y_pred = np.dot(X_train,self.weights) + self.bias

      # Taking parital deravatives
      dw = (1/number_of_samples) * np.dot(X_train.T,y_pred - y)
      db = (1/number_of_samples) * np.sum(y_pred - y)

      # Update the old weights/bias
      self.weights = self.weights - self.lr*dw
      self.bias = self.bias - self.lr * db
    return self

  def predict(self,X_test):
    return np.dot(X_test,self.weights) + self.bias