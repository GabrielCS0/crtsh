import argparse

parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '-d', '--domain',
    help = 'The domain to search.',
    required = True
)

parser.add_argument(
    '-o', '--output',
    help = 'Save the results to text file.',
    dest = 'output_file'
)
