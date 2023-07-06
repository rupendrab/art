import cv2

def reverse_video(input_file: str, output_file: str):
    # Open the video file
    video = cv2.VideoCapture(input_file)

    # Get the total number of frames in the video
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Get the frame rate of the video
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Create a VideoWriter object to write the reversed video
    fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Read and write the video frames in reverse order
    for frame_no in range(total_frames-1, -1, -1):
        video.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = video.read()
        if not ret:
            break
        out.write(frame)

    # Release the resources
    video.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import sys
    from sys import argv
    if len(argv) != 3:
        sys.exit(1)
    reverse_video(argv[1], argv[2])
