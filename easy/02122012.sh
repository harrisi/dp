#/bin/bash

gshuf -n $1 /usr/share/dict/words | tr '\n' ' ' | sed 's/ $//' | pbcopy
