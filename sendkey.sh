#!/bin/bash

win_id=`xdotool search --limit 1 --name $1`
xdotool key --window $win_id ${@:2}
