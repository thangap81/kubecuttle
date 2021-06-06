=======
kubecuttle
=======


Installation
============

To install `kubecuttle` to your local environment::

    make install

Usage
=====

Once installed, simply call `kubecuttle` from the command line or add it to your
.bashrc file

Use the `-h` flag to get Options::

    $ kubecuttle -h
    usage: kubecuttle [-h] [-f FILEPATH] apply

    positional arguments:
      apply                 Apply a configuration to a resource by filename

    optional arguments:
      -h, --help            show this help message and exit
      -f FILEPATH, --filename FILEPATH
                            that contains the configuration to apply
  
Example
=======

Return of None explains the successfull deployment, in future considered to return the exact objects created, e.g. pod(s) created, deployment created etc::

    $ kubecuttle apply -f /tmp/nginx-deployment.yaml 
    None
    $

Any other issues realted to yaml file or resources will be returned as received from k8's client api
