#!/bin/bash

THEMEDIR="$HOME/.config/awesome/themes/niceandclean"

killall -9 conky
conky -c "$THEMEDIR"/resolutions/default/conkyhr &
conky -c "$THEMEDIR"/resolutions/default/conkymin &
conky -c "$THEMEDIR"/resolutions/default/conkydate &
conky -c "$THEMEDIR"/resolutions/default/conkycals &
conky -c "$THEMEDIR"/resolutions/default/conkystats &
