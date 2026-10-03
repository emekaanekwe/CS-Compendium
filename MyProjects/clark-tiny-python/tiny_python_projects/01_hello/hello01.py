#! usr/var/bin/python3
# place script in a dir and make it runnable anywhere
"""
$cp <script> ~/<bin location>
$PATH=~/<bin location>:$PATH
"""
# check if worked
"""$which <script>"""

import argparse
# input what plans will be
parser = argparse.ArgumentParser(description="Plans within plans")
parser.add_argument("plans", help='what will be the plan')
args = parser.parse_args()
print("Plans within " + args.plans + ".")

