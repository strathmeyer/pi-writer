from datetime import datetime

import os
import sys

FILE_STORE = '/Users/strathmeyer/Documents/writing/'

def new_file():
  return datetime.today().strftime('%Y%m%d_%H%M%S') + '.txt';


def latest_file():
  all_files = os.listdir(FILE_STORE)
  plain_files = list(filter(lambda x: os.path.isfile(os.path.join(FILE_STORE, x)), all_files))

  try:
    return plain_files[-1]
  except IndexError:
    return None


def main():
  filename = latest_file() or new_file()

  while True:
    path = os.path.join(FILE_STORE, filename)
    print("Writing to:", filename)

    with open(path, 'a') as f:
      while True:
        try:
          line = input()
        except EOFError:
          break
        f.write(line + '\n')
        f.flush()

    filename = new_file()


if __name__ == '__main__':
  main()
