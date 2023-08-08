import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ColorClip
from moviepy.video.fx import resize


# Function to resize a video to the target aspect ratio
def resize_video(input_path, output_path, target_width, target_height):
    video_clip = VideoFileClip(input_path)
    
    # Calculate the target height based on the target width and aspect ratio
    target_height = int(target_width * video_clip.h / video_clip.w)
    
    # Resize the video to the target dimensions
    #resized_clip = video_clip.fx(video_clip.resize, width=target_width, height=target_height)
    resized_clip = video_clip.fx(video_clip.resize, width=target_width, height=target_height)

    
    # Write the resized video to the output path
    resized_clip.write_videofile(output_path, codec="libx264")

# Folder containing the input videos
#input_folder = "C:\Users\Chinwendu Nweje\Documents\My Series\ATLA  NEW AVATAR\ATLA S1"
input_folder = r"C:\Users\Chinwendu Nweje\Documents\My Series\ATLA  NEW AVATAR\ATLA S1"


# Folder to save the resized videos
output_folder = r"C:\Users\Chinwendu Nweje\Documents\My Series\ATLA  NEW AVATAR\resized_atla_s1"

# Target aspect ratio (21:9)
target_width = 21
target_height = 9

# Loop through all video files in the input folder
import os
for filename in os.listdir(input_folder):
    if filename.endswith(".mp4"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Resize the video
        resize_video(input_path, output_path, target_width, target_height)
        print(f"Resized {filename} and saved to {output_path}")

print("All videos resized successfully.")
