import cv2
from PIL import Image
import numpy as np

import click

# input ( video  ) if image returns color average of image
# output otherwise output
# width
# if height, must choose between cutting the video and/or specify frame capture time (every 2s), otherwise image will be gigantic if every frame and will take a long time
# file ext

@click.command()
@click.argument('filepath', required=True)
@click.option('--out', help='Output file name. If not extension, defaults to --extension or JPEG if no extension is given.', default='output', required=False)
@click.option('--width', default=800, help='Width of the output file.')
# @click.option('--height', )
# @click.option('--extension')
def main(filepath, width, out):
    average = AverageFrameColor(filepath, width, out)
    

class AverageFrameColor:
    """
        Average color for specified frames and returns a representation of the data. 
    """
    def __init__(self, filepath, width, output):
        self.filepath = filepath
        self.width = width
        self.output = output
        print(filepath, width, output)

if __name__ == '__main__':
    main()

# fpath = 'got.mkv'

# video = cv2.VideoCapture(fpath)


# frame_count = 0
# colors = []
# print('Averaging ', fpath)
# while True:
#     try:
#         ret, frame = video.read()

#         r_sum, g_sum, b_sum = (0, 0, 0)
#         px_count = 0
        
#         if frame_count % 48 == 0:
#             print()
#             for _row in frame:
#                 for px in _row:
                    
#                     r, g, b = px
#                     r_sum += r
#                     g_sum += g
#                     b_sum += b
#                     px_count += 1

#             r_med = int(round(r_sum / px_count))
#             g_med = int(round(g_sum / px_count))
#             b_med = int(round(b_sum / px_count))
#             colors.append([r_med, g_med, b_med])
#         print('|', end='')

#         frame_count += 1
#     except KeyboardInterrupt:
#         break
#     except Exception as e:
#         print(e)
#         break

# width = 1920
# n_frames = len(colors)
# frames = []
# for color in colors:
#     frames.append([color]*width)
# im = np.array(frames).reshape(n_frames, width, 3)

# result = Image.fromarray(im.astype('uint8'))

# result.show()
# result.save(f'output.jpeg', 'JPEG')