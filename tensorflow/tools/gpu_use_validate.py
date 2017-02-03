#!/usr/bin/env python
import tensorflow as tf
tf.logging.set_verbosity(tf.logging.DEBUG)
with tf.device('/cpu:0'):
  a1 = tf.constant([1.0, 2.0], name='a1')
  b1 = tf.constant([3.0, 4.0], name='b1')
  c1 = tf.reduce_sum(tf.mul(a1, b1))

with tf.device('/gpu:0'):
  a2 = tf.constant([5.0, 6.0], name='a2')
  b2 = tf.constant([7.0, 8.0], name='b2')
  c2 = tf.reduce_sum(tf.mul(a2, b2))

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as s:
    print("Dot product {0}".format(s.run(c1)))
    print("Dot product {0}".format(s.run(c2)))
