# coding:utf-8
import tensorflow as tf
import numpy as np

# Import MINST dataflow
from tensorflow_execise.mnist_data import input_data
#from mnist_data import input_data


mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)


# parameters
learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1

# tf Graph Input
x = tf.placeholder(tf.float32,[None,784]) # mnist data image of shape 28*28=784
y = tf.placeholder(tf.float32,[None,10]) # 0-9 digits recognition => 10 classes

# Set model weights
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

# construct model
pred = tf.nn.softmax(tf.matmul(x,W)+b) # softmax

# minimize error using cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred),reduction_indices=1))
# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
# Initializing the variables
init = tf.global_variables_initializer()


# Launch the graph
sess = tf.Session()
# with tf.Session() as sess:
sess.run(init)
# Training cycle
for epoch in range(training_epochs):
    avg_cost = 0.
    total_batch = int(mnist.train.num_examples/batch_size)
    # Loop over all batches
    for i in range(total_batch):
        batch_xs,batch_ys = mnist.train.next_batch(batch_size)
        # Fit training using batch data
        _, c = sess.run([optimizer,cost],feed_dict={x:batch_xs,y:batch_ys})
        # Compute average loss
        avg_cost += c/total_batch
    if (epoch+1) % display_step == 0:
        print ("Epoch:",'%04d' %(epoch + 1) ,"cost=","{:.9f}".format(avg_cost))

print ("Optimization finished!")

# Test model
correct_prediction = tf.equal(tf.argmax(pred,1),tf.argmax(y,1))
# Caculate accuracy for 3000 examples
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print ("Accuracy:",accuracy.eval({x:mnist.test.images[:3000],y:mnist.test.labels[:3000]}))
