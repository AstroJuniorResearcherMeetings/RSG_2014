#!/bin/bash

# source this file to randomly change the colors of the prompt

# $RANDOM returns a different random integer at each invocation.
# Nominal range: 0 - 32767 (signed 16-bit integer).
random=$RANDOM

BLACK="\[\033[0;30m\]"
BLUE="\[\033[0;34m\]"
GREEN="\[\033[0;32m\]"
CYAN="\[\033[0;36m\]"
RED="\[\033[0;31m\]"
PURPLE="\[\033[0;35m\]"
BROWN="\[\033[0;33m\]"
LIGHT_GRAY="\[\033[0;37m\]"
DARK_GRAY="\[\033[1;30m\]"
BOLD_BLUE="\[\033[1;34m\]"
BOLD_GREEN="\[\033[1;32m\]"
BOLD_CYAN="\[\033[1;36m\]"
BOLD_RED="\[\033[1;31m\]"
BOLD_PURPLE="\[\033[1;35m\]"
YELLOW="\[\033[1;33m\]"
WHITE="\[\033[1;37m\]"
RESET="\[\033[m\]"

if [ $random -lt 6000 ]; then
    COLOR1=$WHITE
    COLOR2=$WHITE
    COLOR3=$BROWN
    
elif [ $random -lt 10000 ]; then
    COLOR1=$BOLD_GREEN
    COLOR2=$WHITE
    COLOR3=$RED

elif [ $random -lt 16000 ]; then
    COLOR1=$GREEN
    COLOR2=$BOLD_GREEN
    COLOR3=$DARK_GRAY
    
elif [ $random -lt 21000 ]; then
    COLOR1=$BOLD_RED
    COLOR2=$CYAN
    COLOR3=$PURPLE    

elif [ $random -lt 26000 ]; then
    COLOR1=$PURPLE
    COLOR2=$BOLD_CYAN
    COLOR3=$RED    

else
    COLOR1=$LIGHT_GRAY
    COLOR2=$YELLOW
    COLOR3=$RESET    
fi
  
export PS1="${COLOR1}[${COLOR2}\h:${COLOR1}\W]${COLOR2}$ ${COLOR3}"
export PS2="$COLOR2> "



