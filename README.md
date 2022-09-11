 ### A brief documentation ###
 **dataset.py:** <br />
 There is a class named VideoCaptionDataset in this file that inherits Dataset class of torch lib. It helps us read path and caption from the .csv file and   aslo apply all the wanted transforms and preprocesses on any columns, in this case "path" col. 
 
 **trasnform.py:** <br />
 There are two classes in this file, VideoFilePathToTensor and  SampleRandomFrames. the first class, gives a path to a video and return a sequence of the frames, and the second one, gives a parameter named num_frames which indicates the number of random frames that we want to sample from each video. If this parameter is not set, the video will be returned with all its original frames.
 
 **test.py:** <br />
 This is a very simple code to test my custom dataLoader. I have prepared a dataset of 5 random short videos and uploaded them into /video folder. A .csv file (video-caption.csv) is also prepared in two cols (path to video file and caption). 
 - - - -

### My answers ###
- **Why did I design the video dataloader in this way?**<br />
In this design, we can directly load video files without preprocessing. It is easy to add any other required transform classes or customize dataset classes to change the way we're reading video files. Another reason was that using Torch made the task a lot easier to code and handle the process.

- **What are the weaknesses of my video loader?**<br />
It requires a heavy code rewrite for any changes, which leads to dozens of hours wasted over the lifetime of a project. Second, it is merely a way to load data from disk, it doesn't support any data visualization or exploration that can help us construct better datasets.
