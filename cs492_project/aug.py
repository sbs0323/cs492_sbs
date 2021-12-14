import cv2
import matplotlib.pyplot as plt
import os
import sys
import glob
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

im_dir = '../datasets/kama_insta/'
label_dir = '../datasets/kama_insta_label/'

im_format = '.jpg'
label_format = '.txt'
option = '_rot90ccw'
option2 = '_rot90cw'
option3 = '_flipLR'
option4 = '_flipUD'
FILES = glob.glob( str(ROOT / im_dir / '*.jpg'))

for FILE in FILES:
    # im_name = 'foodsample%d.jpg' %(i+1)
    im_name = FILE[len(im_dir):-4]
    im_tar_dir = im_dir + im_name + im_format
    imBGR = cv2.imread(str(ROOT / im_tar_dir))
    imRGB = cv2.cvtColor(imBGR, cv2.COLOR_BGR2RGB)
    imFlip1 = cv2.flip(imBGR, 1)  # LR
    imFlip2 = cv2.flip(imBGR, 0) # UD
    imRot90 = cv2.rotate(imBGR, cv2.ROTATE_90_COUNTERCLOCKWISE)
    imRotm90 = cv2.rotate(imBGR, cv2.ROTATE_90_CLOCKWISE)

    im_save_dir = '../datasets/aug/' + im_name + option + im_format
    im_save_dir2 = '../datasets/aug/' + im_name + option2 + im_format
    im_save_dir3 = '../datasets/aug/' + im_name + option3 + im_format
    im_save_dir4 = '../datasets/aug/' + im_name + option4 + im_format
    cv2.imwrite(str(ROOT / im_save_dir), imRot90)
    cv2.imwrite(str(ROOT / im_save_dir2), imRotm90)

    cv2.imwrite(str(ROOT / im_save_dir3), imFlip1)
    cv2.imwrite(str(ROOT / im_save_dir4), imFlip2)

    label_tar_dir = label_dir + im_name + label_format
    label_save_dir = '../datasets/aug_label/' + im_name + option + label_format
    label_save_dir2 = '../datasets/aug_label/' + im_name + option2 + label_format
    label_save_dir3 = '../datasets/aug_label/' + im_name + option3 + label_format
    label_save_dir4 = '../datasets/aug_label/' + im_name + option4 + label_format

    f1 = open(str(ROOT / label_tar_dir), 'r')
    f2 = open(str(ROOT / label_save_dir), 'w')
    f3 = open(str(ROOT / label_save_dir2), 'w')
    f4 = open(str(ROOT / label_save_dir3), 'w')
    f5 = open(str(ROOT / label_save_dir4), 'w')
    lines = f1.readlines()
    for line in lines:
        sp=line.split()
        sp[0] = sp[0]
        # if(sp[0]=='35'):
        #    print(im_name)
        sp[3], sp[4] = sp[4], sp[3]
        sp[1], sp[2] = sp[2], str((1 - float(sp[1])).__round__(6))
        f2.write(' '.join(sp)+'\n')

        sp2=line.split()
        sp2[0] = sp2[0]
        sp2[3], sp2[4] = sp2[4], sp2[3]
        sp2[1], sp2[2] = str((1 - float(sp2[2])).__round__(6)), sp2[1]
        f3.write(' '.join(sp2)+'\n')

        sp3 = line.split()
        sp3[0] = sp[0]
        sp3[1], sp3[2] = str((1 - float(sp3[1])).__round__(6)), sp3[2]
        f4.write(' '.join(sp3) + '\n')

        sp4 = line.split()
        sp4[0] = sp4[0]
        sp4[1], sp4[2] = sp4[1], str((1 - float(sp4[2])).__round__(6))
        f5.write(' '.join(sp4) + '\n')
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()

    # cv2.imwrite(str(ROOT / 'data/images/flip1/foodsample1.jpg'), imFlip1)
    # cv2.imwrite(str(ROOT / 'data/images/flip2/foodsample1.jpg'), imFlip2)

# plt.subplot(1,2,1)
# plt.imshow(imRGB)
#
# plt.subplot(1,2,2)
# plt.imshow(imRot90)

# plt.show()
# plt.pause(2222)