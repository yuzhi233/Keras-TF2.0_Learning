# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 20:35:15 2020

@author: zhoubo
"""

#测试代码1：
# import tensorflow as tf
# from tensorflow.keras.layers import Concatenate
# import numpy as np
# print(tf.__version__)

# # a =np.array([])
# a = tf.ones([10,26,26,256])
# b = tf.ones([10,26,26,128])
# c = Concatenate()([a,b])

# print(tf.shape(c)) # [ 10  26  26 384]


#测试代码2
# import tensorflow as tf
# import timeit


# with tf.device('/cpu:0'):
# 	cpu_a = tf.random.normal([10000, 1000])
# 	cpu_b = tf.random.normal([1000, 2000])
# 	print(cpu_a.device, cpu_b.device)

# with tf.device('/gpu:0'):
# 	gpu_a = tf.random.normal([10000, 1000])
# 	gpu_b = tf.random.normal([1000, 2000])
# 	print(gpu_a.device, gpu_b.device)

# def cpu_run():
# 	with tf.device('/cpu:0'):
# 		c = tf.matmul(cpu_a, cpu_b)
# 	return c

# def gpu_run():
# 	with tf.device('/gpu:0'):
# 		c = tf.matmul(gpu_a, gpu_b)
# 	return c


# # warm up
# cpu_time = timeit.timeit(cpu_run, number=10)
# gpu_time = timeit.timeit(gpu_run, number=10)
# print('warmup:', cpu_time, gpu_time)


# cpu_time = timeit.timeit(cpu_run, number=10)
# gpu_time = timeit.timeit(gpu_run, number=10)
# print('run time:', cpu_time, gpu_time)

#测试代码3
# import tensorflow as tf
# import os

# os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# a = tf.constant(1.)
# b = tf.constant(2.)
# print(a+b)

# print('GPU:', tf.config.list_physical_devices('GPU'))

