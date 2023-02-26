#!/usr/bin/env python
import io

from setuptools import setup


requires = [
    'jmespath-community>=1.1.0',
    'Pygments>=2.14.0,<3.0',
    'urwid==2.1.2',
]


setup(
    name='jmespath-community-terminal',
    version='1.1.1',
    description='JMESPath Terminal',
    long_description=io.open('README.rst', encoding='utf-8').read(),
    author='James Saryerwinnie, Springcomp',
    author_email='js@jamesls.com, springcomp@users.noreply.github.com',
    url='https://github.com/jmespath-community/jmespath.terminal',
    scripts=['bin/jpterm'],
    py_modules=['jpterm'],
    install_requires=requires,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ),
)
