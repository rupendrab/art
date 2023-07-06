import cv2

# Open the video file
def invert_video(input_file: str, output_file: str):
    video = cv2.VideoCapture(input_file)

    # Get the frame rate of the video
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Get the codec used to encode the video
    fourcc = int(video.get(cv2.CAP_PROP_FOURCC))

    # Get the dimensions of the video frames
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a VideoWriter object to write the reversed video
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Read the video frames in reverse order and write them to the output video
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        out.write(frame[::-1, ::-1, :])

    # Release the resources
    video.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import sys
    from sys import argv
    if len(argv) != 3:
        sys.exit(1)
    invert_video(argv[1], argv[2])
