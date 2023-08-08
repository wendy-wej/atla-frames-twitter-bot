from moviepy.editor import VideoFileClip
import os

def resize_videos(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all video files in the input folder
    video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mkv', '.mov'))]

    for video_file in video_files:
        input_path = os.path.join(input_folder, video_file)
        output_path = os.path.join(output_folder, video_file)

        # Load the video clip
        video_clip = VideoFileClip(input_path)

        # Calculate new dimensions for the '21:9' aspect ratio
        new_width = int(video_clip.h * 21 / 9)
        new_size = (new_width, video_clip.h)

        # Resize the video clip
        resized_clip = video_clip.resize(new_size)

        # Write the resized clip to the output path
        resized_clip.write_videofile(output_path, codec="libx264")

        # Close the video clip objects
        video_clip.close()
        resized_clip.close()

        # Print a message indicating the file has been resized
        print(f"Resized: {video_file}")

if __name__ == "__main__":
    input_folder = r"C:\Users\Chinwendu Nweje\Documents\My Series\ATLA  NEW AVATAR\ATLA S1"
    output_folder = r"C:\Users\Chinwendu Nweje\Documents\My Series\ATLA  NEW AVATAR\resized_atla_s1"
    resize_videos(input_folder, output_folder)
