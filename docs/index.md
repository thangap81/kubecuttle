# kubecuttle

alternative to kubectl using python kubernetes client



## Install on Local

Install on your local:

```
make install

```

See the [install](install.md) page for information on installation instructions.

## Usage

### Command line

Run `kubecuttle` at the command line to get a options:

```
$ kubecuttle
usage: kubecuttle [-h] [-f FILEPATH] apply
kubecuttle: error: the following arguments are required: apply
```

Run `kubecuttle -h` at the command line to get a options:

```
$ kubecuttle --help
usage: kubecuttle [-h] [-f FILEPATH] apply

positional arguments:
  apply                 Apply a configuration to a resource by filename

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filename FILEPATH
                        that contains the configuration to apply
```
