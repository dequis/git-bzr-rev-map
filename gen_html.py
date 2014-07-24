# simple html generator for the revision mapping
# requires jinja2 because jinja2 is cool
# reads from stdin, writes to stdout

# configuration, change this if you're not me:
GIT_URL = "http://github.com/dequis/bitlbee/commit/%s"
BZR_URL = "http://code.bitlbee.org/lh/bitlbee/revision/%s"

import sys
from jinja2 import Environment, FileSystemLoader

def generator():
    for line in sys.stdin.readlines():
        yield line.strip("\n").split("\t")

def main():
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")

    print template.render(data=generator(), git_url=GIT_URL, bzr_url=BZR_URL)

if __name__ == "__main__":
    main()
