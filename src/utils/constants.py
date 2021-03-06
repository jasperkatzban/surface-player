# motor config
MOTOR_NUM_STEPS_REVOLUTION = 200 # this changes depending on which step type is used
MOTOR_STEP_DELAY_MS = 15 # delay in ms between each motor step

# laser pin definition
GPIO_LASER = 14 # pin 8 (GPIO14) on raspberry pi 2B V1.1

# camera & cv macros
# vals when swapping red and blue
# in a dark room on a white object, detects the area outside of the bright center beam
min_hue, max_hue = 130, 180
min_sat, max_sat = 50, 255
min_val, max_val = 100, 255

# construct arrays of min and max values
from numpy import array 
THRESHOLD_LOWER = array([min_hue, min_sat, min_val])
THRESHOLD_UPPER = array([max_hue, max_sat, max_val])

POLYFIT_DEG = 5 # degree to fit polynomial to
LINE_RESOLUTION = 5 # polynomial line granularity
SIGMOID_N = 200
X_CROP_PX = 150 # crop pixels off of left and right of frame
MIN_CONTOUR_AREA = 0 # minimum area for valid detected contours in mask

# led control
NUM_LEDS = 33
LED_HUE_THRESHOLD_LOWER = 0.3
LED_HUE_THRESHOLD_UPPER = 0.7