from distutils.core import setup

setup(
    name='django-auditlog',
    version='0.4.3',
    packages=['auditlog', 'auditlog.migrations'],
    package_dir={'': 'src'},
    url='https://github.com/BCriswell/django-auditlog',
    license='MIT',
    author='Brian Criswell',
    description='Audit log app for Django',
    install_requires=[
        'Django>=1.8',
        'jsonfield>=2.0.1'
    ],
    zip_safe=False
)
