from moviepy.editor import VideoFileClip
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os
from functools import partial

def mask_image(img, mask_area):
    """ Mask the image at the specified area
    
    Args:
        img: image to be masked
        mask_area: a list a two tuples, representing the LB corner and RT corner
        of the area to be masked
    Returns:
        masked_img
    """
    mask_LB, mask_RT = mask_area
    ignore_mask_color = (0,0,0)
    masked_img = cv2.rectangle(img, mask_LB, mask_RT, ignore_mask_color, -1)
    return masked_img

def process(path_to_movie, mask_area, path_to_save):
    """ Process the video by blacking out the area specified

    Args:
        path_to_movie: where the movie is stored
        mask_area: a list a two tuples, representing the LB corner and RT corner
        of the area to be masked
        path_to_save: where the movie will be saved after being processed    
    """
    movie = VideoFileClip(path_to_movie)
    processed_movie = movie.fl_image(partial(mask_image, mask_area=mask_area))
    processed_movie.write_videofile(path_to_save, audio=True)

def test(path_to_movie, mask_area, time_stamp):
    """ Test the subtitle removal function on a single frame
    
    Args:
        path_to_movie: where the movie is stored
        mask_area: a list a two tuples, representing the LB corner and RT corner
        of the area to be masked
        time_stamp: the frame at that time stamp (in second) will be processed
    """
    movie = VideoFileClip(path_to_movie)
    print('Total number of frames in the movie is {}.'.format(movie.reader.nframes))
    frame = movie.get_frame(time_stamp)
    
    frame = mask_image(frame, mask_area)
    plt.imshow(frame)

if __name__ == '__main__':
    path_to_movie = "movie_name.extention"
    path_to_save = "movie_name_no_subtitle.extention"
    mask_area = [(x1,y1),(x2,y2)] # Left-Bottom: (x1,y1); Right-top: (x2,y2)
    process(path_to_movie, mask_area, path_to_save)
