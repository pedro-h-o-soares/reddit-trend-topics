from argparse import ArgumentParser, ArgumentTypeError, Namespace

def configure_parser() -> Namespace:
    parser = ArgumentParser(
        prog='Reddit Trend Topics',
        epilog='Requires a N value(default 10)'
    )

    parser.add_argument('-n', dest='n', action='store', default=10, help='Number of trend words')
    parser.add_argument('-l', '--limit', dest='limit', action='store', default=150, help='Max number of analysed comments')
    parser.add_argument('-s', '--subreddit', dest='subreddit', action='store', default='skincancer', help='Subreddit name without "r/"')

    return parser.parse_args()

def cast_arg(value: str, r_type: type=str) -> int | str:
    try:
        return r_type(value)
    except ValueError:
        raise ArgumentTypeError('Invalid argument passed')