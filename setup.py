#!/usr/bin/env python
#coding=utf-8
import codecs
import os
import sys
try:
    from setuptools import setup,find_packages
except:
    from distutils.core import setup
'''import the setup lib'''


'''
    定义一个read方法，用来读取目录下的长描述
    我们一般是将README文件中的内容读取出来作为长描述，这个会在PyPI中你这个包的页面上展现出来，
    你也可以不用这个方法，自己手动写内容即可，
    PyPI上支持.rst格式的文件。暂不支持.md格式的文件，<BR>.rst文件PyPI会自动把它转为HTML形式显示在你包的信息页面上。
'''
def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()
NAME = "FriedRing"
'''
名字，一般放你包的名字即可
'''
PACKAGES = find_packages(include=[
        "FriedRing", "FriedRing.*"
    ])
'''
包含的包，可以多个，这是一个列表
'''
DESCRIPTION = "this is a FriedRing package for get http request and response."
'''
关于这个包的描述
'''
LONG_DESCRIPTION = read("README.md")
'''
参见read方法说明
'''
KEYWORDS = "FriedRing python package"
'''
关于当前包的一些关键字，方便PyPI进行分类。
'''
AUTHOR = "CrissChan"

AUTHOR_EMAIL = "can101208@gmail.com"
'''
作者的邮件地址
'''
URL = "http://blog.csdn.net/crisschan"
'''
你这个包的项目地址，如果有，给一个吧，没有你直接填写在PyPI你这个包的地址也是可以的
'''
VERSION = "1.0.6"
'''
当前包的版本，这个按你自己需要的版本控制方式来
'''
LICENSE = "MIT"
'''
授权方式，我喜欢的是MIT的方式，你可以换成其他方式
'''
REQUIREMENTS = [i.strip() for i in open("requirement.txt").readlines()]

'''
this grabs the requirements from requirements.txt
'''
setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    install_requires=REQUIREMENTS,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Testing"
    ],

    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': [
            "fr = FriedRing.fr:main"
        ]
    },
    # scripts=["scripts/test.py"],scripts表示将该文件放到 Python的Scripts目录下，可以直接用
)
## 把上面的变量填入了一个setup()中即可。