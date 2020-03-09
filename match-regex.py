import re
from colorama import Fore, Back, Style
import argparse
from colorama import init
import platform
if platform.system() == "Windows":
    init()


def main():
    args = parse_args()
    if args.files: # process all files
        for file_name in args.files:
            try:
                file = open(file_name, 'r', encoding='utf-8')
                line_num = 0
                for line in file:
                    line_num += 1
                    line = line.rstrip('\n')
                    match_string(args, line, file_name, line_num)
            except IOError as err:
                print(err)
            finally:
                file.close()
    else: # process stdin
        line = input('Enter string:')
        match_string(args, line, 'stdin', 1)


def match_string(args, line, file_name, line_num):
    match = re.search(args.regex, line)
    if match:
        start_pos_list = []
        matched_text_list = []
        pattern = re.compile(args.regex)
        for match1 in pattern.finditer(line):
            start_pos_list.append(match1.start())
            matched_text_list.append(match1.group())
        # prints '^' under the matching text
        if args.underscore:
            underscore_line = ''
            for i in range(len(line)):
                if i in start_pos_list:
                    underscore_line += '^'
                else:
                    underscore_line += ' '
            print(line)
            print(underscore_line)
        # highlight matching text
        if args.color:
            print(re.sub(r'(%s)' % args.regex, Fore.RED + r'\1' + Fore.RESET, line))
        # generate machine readable output
        if args.machine:
            for i in range(len(start_pos_list)):
                print(file_name + ':' + str(line_num) + ':' +
                      str(start_pos_list[i]) + ':' + matched_text_list[i])
        # print line
        if not args.underscore and not args.color and not args.machine:
            print(line)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--regex", required=True,
                        help="regular expression")
    parser.add_argument("-f", "--files", required=False,
                        nargs='+', help="file(s)")
    parser.add_argument("-u", "--underscore", action="store_true", required=False,
                        help="prints '^' under the matching text")
    parser.add_argument("-c", "--color", action="store_true", required=False,
                        help="highlight matching text")
    parser.add_argument("-m", "--machine", action="store_true", required=False,
                        help="generate machine readable output")
    return parser.parse_args()


if __name__ == "__main__":
    main()
