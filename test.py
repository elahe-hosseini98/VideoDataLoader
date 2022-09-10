import torchvision
import torch
import transforms
from datasets import VideoCaptionDataset

dataset = VideoCaptionDataset(
    "video-caption.csv",
    transform=torchvision.transforms.Compose([
        transforms.VideoFilePathToTensor(),
        transforms.SampleRandomFrames(num_frames=100)
    ])   
)

data_loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=True)
for videos, captions in data_loader:
    print(videos[0].size(), captions[0])

