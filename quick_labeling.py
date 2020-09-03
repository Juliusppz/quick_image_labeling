import sys
import os
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pynput import keyboard
import matplotlib as mpl
import shutil


def on_press(key):
    global key0
    if key == keyboard.Key.esc:
        key0 = -1
        return False  # stop keylogger
    if key == keyboard.Key.backspace or str(key) == "'+'":
        print('lol')
        key0 = -2
        return False
    if key.char is not None:
        key0 = int(key.char)
    elif hasattr(key, 'vk'):
        key0 = key.vk - 96
    return False


mpl.rcParams['toolbar'] = 'None'
global key0

source_dir = sys.argv[1]
source_dir = source_dir.replace("'", "")
num_classes = sys.argv[2]
for i in range(1, int(num_classes) + 1):
    if not os.path.exists(source_dir + "\\" + str(i)):
        os.mkdir(source_dir + "\\" + str(i))

move_history = deque(maxlen=100)
history_txt = "history.txt"
history_file = open(source_dir + "\\" + history_txt, 'a')

files = (file for file in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, file)))
files = list(files)
if history_txt in files:
    files.remove(history_txt)

i = 0
while True:
    file = files[i]
    img = mpimg.imread(source_dir + "\\" + file)
    # img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_LINEAR)
    imgplot = plt.imshow(img)
    plt.show(block=False)
    plt.axis('off')
    plt.pause(0.001)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    if key0 == -1:
        break
    if key0 == -2:
        last_move = move_history.pop()
        shutil.move(last_move[1], last_move[0])
        history_file.write('mv ' + last_move[1] + ' ' + last_move[0] + '\n')
        i -= 1
    elif key0 in list(range(1, 10)):
        shutil.move(source_dir + "\\" + file, source_dir + "\\" + str(key0) + "\\" + file)
        move_history.append((source_dir + "\\" + file, source_dir + "\\" + str(key0) + "\\" + file))
        history_file.write('mv ' + source_dir + "\\" + file + ' ' + source_dir + "\\" + str(key0) + "\\" + file + '\n')
        i += 1
        if i == len(files):
            break

history_file.close()
