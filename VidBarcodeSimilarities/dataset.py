
import numpy as np
import random
from PIL import Image
import PIL.ImageOps   
from torch.utils.data import DataLoader, Dataset


class SiameseNetworkDataset(Dataset):
    def __init__(self,imageFolderDataset,transform=None):
        self.imageFolderDataset = imageFolderDataset    
        self.transform = transform
        
    def __getitem__(self,index):
        img0_tuple = random.choice(self.imageFolderDataset.imgs)

        should_get_same_class = random.randint(0,1) 
        if should_get_same_class:
            while True:
                img1_tuple = random.choice(self.imageFolderDataset.imgs) 
                if img0_tuple[1] == img1_tuple[1]:
                    break
        else:

            while True:
                img1_tuple = random.choice(self.imageFolderDataset.imgs) 
                if img0_tuple[1] != img1_tuple[1]:
                    break

        img0 = Image.open(img0_tuple[0])
        img1 = Image.open(img1_tuple[0])

        # img0 = img0.convert("L")
        # img1 = img1.convert("L")
        if self.transform is not None:
            img0 = self.transform(img0)
            img1 = self.transform(img1)

        # img0 = np.asarray(img0, dtype=np.float64)/255.0
        # img1 = np.asarray(img1, dtype=np.float64)/255.0
        
        return img0, img1, torch.from_numpy(np.array([int(img1_tuple[1] != img0_tuple[1])], dtype=np.float32))
    
    def __len__(self):
        return len(self.imageFolderDataset.imgs)
