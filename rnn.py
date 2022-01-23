import torch
import torch.nn as nn
import torch.optim as optim
from torchtext.datasets import Multi30k
from torchtext.data import Field, BucketIterator
import numpy as np
import spacy
import random
from torch.utils.tensorboard import SummaryWriter

spacy_ger = spacy.load('de')
spacy_eng = spacy.load('en')


# import torch.nn.functional as F
# from torch.utils.data import DataLoader
# import torchvision.datasets as datasets
# import torchvision.transforms as transforms
