__author__ = 'Mt Front'

import argparse
import csv
import os
import sys

doc = """
    This is a simple script created by Mt Front, 
    that converts Weread notes export to a csv, so it can be import to Notion into a table.
    *** Warning: This script has only been tested on MacOS ***

    Output table format in Notion:
    --------------------------------------------
    |Name   |Highlight            |Note          |No.               |
    |Chapter|Underlined highlights|Notes/thoughts|Index used to sort|
    --------------------------------------------

    Steps:
        1. In Weread, go into your notes, click "export/导出"
        2. Click "Copy to clipboard/复制到剪贴板”
        3. Paste the copied notes into a txt file.
        4. Run this script by typing 'weread.py [txt file path]', the script will create a csv file
        5. In Notion, create a table (can be either inline or entire page)
        6. Click the '...' on right top cornor of your table, chose "Merge with CSV"
        7. Wait for import to complete and refresh the notion page
        8. Click the '...'->sort, add an ascending sort on 'No.' (why does stupid notion import in random order?)
        9. Notion may convert your 'Note' column to 'Type'. Simply click on the header and change property type to 'Text'
        10. Remove default unsed fields like "tags"
"""
parser = argparse.ArgumentParser(description=doc, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument(dest="path", help="The path of input Weread note txt file")

args = parser.parse_args()
path = args.path
if not os.path.isfile(path):
    print('The path specified does not exist, make sure it is a txt file')
    sys.exit()

book = ""
author=""

with open(path, 'r', encoding = 'utf8') as weread:
    # skip title
    # weread.readline()
    lines = weread.readlines()
    # remove 5 lines, including book name, author, etc.
    book = lines[0].strip('\n')
    author = lines[1].strip('\n')
    lines = lines[4:]
    # for line in lines:
    #     if line == '\n':
    #         lines.remove(line)

notes = []
# notion import csv is in random sort (why?????), so we need index
# notion import same length rows (why???), thus the stupid placeholder ' '
prev_line = ''
idx = 0
for i,line in enumerate(lines):
    line = line.strip('\n')
    if line == '':
        prev_line = ''
        continue
    # chapter beginning, format '◆ chapter title'
    if line.startswith('◆'):
        title = line.strip('◆ ')
    # underlined highlight without note
    elif line.startswith('>>'):
        if prev_line:
            if not prev_line.startswith('>>'):
                notes[-1] = [line.strip('>> '), book, author, prev_line]
        else:
            notes.append([line.strip('>> '), book, author, ' '])
            idx += 1
        prev_line = line
    # review if any
    elif line.startswith('★'):
        notes.append([title, line, ' ', idx])
        idx += 1
        prev_line = line
    # highlight qith notes, format 'notes>highlight'
    else:
        if not prev_line:
            notes.append([' ', book, author, line])
            idx += 1
            prev_line = line
        elif prev_line.startswith('>>'):
            prev_line = prev_line + line
            notes[-1] = [prev_line.strip('>> '), book, author, notes[-1][2]]

# write to csv
with open(path[:path.index('txt')] + 'csv', 'w', newline='', encoding = 'utf8') as notion:
    writer = csv.writer(notion)
    # initialize headers
    # Highlight, Book title, Author, Note, Location
    writer.writerow(['Highlight', 'Title', 'Author', 'Note'])
    writer.writerows(notes)
