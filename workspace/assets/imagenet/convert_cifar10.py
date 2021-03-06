
# coding: UTF-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import numpy as np
import tensorflow as tf
from PIL import Image

from reader import Cifar10Reader

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('format', 'png', "ファイルフォーマット")
tf.app.flags.DEFINE_string('file', None, "処理するファイルのパス")
tf.app.flags.DEFINE_string('out', './images', "処理するファイルのパス")
tf.app.flags.DEFINE_integer('offset', 0, "読み飛ばすレコード数")
tf.app.flags.DEFINE_integer('length', 1000, "読み込んで変換するレコード数")

basename = os.path.basename(FLAGS.file)
path = os.path.dirname(FLAGS.file)

reader = Cifar10Reader(FLAGS.file)

stop = FLAGS.offset + FLAGS.length
for index in range(FLAGS.offset, stop):
    image = reader.read(index)

    print('label: %d' % image.label)
    imageshow = Image.fromarray(image.byte_array.astype(np.uint8))

    # file_name = '%s-%02d-%d.%s' % (basename, index, image.label, FLAGS.format)
    # file = os.path.join(path, file_name)

    file_name = '%02d.%s' % (index, FLAGS.format)
    file_path = '%s/%d' % (FLAGS.out, image.label)
    if not os.path.isdir(file_path):
        os.makedirs(file_path)
    file = os.path.join(file_path, file_name)

    with open(file, mode='wb') as out:
        imageshow.save(out, format=FLAGS.format)

reader.close()






