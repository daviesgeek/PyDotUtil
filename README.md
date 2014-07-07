PyDotUtil
=========

Simple Python script to manage DotFiles.

PyDotUtil symlinks everything in a `home` folder in the same directory as your install. I have only tested this on OS X, but there's no reason why it won't work on a Linux install. Feel free to submit pull request for cross-platform.

## Install

First, clone this repo: 
```bash
git clone git@github.com:daviesgeek/PyDotUtil.git <your destination folder>
```
Then create a `home` folder. Everything in this folder will by symlinked into your home directory.

To remove the symlinks, use the `-r/--remove` flag.
