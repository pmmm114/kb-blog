PRODUCT_FLAG = False

if PRODUCT_FLAG:
    from kbblog.settings.production_settings import *
else :
    from kbblog.settings.develop_settings import *