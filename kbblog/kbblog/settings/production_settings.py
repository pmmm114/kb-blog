from kbblog.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# S3 config
DEFAULT_FILE_STORAGE = 'kbblog.storages.S3DefaultStorage'
# STATICFILES_STORAGE = 'kbblog.storages.S3StaticStorage'

AWS_REGION = 'us-east-2'
AWS_STORAGE_BUCKET_NAME = 'kb-blog-img'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (
    AWS_STORAGE_BUCKET_NAME, AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_DEFAULT_ACL = 'public-read'

# static url
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

# media url
MEDIA_ROOT = 'https://%s/' % (AWS_S3_CUSTOM_DOMAIN)
MEDIA_URL = 'media/'