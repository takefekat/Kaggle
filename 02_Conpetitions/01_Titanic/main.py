import pandas as pd
import numpy as np
import dabl

TRAIN_PATH = '01_data/train.csv'
TEST_PATH = '01_data/test.csv'
TARGET = 'Survived'
SUBMISSION_PATH = 'submission.csv'


train = pd.read_csv(TRAIN_PATH)
test = pd.read_csv(TEST_PATH)
train.head()
