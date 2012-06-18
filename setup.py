from distutils.core import setup

setup(
    name = 'django-sneak',
    version = '0.1',
    description = 'Sneak into in admin change list',
    author = 'Djaz Team',
    author_email = 'devweb@liberation.fr',
    packages = ['sneak'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
