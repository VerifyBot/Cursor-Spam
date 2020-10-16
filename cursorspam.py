import cv2

data = cv2.imread('bg.png')
C = cv2.imread('cursor.png', -1)
C = cv2.resize(C, None, fx = .2, fy = .2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Joe Mama', data)

is_down = False
DEFAULT = 15
tm = DEFAULT

def on_click(ev, x, y, flags, param):
  global is_down, tm

  tm -= 1

  if ev == cv2.EVENT_LBUTTONDOWN:
    is_down = True
  elif ev == cv2.EVENT_LBUTTONUP:
    is_down = False
  else:
    if is_down and tm <= 0:
      tm = DEFAULT
      y1, y2 = y - 2, y + C.shape[0] - 2
      x1, x2 = x - 25, x + C.shape[1] - 25

      alpha_s = C[:, :, 3] / 255.0
      alpha_l = 1.0 - alpha_s

      for c in range(0, 3):
        try:
          data[y1:y2, x1:x2, c] = (alpha_s * C[:, :, c] + alpha_l * data[y1:y2, x1:x2, c])
        except ValueError:
          pass


cv2.setMouseCallback('Joe Mama', on_click)

while True:
  cv2.imshow('Joe Mama', data)

  k = cv2.waitKey(20) & 0xFF

  if k == 27:
    break
