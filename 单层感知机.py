import numpy as np
import random
import matplotlib.pyplot as plt


# sign function
def sign(v):
    if v > 0:
        return 1
    else:
        return -1


# train function to get weight and bias
def training():
    train_data1 = [[1, 3, 1], [2, 5, 1], [3, 8, 1], [2, 6, 1]]  # positive sample
    train_data2 = [[3, 1, -1], [4, 1, -1], [6, 2, -1], [7, 3, -1]]  # negative sample
    train_data = train_data1 + train_data2;

    weight = [0, 0]
    bias = 0
    learning_rate = 0.1

    train_num = int(input("train num:"))

    for i in range(train_num):
        train = random.choice(train_data)
        x1, x2, y = train;
        y_predict = sign(weight[0] * x1 + weight[1] * x2 + bias)
        print("train data:x:(%d, %d) y:%d ==>y_predict:%d" % (x1, x2, y, y_predict))
        if y * y_predict <= 0:
            weight[0] = weight[0] + learning_rate * y * x1
            weight[1] = weight[1] + learning_rate * y * x2
            bias = bias + learning_rate * y
            print("update weight and bias:")
            print(weight[0], weight[1], bias)
    print("stop training :")
    print(weight[0], weight[1], bias)

    # plot the train data and the hyper curve
    plt.plot(np.array(train_data1)[:, 0], np.array(train_data1)[:, 1], 'ro')
    plt.plot(np.array(train_data2)[:, 0], np.array(train_data2)[:, 1], 'bo')
    x_1 = []
    x_2 = []
    for i in range(-10, 10):
        x_1.append(i)
        x_2.append((-weight[0] * i - bias) / weight[1])
    plt.plot(x_1, x_2)
    plt.show()

    return weight, bias


# test function to predict
def test():
    weight, bias = training()
    while True:
        test_data = []
        data = input("enter q to quit,enter test data (x1, x2):")
        if data == 'q':
            break
        test_data += [int(n) for n in data.split(',')]
        predict = sign(weight[0] * test_data[0] + weight[1] * test_data[1] + bias)
        print("predict==>%d" % predict)


if __name__ == "__main__":
    test()