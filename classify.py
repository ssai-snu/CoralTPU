"""A demo which runs object classification on camera frames.

Run default object detection:
python3 classify.py

Run ImageNet model:
python3 classify.py \
  --model ./all_models/mobilenet_v2_1.0_224_quant_edgetpu.tflite \
  --labels ./all_models/imagenet_labels.txt
"""

import argparse
import gstreamer
import os
import time

from common import avg_fps_counter, SVG
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter
from pycoral.utils.edgetpu import run_inference
from pycoral.adapters.common import input_size
from pycoral.adapters.classify import get_classes

def generate_svg(size, text_lines):
    svg = SVG(size)
    for y, line in enumerate(text_lines, start=1):
      svg.add_text(10, y * 20, line, 20)
    return svg.finish()

def main():
    default_model_dir = './all_models'
    default_model = 'mobilenet_v2_1.0_224_quant_edgetpu.tflite'
    default_labels = 'imagenet_labels.txt'
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='.tflite model path',
                        default=os.path.join(default_model_dir,default_model))
    parser.add_argument('--labels', help='label file path',
                        default=os.path.join(default_model_dir, default_labels))
    parser.add_argument('--top_k', type=int, default=3,
                        help='number of categories with highest score to display')
    parser.add_argument('--threshold', type=float, default=0.1,
                        help='classifier score threshold')
    parser.add_argument('--videosrc', help='Which video source to use. ',
                        default='/dev/video0')
    parser.add_argument('--videofmt', help='Input video format.',
                        default='raw',
                        choices=['raw', 'h264', 'jpeg'])
    args = parser.parse_args()

    print('Loading {} with {} labels.'.format(args.model, args.labels))

    // TODO 

if __name__ == '__main__':
    main()
