from distutils.core import setup
from setuptools import setup

setup(name='jadukor',
      version='0.1',
      description='The most powerfull module in the universe',
      url='http://github.com/atmragib/jadukor',
      download_url='https://github.com/atmragib/jadukor/archive/v_01.tar.gz',
      author='A T M Ragib Raihan',
      author_email='atmragibraihan@gmail.com',
      license='MIT',
      packages=['jadukor'],
      keywords=['personal', 'handy', 'ragib', 'jadukor'],
      install_requires=[
          'validators',
          'beautifulsoup4',
      ],
      zip_safe=False,
      classifiers=[
          # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
          'Development Status :: 3 - Alpha',
          # Define that your audience are developers
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',   # Again, pick a license
          # Specify which pyhton versions that you want to support
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],)


setup(
)
