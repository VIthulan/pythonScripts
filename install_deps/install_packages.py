import os

install_list = [
    'https://files.pythonhosted.org/packages/63/09/1da37a51b232eaf9707919123b2413662e95edd50bace5353a548910eb9d/coloredlogs-10.0.tar.gz',
    'https://files.pythonhosted.org/packages/3c/75/77922d0e415f82dfe5c5e60c857a58d6914d37d5a48407db8b524e91088b/speedtest-cli-2.0.2.tar.gz',
    'https://files.pythonhosted.org/packages/68/01/b9943984447e7ea6f8948e90c1729b78161c2bb3eef908430638ec3f7296/scapy-2.4.0.tar.gz',
    'https://files.pythonhosted.org/packages/84/f4/5771e41fdf52aabebbadecc9381d11dea0fa34e4759b4071244fa094804c/docutils-0.14.tar.gz',
    'https://files.pythonhosted.org/packages/e5/21/795b7549397735e911b032f255cff5fb0de58f96da794274660bca4f58ef/jmespath-0.9.3.tar.gz',
    'https://files.pythonhosted.org/packages/a0/b0/a4e3241d2dee665fea11baec21389aec6886655cd4db7647ddf96c3fad15/python-dateutil-2.7.3.tar.gz',
    'https://files.pythonhosted.org/packages/16/7d/c091ee78ec3117a37f0ac8676bb412f013d42094dca6a4e9c93975c7863a/botocore-1.10.66.tar.gz',
    'https://files.pythonhosted.org/packages/1f/9e/7b2ff7e965fc654592269f2906ade1c7d705f1bf25b7d469fa153f7d19eb/futures-3.2.0.tar.gz',
    'https://files.pythonhosted.org/packages/9a/66/c6a5ae4dbbaf253bd662921b805e4972451a6d214d0dc9fb3300cb642320/s3transfer-0.1.13.tar.gz',
    'https://files.pythonhosted.org/packages/e7/58/6cde46663d9cec6e81a0ce4d05e8d2d174b8526b519c4afab03860f5fbe5/boto3-1.7.66.tar.gz',
    'https://files.pythonhosted.org/packages/95/d9/c3336b6b5711c3ab9d1d3a80f1a3e2afeb9d8c02a7166462f6cc96570897/click-6.7.tar.gz',
    'https://files.pythonhosted.org/packages/28/85/df04ec21c622728316b591c2852fd20a0e74324eeb6ca26f351844ba815f/websocket_client-0.48.0.tar.gz',
    'https://files.pythonhosted.org/packages/54/1f/782a5734931ddf2e1494e4cd615a51ff98e1879cbe9eecbdfeaf09aa75e9/requests-2.19.1.tar.gz',
    'https://files.pythonhosted.org/packages/64/61/079eb60459c44929e684fa7d9e2fdca403f67d64dd9dbac27296be2e0fab/configobj-5.0.6.tar.gz']

install_list2 = [
    'https://files.pythonhosted.org/packages/64/61/079eb60459c44929e684fa7d9e2fdca403f67d64dd9dbac27296be2e0fab/configobj-5.0.6.tar.gz']

for pack in install_list:
    try:
        # print 'Downloading %s' % pack
        package_name = pack.split('/')[-1].split('.')[0].split('-')
        del package_name[-1]
        package_name = '-'.join(map(str, package_name))
        # package_name_list
        print package_name
        os.system('mkdir %s' % package_name)
        os.system('wget %s -P %s/' % (pack, package_name))
    except Exception as e:
        print 'ERROR: '
        print 'e'
