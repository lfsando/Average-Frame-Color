Average Frame Color
====================

[![Average Frame Color](https://i.imgur.com/Xy3nqRH.jpg "Average Frame Color")](https://i.imgur.com/Xy3nqRH.jpg "Average Frame Color")

Usage:
```
python ./frames.py --help
>> Usage: frames.py [OPTIONS] FILEPATH

>> Options:
>>   --output TEXT     Output file name or relative path. If not extension,
>>                     defaults to --extension or JPEG if no extension is given.
>>   --width TEXT      Width of the output file. If none provided the width of
>>                     the image will be half the amount of frames calculated
>>   --extension TEXT  Output file extension.
>>   --ratio FLOAT     Get a frame every n seconds. Default=1.0
>>   --show TEXT       Show image after processing.
>>   --help            Show this message and exit.

```

Retrieve the average color of every frame from a video file and save it's representation to an image file.
You can input an image to retrieve it's average color.