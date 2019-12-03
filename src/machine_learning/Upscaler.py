import numpy as np
from PIL import Image
from ISR.models import RDN

def scaleWithSuperResolution(image):
    img = Image.open(image)
    lr_img = np.array(img)
    print('Loading weights...')
    rdn = RDN(arch_params={'C':6, 'D':20, 'G':64, 'G0':64, 'x':2})
    rdn.model.load_weights('weights/rdn-C6-D20-G64-G064-x2_ArtefactCancelling_epoch219.hdf5')
    print('Scaling first image')
    sr_img = rdn.predict(lr_img)
    newIMG = Image.fromarray(sr_img)
    newIMG.save('upscale_test/Test.jpeg')
    print('Done Scaling')




scaleWithSuperResolution('../../img/upscale_Test.jpg')