import argparse
import re
import os
import sys
parser = argparse.ArgumentParser()

parser.add_argument("files", help='Files to convert', nargs='+')
parser.add_argument('-r', '--recursive', help='parse files recursive', action='store_true')

args = parser.parse_args()
files = list(args.files)
recursive = args.recursive

repl = [
    ('\*\*', '\t*'),
    ('\[\[File:.*\]\]\\n', ''),
    ('\'\'\'([\w\s\d,._\"\(\)\/+→&:-]*)\'\'\'', '**\\1**'),
    ('\'\'([\w\s\d,._\"\(\)\/+→&:-]*)\'\'', '*\\1*'),
    ('#', '#.'),
    ('\{\{Software header\|scope=section\|name=GNU Health\|version=3\.4\|type=>\}\}', '|version3.4|'),
    ('\{\{Software header\|scope=section\|name=GNU Health\|version=3\.0\|type=>\}\}', '|version3.0|'),
    ('\{\{stub.*', '|stub|'),
    ('\{\{Notice\|(.*)\}\}', '.. note:: \\1'),
    ('\(\(to be added\)\)', '|todo|')
]

headerreplace = [
    ('==== (.*) ====', '\\1', '"'),
    ('=== (.*) ===', '\\1', '^'),
    ('== (.*) ==', '\\1', '-')
]

def parse(files, recursive):
    for file in list(files):
        if not os.path.exists(file):
            print(file + ' does not exist',file=sys.stderr)

        if os.path.isdir(file):
            if recursive:
                parse([os.path.join(file, f) for f in os.listdir(file)], recursive)
            continue

        r_file = open(file, "r")

        w_n_file = ""
        l_line = ''
        for line in r_file:
            n_l = line
            for r in repl:
                match, replace = r
                n_l = re.sub(match, replace, n_l)

            for r in headerreplace:
                match, replace, header = r
                if(re.search(match, n_l)):
                    n_l = re.sub(match, replace, n_l)
                    n_l += header * (len(n_l) - 1)
                    n_l += '\n'
            
            l_n = n_l

            w_n_file += n_l

        w_file = open(file, "w")
        w_file.write(w_n_file)
        w_file.close()

for file in files:
    if not os.path.exists(file):
        print(file + ' does not exist',file=sys.stderr)
    elif not recursive and os.path.isdir(file):
        parse([os.path.join(file, f) for f in os.listdir(file)], recursive)
    else:
        parse([file], recursive)
        