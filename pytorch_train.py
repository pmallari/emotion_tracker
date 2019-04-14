import os
import numpy as np 

import torch
import torch.nn as nn 

import torchvision 
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt 

# Check if GPU is available
train_on_gpu = torch.cuda.is_available()

if not train_on_gpu:
    print("Training on CPU")
else:
    print("Training on GPU")

"""
Import and preprocess datasets. Divide datasets to 3 set

train_set   60%
valid_set   20%
test_set    20%

Preprocessing

Retrieve image, convert from BGR2GREY (OpenCV?)
Pad side to create square data
Resize to n x n
Convert to tensor

n depends on model expected input
224 - VGG16
255 - Inception v3

"""

"""
Define dataset
"""
data_dir    = 'data/images/'
train_dir   = os.path.join(data_dir, 'train/')
valid_dir   = os.path.join(data_dir, 'valid/')
test_dir    = os.path.join(data_dir, 'test/')

classes     = ['angry', 'sad',
               'neutral', 'happy',
               'calm', 'disgust',
               'fear', 'surprise']


img_side    = 225

"""
Define transforms
"""
train_transform = transforms.Compose([transforms.RandomResizedCrop(img_side),
                                      transforms.RandomRotation(30),
                                      transforms.RandomHorizontalFlip(p = 0.5),
                                      transorms.ToTensor()])

valid_transform = transforms.Compose([transforms.CenterCrop(img_side),
                                      transforms.ToTensor()])

test_transform  = transforms.Compose([transforms.CenterCrop(img_side),
                                      transforms.ToTensor()])

"""
Generate image dataset
"""

train_data      = datasets.ImageFolder(train_dir,
                                       transform = train_transform)

valid_data      = datasets.ImageFolder(valid_dir,
                                       transform = valid_transform)

test_data       = datasets.ImageFolder(test_dir,
                                       transform = test_transform)

print(f"Training dataset contains {len(train_data)}.")
print(f"Validation dataset contains {len(valid_data)}.")
print(f"Test dataset contains {len(test_data)}.")

"""
Define DataLoaders
"""

batch_size  = 32
num_workers = 0

train_loader = torch.utils.data.DataLoader(train_data, 
                                           batch_size   = batch_size,
                                           num_workers  = num_workers,
                                           shuffle      = True)


valid_loader = torch.utils.data.DataLoader(valid_data, 
                                           batch_size   = batch_size,
                                           num_workers  = num_workers,
                                           shuffle      = True)

test_loader  = torch.utils.data.DataLoader(test_data, 
                                           batch_size   = batch_size,
                                           num_workers  = num_workers,
                                           shuffle      = True)

"""
Load pretrained model
"""

model = models.vgg16(pretrained = True)

# Freeze model feature parameters
for param in model.features.parameters():
    param.requires_grad = False

"""
Defining the new fully connected layer
"""

n_inputs = model.classifier[6]