import numpy as np

def fake_data_1():
    n_frames = 10
    array_size = (9, 9)
    moving_pixels_size = (3, 3)
    frames = []

    for frame_number in range(n_frames):
        frame = np.zeros(array_size)
        row_start = frame_number % (array_size[0] - moving_pixels_size[0] + 1)
        col_start = frame_number % (array_size[1] - moving_pixels_size[1] + 1)
        for i in range(moving_pixels_size[0]):
            for j in range(moving_pixels_size[1]):
                frame[row_start + i, col_start + j] = (i + j + frame_number) * 10  # Example intensity pattern
        
        frames.append(frame)

    fake_data_1 = np.array(frames)
    return fake_data_1

def fake_data_2():
    np.random.seed(0)  # For reproducible results
    time_points, height, width = 10, 100, 100
    image_stack = np.random.rand(time_points, height, width) * 100

    # Adding some "activity" to simulate calcium signals in certain regions
    image_stack[:, 20:40, 40:60] += np.linspace(0, 50, time_points)[:, None, None]

    fake_data_2 = image_stack.copy()

    return fake_data_2