"""An example of semantic segmentation.

The following command runs this script and saves a new image showing the
segmented pixels at the location specified by `output`:

```
python3 semantic_segmentation.py \
  --model ./deeplabv3_mnv2_pascal_quant_edgetpu.tflite \
  --input test_images/bird.bmp \
  --keep_aspect_ratio \
  --output result_images/seg_bird.jpg
```
"""

import argparse

import numpy as np
from PIL import Image

from pycoral.adapters import common
from pycoral.adapters import segment
from pycoral.utils.edgetpu import make_interpreter


def create_pascal_label_colormap():
  colormap = np.zeros((256, 3), dtype=int)
  indices = np.arange(256, dtype=int)

  for shift in reversed(range(8)):
    for channel in range(3):
      colormap[:, channel] |= ((indices >> channel) & 1) << shift
    indices >>= 3

  return colormap


def label_to_color_image(label):
  if label.ndim != 2:
    raise ValueError('Expect 2-D input label')

  colormap = create_pascal_label_colormap()

  if np.max(label) >= len(colormap):
    raise ValueError('label value too large.')

  return colormap[label]


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--model', required=True,
                      help='Path of the segmentation model.')
  parser.add_argument('--input', required=True,
                      help='File path of the input image.')
  parser.add_argument('--output', default='semantic_segmentation_result.jpg',
                      help='File path of the output image.')
  parser.add_argument('--keep_aspect_ratio', action='store_true', default=False,
                      help='keep the image aspect ratio when down-sampling the image by adding ')
  args = parser.parse_args()

  // TODO 

if __name__ == '__main__':
  main()
