#!/usr/bin/env python3

# A quick app to help brew tea

import argparse
import sys
import time
import curses
import shutil

parser = argparse.ArgumentParser()
parser.add_argument("action", help="The action you want to take", type=str, choices=["instruct", "brew"])
parser.add_argument("-t", "--type", help="The type of tea to brew", type=str, choices=["white", "green", "oolong", "black", "rooibos", "herbal"], default="black")
args = parser.parse_args()

teas = {
	'white': (160, 3),
	'green': (175, 3),
	'oolong': (185, 3),
	'black': (200, 4),
	'pu-erh': (205, 3),
	'herbal': (212, 6),
}


def ring(times=3, sleepTime=1):
	for i in range(times):
		print('\a')
		time.sleep(sleepTime)

def brew(window):
	window.nodelay(1)

	totalSeconds = teas[args.type][1] * 60
	key = ''
	print('Starting brew timer for {} tea'.format(args.type))
	for second in range(totalSeconds):
		key = window.getch()
		if key == ord('q'): 
			sys.exit(0)

		width = shutil.get_terminal_size((200,200)).columns
		window.erase()
		window.addstr('{0:^{width}}'.format('Currently brewing {} tea\n'.format(args.type), width=width))
		window.addstr('{} of {} seconds elapsed\n'.format(second, totalSeconds))
		window.addstr('{0:^{width}}'.format("('q' to quit)", width=width))
		window.refresh()
		
		time.sleep(1)
	
	window.erase()
	window.refresh()

	width = shutil.get_terminal_size((200,200)).columns
	print('{0:^{width}}'.format('Brew complete!', width=width))
	print('{0:^{width}}'.format('~Enjoy \U0001f375~', width=width))
	ring()


if args.action == "instruct":
	print('Boil water to {} degrees and steep for {} minute(s).'.format(*teas[args.type]))
	sys.exit(0)

curses.wrapper(brew)
