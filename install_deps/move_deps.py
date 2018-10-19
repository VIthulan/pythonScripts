import os

for filename in os.listdir('/home/leapset/py-cache'):
    try:
        package_name = filename.split('.')[0].split('-')
        del package_name[-1]
        package_name = '-'.join(map(str, package_name))
        print package_name
        os.system('mkdir %s' % package_name)
        os.system('mv %s %s/' % (filename, package_name))
    except Exception as e:
        print 'ERROR: '
        print 'e'