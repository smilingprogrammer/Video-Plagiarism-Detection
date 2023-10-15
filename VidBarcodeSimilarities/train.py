
import torch
from model import SiameseNetwork
from loss import ContrastiveLoss
from torch.utils.data import DataLoader, Dataset
import torchvision.datasets as datasets
from torch import optim

folder_datasets = datasets.ImageFolder(root="/content/drive/MyDrive/train_data")

# Resize the images and transform to tensors
transformation = transforms.Compose([transforms.Resize((100,100)),
                                     transforms.ToTensor()
                                    ])

# Initialize the network
siamese_dataset = SiameseNetworkDataset(imageFolderDataset=folder_datasets,
                                        transform=transformation)

train_batch_size=64
train_dataloader = DataLoader(siamese_dataset, 
                              shuffle=True, 
                              batch_size=train_batch_size)
model = SiameseNetwork()
criterion = ContrastiveLoss()
optimizer = optim.Adam(model.parameters(), lr = 0.0005 )


counter = []
loss_history = [] 
iteration_number= 0

def train():
    # Iterate throught the epochs
    for epoch in range(100):

        # Iterate over batches
        for i, (img0, img1, label) in enumerate(train_dataloader, 0):

            # Zero the gradients
            optimizer.zero_grad()

            # Pass in the two images into the network and obtain two outputs
            output1, output2 = model(img0, img1)

            # Pass the outputs of the networks and label into the loss function
            loss_contrastive = criterion(output1, output2, label)

            # Calculate the backpropagation
            loss_contrastive.backward()

            # Optimize
            optimizer.step()

            # Every 10 batches print out the loss
            if i % 10 == 0 :
                print(f"Epoch number {epoch}\n Current loss {loss_contrastive.item()}\n")
                iteration_number += 10

                counter.append(iteration_number)
                loss_history.append(loss_contrastive.item())

    show_plot(counter, loss_history)
