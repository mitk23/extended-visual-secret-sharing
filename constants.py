# constants
import numpy as np

# colors
WHITE = 255
BLACK = 0
THRESH = 127

# visual secret sharing bits
VSS_BITS = (
  (BLACK, BLACK, WHITE, WHITE),
  (WHITE, WHITE, BLACK, BLACK),
)
VSS_PATTERN = (
  (0, 0),
  (0, 1),
)

# extended visual secret sharing bits
EVSS_BITS = ((BLACK, BLACK, WHITE, WHITE), (BLACK, WHITE, BLACK, WHITE),
            (WHITE, WHITE, BLACK, BLACK), (BLACK, BLACK, BLACK, WHITE),
            (WHITE, BLACK, BLACK, BLACK), (BLACK, WHITE, WHITE, BLACK))
# evssBitsから各行を取ってきて基本行列を作るためのインデックス
EVSS_PATTERN = ((0, 1), (0, 2), (0, 3), (0, 4),
              (3, 0), (3, 5), (3, 3), (3, 4))


# error diffusion filter
FILTER_FLOYD_STEINBERG = (1/16) * np.array([
  [0, 0, 7],
  [3, 5, 1],
])

FILTER_JARVIS_JUDICE_NINKE = (1/48) * np.array([
  [0, 0, 0, 7, 5], 
  [3, 5, 7, 5, 3], 
  [1, 3, 5, 3, 1]
])
