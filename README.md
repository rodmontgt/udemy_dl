Python script to download a udemy.com course, for personal offline use.

### Version
**0.2.2-alpha.2**

[![PyPI version](https://badge.fury.io/py/udemy-dl.svg?0.2.0)](http://badge.fury.io/py/udemy-dl) 
[![Build Status](https://travis-ci.org/nishad/udemy-dl.svg?branch=master)](https://travis-ci.org/nishad/udemy-dl)
[![Code Health](https://landscape.io/github/nishad/udemy-dl/master/landscape.svg?style=flat)](https://landscape.io/github/nishad/udemy-dl/master)
[![Waffle.io](https://img.shields.io/waffle/label/nishad/udemy-dl/in%20progress.svg)](https://waffle.io/nishad/udemy-dl)

### Windows Version
A Windows version without any dependecies is available here  
https://github.com/nishad/udemy-dl-windows

You can get the lastest Windows release from here.

https://github.com/nishad/udemy-dl-windows/releases/latest

Download `udemy-dl-win-X.X.X.zip`


### Prerequisites

* Python (2 or 3)
* `pip` (Python Install Packager)
* Python module `requests`
  * If missing, they will be automatically installed by `pip`


### Preinstall

If you don't have `pip` installed, look at their [install doc](http://pip.readthedocs.org/en/latest/installing.html).
Easy install (if you trust them) is to run their bootstrap installer directly by using:

    sudo curl https://bootstrap.pypa.io/get-pip.py | sudo python


### Install

`udemy-dl` can be installed using `pip`

    pip install udemy-dl

``or``

    python -m pip install udemy-dl

 In OS X and Linux you need to `sudo` installing `udemy-dl` or you may face some errors

```
sudo pip install udemy-dl
```

Also you need to `sudo` installing `pip` itself or you run into the same problem. 


### Update

`udemy-dl` can be updated using `pip`

    pip install --upgrade udemy-dl
 
 
``or``

    python -m pip install --upgrade udemy-dl
    
 In OS X and Linux you need to `sudo` upgrade `udemy-dl`
 
 ```
 sudo pip install --upgrade udemy-dl
 ```

### Usage

Simply call `udemy-dl` with the full URL to the course page.

    udemy-dl https://www.udemy.com/COURSE_NAME

``or``

    python -m udemy_dl https://www.udemy.com/COURSE_NAME

`udemy-dl` will ask for your udemy username (email address) and password then start downloading the videos.

By default, `udemy-dl` will create a subdirectory based on the course name.  If you wish to have the files downloaded to a specific location, use the `-o /path/to/directory/` parameter.

If you wish, you can include the username/email and password on the command line using the -u and -p parameters.

    udemy-dl -u user@domain.com -p $ecRe7w0rd https://www.udemy.com/COURSE_NAME
 
 If you don't want to download but save links to a file for later downloading with a different downloader
 
    python -m udemy_dl -s https://www.udemy.com/COURSE_NAME

For information about all available parameters, use the `--help` parameter

    udemy-dl --help


### Advanced Usage

```
usage: udemy-dl [-h] [-u USERNAME] [-p PASSWORD]
                [--lecture-start LECTURE_START] [--lecture-end LECTURE_END]
                [-o OUTPUT] [-d {aria2c,axel,httpie,curl}] [--use-ffmpeg]
                [-q VIDEO_QUALITY] [-s] [--safe-file-names] [-l] [--debug] [--use-course-title]
                [-v]
                link

Fetch all the lectures for a udemy course

positional arguments:
  link                  Link for udemy course

optional arguments:
  -h, --help            	show this help message and exit
  -u USERNAME, --username USERNAME
							Username / Email
  -p PASSWORD, --password PASSWORD
							Password
  --lecture-start LECTURE_START
							Lecture to start at (default is 1)
  --lecture-end LECTURE_END
							Lecture to end at (default is last)
  -o OUTPUT, --output OUTPUT
							Output directory / text file path (if saving links)
  -d {aria2c,axel,httpie,curl}, --external-downloader {aria2c,axel,httpie,curl}
							Download with external downloader [aria2c, axel,
							httpie, curl] (default is aria2c)
  --use-ffmpeg          	Download videos from m3u8/hls with ffmpeg
							(Recommended)
  -q VIDEO_QUALITY, --video-quality VIDEO_QUALITY
							Select video quality [default is 654321(highest)]
  -s, --save-links      	Do not download but save links to a file
  --safe-file-names     	Use safe cross-platform filenames
  -l, --list            	Just list all of the possible lectures and their ids
  --debug               	Enable debug mode
  --use-course-title	Use the course title for the parent folder name (WARNING: can make file path too long
  -v, --version         	Display the version of udemy-dl and exit
```


### Uninstall

`udemy-dl` can be uninstalled using `pip`

    sudo pip uninstall udemy-dl

You may uninstall the required `requests` module too but be aware that those might be required for other Python modules.
