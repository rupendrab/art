from PIL import Image # , ImageSequence

FRAME_DURATION = 100

def create_gif(image1_name: str, image2_name: str, gif_name: str):
    # Load the two images
    image1 = Image.open(image1_name)
    image2 = Image.open(image2_name)

    # Define the duration (in milliseconds) for each frame

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

    # Save the frames as an animated GIF
    frames[0].save(
        gif_name, 
        save_all=True, 
        append_images=frames[1:], 
        optimize=False, 
        duration=FRAME_DURATION, 
        loop=2
    )

if __name__ == "__main__":
    import sys
    from sys import argv
    if len(argv) != 4:
        sys.exit(1)

    create_gif(argv[1], argv[2], argv[3])
