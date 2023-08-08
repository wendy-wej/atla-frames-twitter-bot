import os
from moviepy.editor import *
from glob import glob
from PIL import Image

def resize_video(input_path, output_path, target_width, target_height):
    video_clip = VideoFileClip(input_path)
    
    # Calculate the target height based on the target width and aspect ratio
    target_height = int(target_width * video_clip.h / video_clip.w)
    
    # Resize the video to the target dimensions
    resized_clip = video_clip.resize(target_width, height=target_height)
    
    # Set the duration of the resized clip to match the original clip
    resized_clip = resized_clip.set_duration(video_clip.duration)
    
    # Write the resized video to the output path
    resized_clip.write_videofile(output_path, codec="libx264")

if __name__ == "__main__":
    input_folder = r"C:\Users\Chinwendu Nweje\Documents\My Series\ATLA  NEW AVATAR\ATLA S1"
    output_folder = r"C:\Users\Chinwendu Nweje\Documents\My Series\ATLA  NEW AVATAR\resized_atla_s1"
    target_width = 21
    target_height = 9

    # Get all video files in the input folder
    video_files = glob(os.path.join(input_folder, "*.mp4"))

    # Resize all of the videos
    for video_file in video_files:
        input_path = video_file
        output_path = os.path.join(output_folder, os.path.basename(video_file))
        
        resize_video(input_path, output_path, target_width, target_height)  # Provide both width and height
        print(f"Resized {video_file} and saved to {output_path}")

print("All videos resized successfully.")
