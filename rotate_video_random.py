import cv2
import random

next_rotation = {
    0: [cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_90_COUNTERCLOCKWISE, None],
    90: [cv2.ROTATE_180, None],
    180: [cv2.ROTATE_90_CLOCKWISE, cv2.ROTATE_90_COUNTERCLOCKWISE, None],
    -90: [cv2.ROTATE_180, None]
}

position_after_rotation = {
    cv2.ROTATE_90_COUNTERCLOCKWISE: 90,
    cv2.ROTATE_90_CLOCKWISE: -90,
    cv2.ROTATE_180: 180
}

def get_next_rotation(current_pos: int):
    next_angles = next_rotation.get(current_pos)
    next_angle = next_angles[random.randint(0, len(next_angles) - 1)]
    if next_angle is None:
        return None, 0
    else:
        return next_angle, position_after_rotation[next_angle]

def should_rotate(fps: int, avg_seconds: int) -> bool:
    no_frames = fps * avg_seconds;
    return random.random() < 1.0/no_frames;

def rotate_frame(frame, current_pos: int, fps: int, avg_seconds: int = 3):
    rotate: bool = should_rotate(fps, avg_seconds)
    if rotate:
        rot, next_pos = get_next_rotation(current_pos)
        if rot is None:
            return frame, 0
        else:
            print('Rotating Frame', rot)
            new_frame = cv2.rotate(frame, rot)
            return new_frame, next_pos
    else:
        return frame, 0

def rotate_video(input_file: str, output_file: str):
    video = cv2.VideoCapture(input_file)

    # Get the frame rate of the video
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Get the codec used to encode the video
    fourcc = int(video.get(cv2.CAP_PROP_FOURCC))

    # Get the dimensions of the video frames
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a VideoWriter object to write the reversed video
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, width))

    # Read the video frames in reverse order and write them to the output video
    current_pos = 0
    i = 0
    while video.isOpened():
        i += 1
        ret, frame = video.read()
        if not ret:
            break
        if i == 1:
            print(frame)
        # nframe, current_pos = rotate_frame(frame, current_pos, fps)
        nframe = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        out.write(nframe)
        cv2.imshow('Rotated Frame', nframe)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the resources
    video.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    import sys
    from sys import argv
    if len(argv) != 3:
        sys.exit(1)
    rotate_video(argv[1], argv[2])
