from django.apps import AppConfig
import sys, os

class FastbertConfig(AppConfig):
    name = 'fastbert'
    print("In App")
    ROOT_DIR = os.path.abspath("")
    print(ROOT_DIR)
    sys.path.append(os.path.join(ROOT_DIR, "./fastbert/Mask_RCNN-master"))
    print(sys.path);
    import violence
    ml = violence.MLmodel()