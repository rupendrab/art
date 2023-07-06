import imageio
from PIL import Image

def create_video(image1_file: str, image2_file: str, video_file: str):
    """
    Create a video by blending one image into another
    """
    # Load the two images
    image1 = Image.open(image1_file)
    image2 = Image.open(image2_file)

    # Define the duration (in seconds) for each frame
    frame_duration = 0.1

    # Create a list to store the frames
    frames = []

    # Iterate over a range of alpha values from 255 to 0 (fully opaque to fully transparent)
    for alpha in range(255, -1, -5):
        # Create a new blank image with a transparent background
        new_image = Image.new("RGBA", image1.size, (0, 0, 0, 0))

        # Blend the two images together using the alpha value
        blended_image = Image.blend(image1.convert("RGBA"), image2.convert("RGBA"), alpha / 255.0)

        # Paste the blended image onto the new blank image
        new_image.paste(blended_image, (0, 0), blended_image)

        # Append the new frame to the list
        frames.append(new_image)

    imageio.mimsave(video_file, frames, format="FFMPEG", fps=1 / frame_duration)

if __name__ == "__main__":
    import sys
    from sys import argv
    if len(argv) != 4:
        sys.exit(1)

    create_video(argv[1], argv[2], argv[3])
