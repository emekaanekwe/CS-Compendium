#!/usr/bin/env python3
import argparse
import stat
from pathlib import Path


def install_command():
	script_path = Path(__file__).resolve()
	bin_dir = Path.home() / "bin"
	command_path = bin_dir / script_path.name
	bin_dir.mkdir(parents=True, exist_ok=True)

	if command_path.is_symlink():
		if command_path.resolve() != script_path:
			raise FileExistsError(f"Refusing to replace existing symlink: {command_path}")
	elif command_path.exists():
		raise FileExistsError(f"Refusing to replace existing file: {command_path}")
	else:
		command_path.symlink_to(script_path)

	script_path.chmod(script_path.stat().st_mode | stat.S_IXUSR)

	bashrc_path = Path.home() / ".bashrc"
	path_line = 'export PATH="$HOME/bin:$PATH"'
	try:
		bashrc = bashrc_path.read_text()
	except FileNotFoundError:
		bashrc = ""
	if path_line not in bashrc.splitlines():
		with bashrc_path.open("a") as bashrc_file:
			if bashrc and not bashrc.endswith("\n"):
				bashrc_file.write("\n")
			bashrc_file.write(path_line + "\n")

	print(f"Installed {command_path}. Open a new terminal or run: source ~/.bashrc")


install_command()

# Input what plans will be.
parser = argparse.ArgumentParser(description="Plans within plans")
parser.add_argument("plans", help='what the plan is within')
args = parser.parse_args()
print("Plans within " + args.plans + ".")
