from math import sqrt

X = [(0, 1),
    (2, 2),
    (4, 3),
    (9, 8),
    (3, 5)]

x_train = [X[i][0] for i in range(0,len(X))]
y_train = [X[i][1] for i in range(0,len(X))]

def zero_vector(len):
    vector = [0] * len
    return vector

def vector_multi(v1 , v2):
    return [x*y for x , y in zip(v1 , v2)]

def dot(v1 , v2):
    return sum(x*y for x , y in zip(v1 , v2))


def add_number_to_vec(wx , b):
    return [i+b for i in wx]

# def rmse(y_test , predictions):

#     vmv = vec_minus_vec(y_test , predictions)

#     vmvsqr = vector_multi(vmv , vmv)

#     sum_of_vector_values(vmvsqr)

#     vmvsqr_devide_by_n = sum_of_vector_values(vmvsqr)/len(y_test)

#     return sqrt(vmvsqr_devide_by_n)


def sum_of_vector_values(v):
    sum = 0
    for i in v:
        sum = sum + i
    return sum

def vec_minus_vec(v1 , v2):
    return [i - j for i , j in zip(v1 , v2)]

def vec_element_multi_by_num(v , num):
    return [i * num for i in v]



class LinearRegression:
    
    def __init__(self , lr=0.001 , n_iters=1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = 0

    def fit(self , X , y):
        n_samples = len(X)
        n_features = 1
        self.weights =  zero_vector(len(X))
        self.bias = 1.5

        for _ in range(self.n_iters):

            y_pred = add_number_to_vec(vector_multi(X , self.weights) , self.bias)

            dw = (1/n_samples) + dot((X) , vec_minus_vec(y_pred , y))
            db = (1/n_samples) + sum_of_vector_values(vec_minus_vec(y_pred , y))            

            self.weights = add_number_to_vec(self.weights , -(self.lr * dw))
            self.bias = self.bias  -(self.lr * db)

    def predict(self , X):
        y_pred =   X * self.weights[0] + self.bias   #add_number_to_vec( vector_multi(X , self.weights) , self.bias)
        return y_pred 



dm = LinearRegression()
dm.fit(x_train , y_train)

