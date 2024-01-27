import time
import sys
import random
import string
import argparse
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import TerminalFormatter

def print_code_like_typing(file_path, lexer_name='python', delay=0.15, error_rate=19, error_delay=0.5):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        lexer = get_lexer_by_name(lexer_name)
        formatter = TerminalFormatter()

        for line in lines:
            colored_line = highlight(line, lexer, formatter)
            in_ansi_sequence = False
            for char in colored_line:
                if char == '\x1b':
                    in_ansi_sequence = True
                    sys.stdout.write(char)
                elif in_ansi_sequence:
                    sys.stdout.write(char)
                    if char == 'm':
                        in_ansi_sequence = False
                else:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(delay)

                    if random.randint(1, error_rate) == 1:
                        random_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
                        sys.stdout.write(random_char)
                        sys.stdout.flush()
                        time.sleep(error_delay)

                        sys.stdout.write('\b \b')
                        sys.stdout.flush()
                        time.sleep(delay)

    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simulate typing of a code file with optional typing errors.")
    parser.add_argument('file_path', type=str, help='Path to the code file to be typed out.')
    parser.add_argument('--lexer', type=str, default='python', help='Lexer name for syntax highlighting. Default is python.')
    parser.add_argument('--delay', type=float, default=0.15, help='Delay between character typings. Default is 0.15 seconds.')
    parser.add_argument('--error_rate', type=int, default=19, help='Error rate for simulating typing errors. Default is 19 (1 in 19 chance).')
    parser.add_argument('--error_delay', type=float, default=0.5, help='Delay after correcting a typing error. Default is 0.5 seconds.')

    args = parser.parse_args()

    print_code_like_typing(args.file_path, args.lexer, args.delay, args.error_rate, args.error_delay)

if __name__ == "__main__":
    main()
