# pi-writer

A minimal Python based app for writing first drafts without distraction.


# Use

When started, it opens the most recent file.
(Or if no previous file, it creates one.)

What you write is appended to the file when you hit Return.

Hit ^D by itself on a line to create a new file.

Filename based on timestamp.  YYYYMMDD_HHMMSS.txt


# Roadmap

## File names

- When creating a file, you type a name.
- Using the Open menu, you can select a file to open and append to.
- When started, it opens the previously opened file. (If none exist, sends you to the Open menu.)
- Top option on the Open menu is "New File…"
- Maybe: show the last few lines of text from the newly opened file

## Write on keypress

I'd like to be able to write every keypress to a file. Currently, you need to hit enter, which encourages a telegraph-like style of short lines.

Unfortunately, grabbing invdividual keystrokes probably involves using a library like curses, which is a big jump in complexity.


# Out of Scope

 - Allow editing the previous text in a file. Unlikely to happen, since a move to GNU nano would probably make more sense.
