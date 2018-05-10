'''
Video capture sample.
Sample shows how VideoCapture class can be used to acquire video
frames from a camera of a movie file. Also the sample provides
an example of procedural video generation by an object, mimicking
the VideoCapture interface (see Chess class).

'create_capture' is a convinience function for capture creation,
falling back to procedural video in case of error.

Usage:
    video.py [--shotdir <shot path>] [source0] [source1] ...'
    sourceN is an
     - integer number for camera capture
     - name of video file
     - synth:<params> for procedural video
Synth examples:
    synth:bg=../cpp/lena.jpg:noise=0.1
    synth:class=chess:bg=../cpp/lena.jpg:noise=0.1:size=640x480
Keys:
    ESC    - exit
    SPACE  - save current frame to <shot path> directory
'''


