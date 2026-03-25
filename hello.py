# hello.py - Read one symbol and pyramid length, then print a pyramid
# Run this file with: python3 hello.py

import random

MAX_LENGTH = 50

# ANSI colors (works in macOS Terminal/iTerm and most modern terminals)
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
PYRAMID_COLORS = [GREEN, CYAN, YELLOW, RED]


def main():
	while True:
		symbol = input(f"{CYAN}Enter a single character (or type 'exit'/'quit' to stop): {RESET}")
		if symbol.lower() in ("exit", "quit"):
			print(f"{GREEN}Goodbye!{RESET}")
			break
		if len(symbol) != 1:
			print(f"{RED}Invalid input. Please enter exactly one character.{RESET}")
			continue

		count_input = input(f"{CYAN}Enter pyramid length (1 to {MAX_LENGTH}): {RESET}")
		if count_input.lower() in ("exit", "quit"):
			print(f"{GREEN}Goodbye!{RESET}")
			break
		if not count_input.isdigit():
			print(f"{RED}Invalid length. Please enter a positive number.{RESET}")
			continue

		count = int(count_input)
		if count < 1 or count > MAX_LENGTH:
			print(f"{RED}Length must be between 1 and {MAX_LENGTH}.{RESET}")
			continue

		print(f"{YELLOW}Input symbol:{RESET} {symbol}")
		print(f"{YELLOW}Pyramid length:{RESET} {count}")
		print(f"{GREEN}Pyramid structure:{RESET}")

		for level in range(1, count + 1):
			row_symbols = " ".join(symbol for _ in range(level))
			line_color = random.choice(PYRAMID_COLORS)
			print(f"{line_color}{row_symbols.center((2 * count) - 1)}{RESET}")


if __name__ == "__main__":
	main()
