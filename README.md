PyDotUtil
=========

Simple Python script to manage DotFiles.

PyDotUtil symlinks everything in a `home` folder in the same directory as your install. I have only tested this on OS X, but there's no reason why it won't work on a Linux install. Feel free to submit pull request for cross-platform.

## Install

First, clone this repo: 
```bash
git clone git@github.com:daviesgeek/PyDotUtil.git <your destination folder>
```
Then create a `castle` folder. Your dot files are your castle, the same as [Homesick](https://github.com/technicalpickles/homesick) Everything in this folder will by symlinked into your home directory.

## Usage

```bash
PyDotUtil [-h] {config, link, unlink}
```

#### config

`-d, --dir` The directory that PyDotUtil will read from

#### link

Run without any options to link everything from the directory into your home folder

#### unlink

Run without any options to unlink everything from the directory into your home folder