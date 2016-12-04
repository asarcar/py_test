#!/usr/bin/env python
import tensorflow as tf
a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([3.0, 4.0], name='b')
c = tf.reduce_sum(tf.mul(a, b))

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as s:
    print("Dot product {0}".format(s.run(c)))
