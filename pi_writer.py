from datetime import datetime

import os
import pathlib
import sys

HOME = str(pathlib.Path.home())
FILE_STORE = os.path.join(HOME, 'Documents', 'writing')


def new_file():
  return datetime.today().strftime('%Y%m%d_%H%M%S') + '.txt';


def latest_file():
  all_files = os.listdir(FILE_STORE)
  no_directories = lambda x: os.path.isfile(os.path.join(FILE_STORE, x))
  plain_files = list(filter(no_directories, all_files))

  try:
    return plain_files[-1]
  except IndexError:
    return None


def main():
  if not os.path.exists(FILE_STORE):
      os.makedirs(FILE_STORE)

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
