
import torch
from .model import SiameseNetwork
from PIL import Image
import PIL.ImageOps
import pkg_resources
import torchvision.transforms as transforms
import torch.nn.functional as F

def videoBarcodeSimilarities(image1_path: str, image2_path: str):
    model = SiameseNetwork()
    weight_path = pkg_resources.resource_filename(__name__, 'barimgsim.pt')
    # PATH = "barimgsim.pt"
    # weights = torch.hub.load_state_dict_from_url(
    #     "https://github.com/smilingprogrammer/RealTimeNudityDetectionAlgorithm/blob/main/barimgsim.pt", progress=True
    # )
    model.load_state_dict(torch.load(weight_path))
    model.eval()

    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Preprocess the images for ResNet50
    preprocess = transforms.Compose([
    transforms.Resize((100, 100)),
    transforms.ToTensor()
    ])

    image1 = preprocess(image1)
    image2 = preprocess(image2)

    # Add batch dimension to images
    image1 = image1.unsqueeze(0)
    image2 = image2.unsqueeze(0)
    output1, output2 = model(image1, image2)

    euclidean_distance = F.pairwise_distance(output1, output2)
    max_distance = torch.sqrt(torch.tensor(output1.shape[1], dtype=torch.float))
    similarity_score = 1.0 / (1.0 + euclidean_distance / max_distance)
    print(f'Similarity score between barImage1 and barImage2: {similarity_score.item()}')
