import torch
import random
import cv2

class VideoFilePathToTensor(object):
    def __init__(self):
        self.channels = 3
    
    def __call__(self, path):
        cap = cv2.VideoCapture(path)
        assert(cap.isOpened())
        
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        frames = torch.FloatTensor(num_frames, height, width, self.channels)
        
        for index in range(num_frames):
            cap.set(cv2.CAP_PROP_POS_FRAMES, index)
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
                frame = torch.from_numpy(frame)
                frames[index, :, :, :] = frame.float()
            else:
                break

        # normalizing the pixel values
        frames /= 255
        cap.release()
        return frames
    
class SampleRandomFrames(object):
    def __init__(self, num_frames=None):
        self.num_frames = num_frames
        
    def __call__(self, video):
       if  self.num_frames:
            L, H, W, C = video.size()
            assert(self.num_frames < L)
            
            random_frames = []
            for i in range(self.num_frames):
                n = random.randint(0, L-1)
                random_frames.append(n)
                
            # sorting the list of random frame number to not lose the video content
            random_frames.sort()
            
            resampled_video = torch.FloatTensor(self.num_frames, H, W, C)
            
            for i, num_frame in enumerate(random_frames):
                resampled_video[i, :, :, :] = video[num_frame, :, :, :]
            return resampled_video
        return video
        
        
        
        
        
