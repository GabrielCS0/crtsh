import argparse

parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '-d', '--domain',
    help = 'The domain to search.',
    required = True
)
