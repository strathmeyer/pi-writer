from datetime import datetime

import curses
import curses.ascii
import os
import sys

FILE_STORE = '/Users/strathmeyer/Documents/writing/'

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


def desired_char(char):
  return curses.ascii.isprint(char) or \
    char == '\n'


def get_and_write(file, stdscr):
  cursor_pos = 0
  stdscr.move(1, 0)

  while True:
    chr_code = stdscr.getch(1, cursor_pos)

    try:
      char = chr(chr_code)
    except ValueError:
      continue

    if char == curses.ascii.ctrl('d'):
      stdscr.clear()
      return
    elif char == '\n':
      file.write(char)
      file.flush()
      cursor_pos = 0
      stdscr.move(1, 0)
      stdscr.clrtoeol()
    elif desired_char(char):
      stdscr.addstr(1, cursor_pos, char)
      file.write(char)
      file.flush()
      (_, width) = stdscr.getmaxyx()
      cursor_pos = min(cursor_pos + 1, width - 1)

    stdscr.refresh()


def main(stdscr):
  curses.curs_set(0)

  filename = latest_file() or new_file()

  try:
    while True:
      path = os.path.join(FILE_STORE, filename)
      stdscr.addstr(0, 0, "Writing to: " + filename)

      with open(path, 'a') as f:
        get_and_write(f, stdscr)

      filename = new_file()

  except KeyboardInterrupt:
    sys.exit(0)


if __name__ == '__main__':
  curses.wrapper(main)
