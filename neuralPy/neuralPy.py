# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:15:35 2019

@author: brianfoster
"""

import numpy
import scipy.special
import matplotlib.pyplot

class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        
        # Wih nodes: weights for input->hidden links
        # of size (hidden) x (input)
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5),
                                       (self.hnodes, self.inodes))
        
        # Who nodes: weights for hidden->output links
        # of size (output) x (hidden)
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5),
                                       (self.onodes, self.hnodes))
                                       
        # activation function is sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)
        pass
    
    def train(self, inputs_list, targets_list):
        
        # convert inputs and targets lists to 2D array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        
        # calculate signal into hidden layer
        # by matrix multiplying Wih weights x inputs
        hidden_inputs = numpy.dot(self.wih, inputs)
        
        # calculate signal emerging from hidden layer
        # by applying the activation function to signal at hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calcuate signal into final output layer
        # by matrix multiplying Who weights x hidden outputs
        final_inputs = numpy.dot(self.who, hidden_outputs)
        
        # calculate signal emerging from final output layer
        # by applying the activation function to signal at final output layer
        final_outputs = self.activation_function(final_inputs)
        
        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        
        # hidden layer error is the output_errors, split by weights,
        # recombined at hidden
        hidden_errors = numpy.dot(self.who.T, output_errors)
        
        #deltaWjk = alpha * Ek * sigmoid(Ok) * (1-sigmoid(Ok)) dot Oj-T
        #
        # deltaWjk : change in Weights to a node from layer J to layer K
        # alpha: learning rate
        # Ek : error at layer K
        # Ok: output at layer K
        # Oj-T: output from layer J, transposed       
        
        # output_errors used for weights between hidden-output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs *
            (1.0 - final_outputs)), numpy.transpose(hidden_outputs))
            
        # hidden_errors used for weights between input-hidden layers   
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs *
            (1.0 - hidden_outputs)), numpy.transpose(inputs))
        
        pass
    
    def query(self, inputs_list):
        
        # convert inputs_list to 2D array
        inputs = numpy.array(inputs_list, ndmin=2).T        
        
        # calculate signal into hidden layer
        # by matrix multiplying Wih weights x inputs
        hidden_inputs = numpy.dot(self.wih, inputs)
        
        # calculate signal emerging from hidden layer
        # by applying the activation function to signal at hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # calcuate signal into final output layer
        # by matrix multiplying Who weights x hidden outputs
        final_inputs = numpy.dot(self.who, hidden_outputs)
        
        # calculate signal emerging from final output layer
        # by applying the activation function to signal at final output layer
        final_outputs = self.activation_function(final_inputs)        
        
        return final_outputs
        
    def importData(self, filename):
        data_file = open(filename, 'r')
        data_list = data_file.readlines()
        data_file.close()
        return data_list
        
    def displayDataFromList(self, dataList, index):
        all_values = dataList[index].split(',')
        image_array = numpy.asfarray(all_values[1:]).reshape((28,28))
        matplotlib.pyplot.imshow(image_array, cmap='Greys', 
                                 interpolation='None')
        pass
    
    def displayDataFromSingle(self, single):
        image_array = numpy.asfarray(single[1:]).reshape((28,28))
        matplotlib.pyplot.imshow(image_array, cmap='Greys', 
                                 interpolation='None')
        pass
                                 
# SETUP FOR HANDWRITING RECOGNITION
                                 
input_nodes = 784
hidden_nodes = 50
output_nodes = 10

learning_rate = 0.3


n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# TRAIN THE NEURAL NETWORK
epochs = 1

# import MNIST training data from csv file
training_data_file = open("mnist_train_100.csv", 'r') #mnist_train.csv , mnist_train_100.csv
training_data_list = training_data_file.readlines()
training_data_file.close()       

for e in range(epochs):
# iterate through entire training data set
    for record in training_data_list:
        # csv format is target, x,y,z,...., (28x28 grid bmp values 0-255)
        all_values = record.split(',')
        # scale CSV values from 0-255 to 0.01-1.0
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        #define target output values, all=0.01 except desired index=0.99
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        n.train(inputs, targets)
        pass
    pass
  

# TEST THE NEURAL NETWORK

scorecard = []

# import MNIST test data from csv file
test_data_file = open("mnist_test_10.csv", 'r') #mnist_test.csv , mnist_test_10.csv
test_data_list = test_data_file.readlines()
test_data_file.close() 

# iterate through entire test data set
for record in test_data_list:
    # csv format is target, x,y,z,...., (28x28 grid bmp values 0-255)
    all_values = record.split(',')
    # correct answer aka tag is first value
    correct_label = int(all_values[0])
    #print("Correct Label: ", correct_label)
    # scale CSV values from 0-255 to 0.01-1.0
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # query the network
    outputs = n.query(inputs)
    # the index of the highest value corresponds to the label
    network_label = numpy.argmax(outputs)
    #print("Network's Answer: ", network_label)
    if (network_label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)
    pass
    
    pass
    
# calc and display performance score
scorecard_array = numpy.asarray(scorecard)
print("Performance: ", scorecard_array.sum()/scorecard_array.size)
                           
    
        
    