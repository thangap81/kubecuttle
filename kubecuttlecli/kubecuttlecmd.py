import os
import argparse
from kubecuttle import kubecuttle


def create_argparser():
    parser = argparse.ArgumentParser()  

    parser.add_argument(
        'apply',
        help='Apply a configuration to a resource by filename'
    )  
    parser.add_argument(
        '-f', '--filename',
        dest='filepath',
        help='that contains the configuration to apply'
    )

    # extend the parser arguments for other potential future development
    # parser.add_argument(
    #     '--dry-run',
    #     dest='dryrun',
    #     choices=[],
    #     help='If true, only print the object that would be sent, without sending it. Warning: --dry-run cannot accurately output the result of merging the local manifest and the server-side data. Use --server-dry-run to get the merged result instead'
    # )
    
    return parser


def main():
    parser = create_argparser()

    try:
        args = parser.parse_args()
        if (args.filepath == None):
            print('usage: \n kubecuttle -h')
            exit(-1)
    except argparse.ArgumentError as exc:
        print('Error parsing arguments.')
        parser.error(str(exc.message))
        exit(-1)
    try:
        kubecuttle.apply(filepath=args.filepath)
    except kubecuttle.FileNotFoundError:
        print('\npath or file do not exist(s), please check and provide a valid path of yaml file\n')
        exit(-1)

if __name__ == '__main__':
    main()
