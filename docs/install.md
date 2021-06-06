# Install kubecuttle

## installation prepration

```
pip3 install kubernetes json mkdocs

```

## noted issues

```
To avoid runing make install as root, please provide write access to the user to /Library/Python/3.x/site-packages/
you may encounter the error while executing make install and the path as well should be available from the error

Other noted issue is unable to find the kunernetes module though installed successfully in previous step

add this to your .bashrc and source it, to find the path where packages are installed 

export PYTHONPATH="/usr/local/lib/python3.8/site-packages"

To get the path try the below command.

$ python3 -m site
sys.path = [
    '/Users/prabhuthangaraj',
    '/usr/local/lib/python3.8/site-packages',
    '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python38.zip',
    '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8',
    '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload',
    '/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages',
    '/Library/Python/3.8/site-packages',
]
USER_BASE: '/Users/prabhuthangaraj/Library/Python/3.8' (doesn't exist)
USER_SITE: '/Users/prabhuthangaraj/Library/Python/3.8/lib/python/site-packages' (doesn't exist)
ENABLE_USER_SITE: True

```
