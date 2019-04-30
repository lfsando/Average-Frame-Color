import os
import cv2
import numpy as np
from PIL import Image

import click

# input ( video  ) if image returns color average of image
# output otherwise output
# width
# if height, must choose between cutting the video and/or specify frame capture time (every 2s), otherwise image will be gigantic if every frame and will take a long time
# file ext

video_exts = [
    'avi',
    'mp4',
    'mkv'
]

image_exts = [
    'bmp',
    'jpeg',
    'jpg',
    'png'
]


@click.command()
@click.argument('filepath', required=True)
@click.option('--output', help='Output file name or relative path. If not extension, defaults to --extension or JPEG if no extension is given.', required=False)
@click.option('--width', default=800, help='Width of the output file.')
@click.option('--extension', help='Output file extension.', required=False)
@click.option('--show', default=True, help='Show image after processing.', required=False)
def main(filepath, width, output, extension, show):
    average = AverageFrameColor(filepath, width, output, extension, show)
    average.check_arguments()

    if average.is_video:
        average.video_average()
    else:
        average.image_average()
    

class AverageFrameColor:
    """
        Average color for specified frames, returns a representation of the data. 
    """
    def __init__(self, filepath, width, output, extension, show):
        self.filepath = filepath
        self.width = width
        self.output = output
        self.extension = extension
        self.is_video = False

        # every n seconds get a frame
        self.seconds_ratio = 2

        self.show = show

    
    def check_arguments(self):
        # check if file exists
        exists = os.path.exists(self.filepath)
        if not exists:
            click.echo('Error: File does not exists.')
            sys.exit(-1)
        
        # Input file
        filename = os.path.basename(self.filepath)
        fname, fext = '.'.join(filename.split('.')[:-1]), filename.split('.')[-1]
        if fext not in video_exts and fext not in image_exts:
            click.echo('Error: Input file extension not supported.')
            sys.exit(-1)
        else:
            if fext in video_exts:
                self.is_video = True

        self.filepath = os.path.abspath(self.filepath)

        # Output file and Extension
        if not self.output:
            self.output = fname + '.jpeg'
        outfilename = os.path.basename(self.output)
        outpath = os.path.abspath(self.output)
        outname, outext = '.'.join(outfilename.split('.')[:-1]), outfilename.split('.')[-1]

        
        if os.path.exists(outpath):  
            if input(f"You will overwrite {outpath}. Do you wish to continue [Y/N]?\n").lower() in ['y', 'yes']:
                pass
            else:
                click.echo('Exiting...')
                sys.exit(0)

        # Warn if user inputs two different extensions for outext and self.extension
        if self.extension != outext and self.extension:
            click.echo('Warning: Output extensions are different between --extension option and --output option')

        if self.extension:
            outext = self.extension
        else:
            self.extension = outext
        if self.extension.lower() == 'jpg':
            self.extension = 'jpeg'    
        if self.extension not in image_exts:
            click.echo('Error: Output file extension not supported.')
            sys.exit(-1)

        # Check width
        if self.width < 1:
            click.echo('Error: Output width must be 1 or more pixels.')
            sys.exit(-1)

        # check ifoutput directory exists else create one
        outdir = os.path.dirname(outpath)
        if not os.path.exists(outdir):
            click.echo(f"Creating new directory at {outdir}")
            os.makedirs(outdir)        
        self.output = os.path.join(outpath)

    def image_average(self):
        im = Image.open(self.filepath)
        im_data = np.array(im)
        average_color = self.frame_average(im_data)


        output_data = []

        for i in range(self.width):
            output_data.append([average_color] * self.width)
        
        output_data = np.array(output_data)
        output = self.save_output(output_data, self.output, self.extension.upper())
        
        if self.show:
            output.show()
        click.echo('Average Color: ' + ' '.join(str(c) for c in average_color))

    def video_average(self):
        video = cv2.VideoCapture(self.filepath)
        framerate = round(video.get(cv2.CAP_PROP_FPS)) * self.seconds_ratio
        
        colors = []
        i = 0
        ret = True
        while ret:
            try:
                ret, frame = video.read()
                if i % framerate == 0:
                    print("Frame:", i, "\tSeconds:", i / (framerate/self.seconds_ratio))
                    colors.append(self.frame_average(frame))
                
            except KeyboardInterrupt:
                if input('Cancelling... Wish to save what you got so far?\n').lower() in ['yes', 'y']:
                    break
                sys.exit()
                
            # except TypeError as e:
                
            i += 1
        
        n_frames = len(colors)
        frames = []
        for color in colors:
            frames.append([color]*self.width)
        frames = np.array(frames).reshape(n_frames, self.width, 3)
        output = self.save_output(frames, self.output, self.extension)
        output.show()
    
    @staticmethod
    def frame_average(frame):
        n_pixels = frame.shape[0] * frame.shape[1]
        colors = [
            frame[:, :, 0].sum(),
            frame[:, :, 1].sum(),
            frame[:, :, 2].sum()
            ]
        colors = np.array(colors)
        average_color = np.round(colors / n_pixels).astype(int)
        return average_color

    @staticmethod
    def save_output(data, output_path, format):
        im = Image.fromarray(data.astype('uint8'))
        im.save(output_path, format)
        return im


if __name__ == '__main__':
    main()