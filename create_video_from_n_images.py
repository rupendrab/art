from typing import List
import imageio
from PIL import Image

def create_video(image_files: List[str], video_file: str):
    """
    Create a video by blending one image into another in succession
    """
    if image_files is None or len(image_files) == 0:
        print("At least two image files must be specified")

    current_image = Image.open(image_files[0])
    
    # Create a list to store the frames
    frames = []
    
    # Define the duration (in seconds) for each frame
    frame_duration = 0.1

    for next_image_file in image_files[1:]:
        next_image = Image.open(next_image_file)
        for alpha in range(255, -1, -5):
            # Create a new blank image with a transparent background
            new_image = Image.new("RGBA", current_image.size, (0, 0, 0, 0))

            # Blend the two images together using the alpha value
            blended_image = Image.blend(next_image.convert("RGBA"), current_image.convert("RGBA"), alpha / 255.0)

            # Paste the blended image onto the new blank image
            new_image.paste(blended_image, (0, 0), blended_image)

            # Append the new frame to the list
            frames.append(new_image)
        current_image = new_image

    ## Make the last image last 2 seconds
    for i in range(int(5/frame_duration)):
        frames.append(current_image)
    
    imageio.mimsave(video_file, frames, format="FFMPEG", fps=1 / frame_duration)

if __name__ == "__main__":
    import sys
    from sys import argv
    if len(argv) < 4:
        print("Usage: <Image File 1> <Image File 2> ... <Image File n> <Video Output File mp4>")
        sys.exit(1)

    create_video(argv[1:-1], argv[-1])
