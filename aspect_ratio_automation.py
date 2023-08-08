import os
import moviepy.editor as mpy

def resize_videos(folder_path, new_aspect_ratio):
  """Resizes all the videos in a folder and changes their aspect ratio to the specified value.

  Args:
    folder_path: The path to the folder containing the videos to resize.
    new_aspect_ratio: The new aspect ratio to set for the videos.
  """

  for video_file in os.listdir(folder_path):
    video = mpy.VideoFileClip(os.path.join(folder_path, video_file))
    video = video.resize(new_aspect_ratio)
    video.write_videofile(os.path.join(folder_path, video_file))

if __name__ == "__main__":
  #folder_path = "C:\Users\Chinwendu Nweje\Documents\My Series\ATLA  NEW AVATAR\ATLA S1"
  folder_path = r"C:\Users\Chinwendu Nweje\Documents\My Series\ATLA  NEW AVATAR\ATLA S1"
  #new_aspect_ratio = "21 9"
  new_aspect_ratio = "21 9"
  resize_videos(folder_path, new_aspect_ratio)
