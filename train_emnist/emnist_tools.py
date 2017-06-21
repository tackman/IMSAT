# -*- coding: utf-8 -*-
import gzip, os, six, sys
from six.moves.urllib import request
from PIL import Image
import numpy as np

parent = "http://yann.lecun.com/exdb/mnist"
train_images_filename = "emnist-balanced-train-images-idx3-ubyte.gz"
train_labels_filename = "emnist-balanced-train-labels-idx1-ubyte.gz"
test_images_filename = "emnist-balanced-test-images-idx3-ubyte.gz"
test_labels_filename = "emnist-balanced-test-labels-idx1-ubyte.gz"
n_train = 112800
n_test = 18800
dim = 28 * 28

def load_emnist(data_filename, label_filename, num):
	images = np.zeros((num, dim), dtype=np.float32)
	label = np.zeros((num,), dtype=np.int32)
	with gzip.open(data_filename, "rb") as f_images, gzip.open(label_filename, "rb") as f_labels:
		f_images.read(16)
		f_labels.read(8)
		for i in six.moves.range(num):
			label[i] = ord(f_labels.read(1))
			for j in six.moves.range(dim):
				image = ord(f_images.read(1)) / 255.0
				iamge = image * 2.0 - 1.0
				images[i, j] = image

			if i % 1000 == 0 or i == num - 1:
				sys.stdout.write("\rloading images ... ({} / {})".format(i, num))
				sys.stdout.flush()
	sys.stdout.write("\n")
	images = images.reshape((num, 1, 28, 28))
	return images, label

def load_train_images():
	assert os.path.exists(train_images_filename), "{} not found. You can download it from https://www.westernsydney.edu.au/bens/home/reproducible_research/emnist".format(train_images_filename)
	images, labels = load_emnist(train_images_filename, train_labels_filename, n_train)
	return images, labels

def load_test_images():
	assert os.path.exists(test_images_filename), "{} not found. You can download it from https://www.westernsydney.edu.au/bens/home/reproducible_research/emnist".foramt(test_images_filename)
	images, labels = load_emnist(test_images_filename, test_labels_filename, n_test)
	return images, labels

def extract_bitmaps():
	train_dir = "train_images"
	test_dir = "test_images"
	try:
		os.mkdir(train_dir)
		os.mkdir(test_dir)
	except:
		pass
	data_train, label_train = load_test_images()
	data_test, label_test = load_test_images()
	print("Saving training images ...")
	for i in range(data_train.shape[0]):
		image = Image.fromarray(data_train[i].reshape(28, 28))
		image.save("{}/{}_{}.bmp".format(train_dir, label_train[i], i))
	print("Saving test images ...")
	for i in range(data_test.shape[0]):
		image = Image.fromarray(data_test[i].reshape(28, 28))
		image.save("{}/{}_{}.bmp".format(test_dir, label_test[i], i))