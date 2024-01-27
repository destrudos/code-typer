# Code Typing Simulator

## Description
This Python script simulates the process of typing code in a terminal. It not only displays the code as if it is being typed in real-time but also includes color syntax highlighting and simulated typing errors. The update now allows for command-line argument input, making the script more versatile and customizable to various programming languages and typing specifications.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Command-Line Arguments](#command-line-arguments)
- [Example](#example)
- [License](#license)

## Installation
Ensure you have Python installed along with the Pygments library for syntax highlighting. Install Pygments using the following command:

```bash
pip install pygments
```

## Usage
Run the script from the command line, providing the path to the code file you want to display. You can also customize the behavior using various command-line arguments.

\```bash
python path_to_script.py path_to_code_file --lexer [lexer_name] --delay [delay_time] --error_rate [error_rate] --error_delay [error_delay]
\```

## Features
- Real-time typing simulation of code.
- Color syntax highlighting for readability.
- Simulated typing errors and corrections for a realistic coding experience.

## Command-Line Arguments
- `file_path`: Path to the code file to be typed out.
- `--lexer`: Lexer name for syntax highlighting. Default is Python.
- `--delay`: Delay between character typings. Default is 0.15 seconds.
- `--error_rate`: Error rate for simulating typing errors. Default is 19 (1 in 19 chance).
- `--error_delay`: Delay after correcting a typing error. Default is 0.5 seconds.

## Example
Here's how you might use the script with custom arguments:

```bash
python print_code_like_typing.py my_script.py --lexer python --delay 0.1 --error_rate 10 --error_delay 0.3
```

## License
This script is released under the MIT License.

---

