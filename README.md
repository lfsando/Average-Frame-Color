Average Frame Color
====================

[![Average Frame Color](https://i.imgur.com/Xy3nqRH.jpg "Average Frame Color")](https://i.imgur.com/Xy3nqRH.jpg "Average Frame Color")

This tool retrieves the average color of every frame from a video file and saves a representation of those colors to an image file. You can also input an image to retrieve its average color.


Usage:
```
python ./frames.py --help
>> Usage: frames.py [OPTIONS] FILEPATH

>> Options:
>>   --output TEXT     Specify the output file name or relative path. If the file
>>                     does not have an extension, it defaults to the value
>>                     specified by `--extension` or to JPEG if no `--extension`
>>                     is provided.
>>   --width INTEGER   Set the width of the output file. If not provided, the width
>>                     will be half the number of frames calculated.
>>   --extension TEXT  Specify the output file extension (e.g., png, jpeg).
>>   --ratio FLOAT     Capture a frame every n seconds. Default: 1.0.
>>   --show TEXT       Display the generated image after processing.
>>   --help            Show this help message and exit.

```
