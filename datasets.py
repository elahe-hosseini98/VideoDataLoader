from torch.utils.data import Dataset 
import pandas as pd

class VideoCaptionDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.dataframe = pd.read_csv(csv_file)
        self.transform = transform 
        
    def __getitem__(self, index):
        video = self.dataframe.iloc[index].path
        caption = self.dataframe.iloc[index].caption
        if self.transform:
            video = self.transform(video)
        return video, caption
        
    def __len__(self):
        return len(self.dataframe)
        
    

