from datetime import datetime

import curses
import curses.ascii
import os
import pathlib
import sys

HOME = str(pathlib.Path.home())

if (os.path.exists(os.path.join(os.sep, 'mnt', 'usb'))):
  FILE_STORE = os.path.join(os.sep, 'mnt', 'usb', 'writing')
else:
  FILE_STORE = os.path.join(HOME, 'Documents', 'writing')


def new_file():
  return datetime.today().strftime('%Y%m%d_%H%M%S') + '.txt';


def latest_file():
  all_files = os.listdir(FILE_STORE)
  no_directories = lambda x: os.path.isfile(os.path.join(FILE_STORE, x))
  plain_files = sorted(list(filter(no_directories, all_files)))

  try:
    return plain_files[-1]
  except IndexError:
    return None


def desired_char(char):
  return curses.ascii.isprint(char) or \
    char == '\n'


class Cursor():
  # Curses uses Y, X syntax, so we will too.
  BASE_Y = 0
  BASE_X = 0

  def __init__(self, stdscr):
    self.stdscr = stdscr
    self.reset()

  def getch(self):
    return self.stdscr.getch(self.y, self.x)

  def increment(self):
    new_y = self.y
    new_x = self.x + 1

    (height, width) = self.stdscr.getmaxyx()

    if (new_x >= width):
      new_y = self.y + 1
      new_x = self.__class__.BASE_X

    if (new_y >= height - 1):
      self.reset()
    else:
      self.y = new_y
      self.x = new_x
      self.update()

  def reset(self):
    self.y = self.__class__.BASE_Y
    self.x = self.__class__.BASE_X
    self.update()

  def update(self):
    self.stdscr.move(self.y, self.x)

  def write(self, char):
    self.stdscr.addstr(self.y, self.x, char)


def get_and_write(file, stdscr):
  cursor = Cursor(stdscr)

  while True:
    chr_code = cursor.getch()

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
      cursor.reset()
      stdscr.clrtobot()
    elif desired_char(char):
      cursor.write(char)
      cursor.increment()
      file.write(char)
      file.flush()

    stdscr.refresh()


def main(stdscr):
  curses.curs_set(0)

  if not os.path.exists(FILE_STORE):
      os.makedirs(FILE_STORE)

  filename = latest_file() or new_file()

  info_bar = curses.newwin(1, curses.COLS, 0, 0)
  main_window = curses.newwin(curses.LINES - 1, curses.COLS, 1, 0)

  try:
    while True:
      path = os.path.join(FILE_STORE, filename)
      info_bar.addstr(0, 0, "Writing to: " + filename, curses.color_pair(3))
      info_bar.clrtobot()
      info_bar.refresh()

      with open(path, 'a') as f:
        get_and_write(f, main_window)

      filename = new_file()

  except KeyboardInterrupt:
    sys.exit(0)


if __name__ == '__main__':
  curses.wrapper(main)
