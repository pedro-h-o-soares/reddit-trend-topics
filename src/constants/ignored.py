import re

REMOVED_CHARS = ('-', '/', ',', '.', '!', '?', '(', ')', '"', "'", '&', '+', ':', '~', '^', '`', ';', '|', '\\', '[', ']', '{', '}', '#', '…', '%')
IGNORED_EMOJIS = re.compile("["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                        "]+", flags=re.UNICODE)
IGNORED_WORDS = ('', '-', '/', 'on', 'my', 'this', 'or', 'I', 'get', 'be', 'am', 'but', 'to', 'a', 'an', 'and', 'all', 'about', 'behind', 'bit', 'any', 'at')