#TODO: not functional, but concept is understood. cread cmd line tool where user inputs a value and script prints it

#!/usr/bin/env python3
import argparse
import stat
from pathlib import Path


#def install_command():
#	script_path = Path(__file__).resolve()
#	bin_dir = Path("/home/emeka/CS-Compendium/MyProjects/rl-evobiodet/ideas")
#	command_path = bin_dir / script_path.name
#	bin_dir.mkdir(parents=True, exist_ok=True)
#
#	#if command_path.is_symlink():
#	#	if command_path.resolve() != script_path:
#	#		raise FileExistsError(f"Refusing to replace existing symlink: {command_path}")
#	#elif command_path.exists():
#	#	raise FileExistsError(f"Refusing to replace existing file: {command_path}")
#	#else:
#	#	command_path.symlink_to(script_path)
#
#	#script_path.chmod(script_path.stat().st_mode | stat.S_IXUSR)
#
#	#bashrc_path = Path.cwd() / ".bashrc"
#	#path_line = 'export PATH="$HOME/bin:$PATH"'
#	#try:
#	#	bashrc = bashrc_path.read_text()
#	#except FileNotFoundError:
#	#	bashrc = ""
#	#if path_line not in bashrc.splitlines():
#	#	with bashrc_path.open("a") as bashrc_file:
#	#		if bashrc and not bashrc.endswith("\n"):
#	#			bashrc_file.write("\n")
#	#		bashrc_file.write(path_line + "\n")
##
#	#print(f"Installed {command_path}. Open a new terminal or run: source ~/.bashrc")
#
#
#install_command()

# card drawing
parser = argparse.ArgumentParser(description="The number of cards selected from the deck")
parser.add_argument("-cards", help='cards selected from the deck')
args = parser.parse_args()
print("Cards Selected: " + args.cards + ".")
