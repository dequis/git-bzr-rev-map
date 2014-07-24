git-bzr-rev-map
===============

Generates a mapping of git revisions to bzr revisions, for use with git-remote-bzr

## Why

It's not my fault, don't look at me like that.

## Dependencies

 * git-remote-bzr (which already depends on python2 and bzrlib)
 * jinja2 for the html generator

## Usage

    cp git-bzr-rev-map ~/bin/
    chmod +x ~/bin/git-bzr-rev-map

    # go to the git-remote-bzr enabled repo

    git bzr-rev-map <remote name> <remote branch name> > mapping

The output has tab separated values (date, git commit, bzr revision, author)

## Fancy html output

First, edit the configuration at the top of `gen_html.py` if you're not me
(unlikely).

Then run:

    cat mapping | python gen_html.py > fancy.html

## Demo

[raw](http://bzr.dequis.org/revmap/raw.txt), [fancy](http://bzr.dequis.org/revmap/fancy.html)
