#!/usr/bin/python3
"""
Generate forward DNS A records from a list of hostnames.
Reads hostnames from a file and outputs DNS A records.
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description='Generate forward DNS A records from a list of hostnames',
        epilog='''
Examples:
  %(prog)s -f hostnames.txt -s 10.0.120 -o 3

  This will read hostnames from hostnames.txt and generate:
    hostname1 IN A 10.0.120.3
    hostname2 IN A 10.0.120.4
    ...

Default behavior (for backward compatibility):
  Reads from 'fr.3' file and generates 10.0.120.x addresses starting at .3
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        '-f', '--file',
        default='fr.3',
        help='Input file containing hostnames (one per line). Default: fr.3'
    )
    parser.add_argument(
        '-s', '--subnet',
        default='10.0.120',
        help='Subnet prefix for IP addresses. Default: 10.0.120'
    )
    parser.add_argument(
        '-o', '--offset',
        type=int,
        default=3,
        help='Starting IP offset. Default: 3'
    )

    args = parser.parse_args()

    try:
        with open(args.file, 'r') as f:
            for i, line in enumerate(f, start=0):
                hostname = line.strip()
                if hostname:  # Skip empty lines
                    ip_offset = args.offset + i
                    print('{} IN A {}.{}'.format(hostname, args.subnet, ip_offset))
    except FileNotFoundError:
        print('Error: File "{}" not found'.format(args.file), file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print('Error: {}'.format(e), file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
