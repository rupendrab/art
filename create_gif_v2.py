from typing import List
from PIL import Image

def create_gif(image_paths: List[str], gif_file: str):

    # Open and load all images
    images = []
    for path in image_paths:
        image = Image.open(path)
        images.append(image)

    # Define the duration (in milliseconds) for each frame
    frame_duration = 200

    # Create a list to store the frames
    frames = []

    # Iterate over each image
    for image in images:
        # Convert image to RGBA if necessary
        if image.mode != "RGBA":
            image = image.convert("RGBA")

        # Append the image as a frame
        for i in range(5):
            frames.append(image)

    # Save the frames as an animated GIF
    frames[0].save(gif_file, save_all=True, append_images=frames[1:], optimize=False, duration=frame_duration, loop=0)

if __name__ == "__main__":
    import sys
    from sys import argv
    if len(argv) < 4:
        print("Usage: <Image File 1> <Image File 2> ... <Image File n> <Gif output file (.gif)")
        sys.exit(1)
    create_gif(argv[1:-1], argv[-1])
