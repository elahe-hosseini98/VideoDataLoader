 ### A brief documentation ###


- **why did I design the video dataloader in this way?**<br />
in this design, we can directly load video files without preprocessing. It is easy to add any other required transform classes or customize dataset classes to change the way we're reading video files. another reason was that using Torch made the task a lot easier to code and handle.

- **What are the weaknesses of my video loader?**<br />
It requires a heavy code rewrite for any changes, which leads to dozens of hours wasted over the lifetime of a project. Second, it is merely a way to load data from disk, it doesn't support any data visualization or exploration that can help us construct better datasets.
