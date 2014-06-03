#!/bin/tcsh

# source this file to randomly change the colors of the prompt

set BLACK = "%{\033[30m%}"
set BLUE  = "%{\033[34m%}"
set GREEN  = "%{\033[32m%}"
set CYAN  = "%{\033[36m%}"
set RED  = "%{\033[31m%}"
set MAGENTA  = "%{\033[35m%}"
set PURPLE  = "%{\033[35m%}"
set YELLOW  = "%{\033[33m%}"
set LIGHT_GRAY  = "%{\033[37m%}"
# set DARK_GRAY  = "%B%{\033[30m%}$B"
set BOLD_BLUE  = "%B%{\033[34m%}%B"
set BOLD_GREEN  = "%B%{\033[32m%}%B"
set BOLD_CYAN  = "%B%{\033[36m%}%B"
set BOLD_RED  = "%B%{\033[31m%}%B"
set BOLD_PURPLE  = "%B%{\033[35m%}%B"
set BOLD_WHITE = "%B%{\033[37m%}%B"
set WHITE = "%{\033[37m%}"
set RESET  = "%{\033[m%}"

set random = `bash -c 'echo $RANDOM'`

if ( $random < 6000 ) then 
    set COLOR1 = "$BOLD_BLUE"
    set COLOR2 = "$RED"
    set COLOR3 = "$YELLOW"
    
else if ( $random < 10000 ) then
    set COLOR1 = "$GREEN"
    set COLOR2 = "$WHITE"
    set COLOR3 = "$RED"

else if ( $random < 16000 ) then
    set COLOR1 = "$GREEN"
    set COLOR2 = "$BOLD_WHITE"
    set COLOR3 = "$CYAN"
    
else if ( $random < 21000 ) then
    set COLOR1 = "$RED"
    set COLOR2 = "$CYAN"
    set COLOR3 = "$BOLD_PURPLE"

else if ( $random < 26000 ) then
    set COLOR1 = "$PURPLE"
    set COLOR2 = "$MAGENTA"
    set COLOR3 = "$BOLD_RED"
else
    set COLOR1 = "$LIGHT_GRAY"
    set COLOR2 = "$YELLOW"
    set COLOR3 = "$RESET"
        
endif

# export PS1="$COLOR1[$COLOR2 APRIL_FOOL:$COLOR1\W]$COLOR2$ $COLOR3"

set prompt = "${COLOR1}[${COLOR2}%m:${COLOR1}%~]${COLOR3} %# ${COLOR3}"
set prompt2 = "${COLOR3} > "

unset COLOR1
unset COLOR2
unset COLOR3

unset BLACK 
unset BLUE  
unset GREEN  
unset CYAN  
unset RED  
unset PURPLE  
unset BROWN  
unset LIGHT_GRAY  
unset DARK_GRAY  
unset BOLD_BLUE  
unset BOLD_GREEN  
unset BOLD_CYAN  
unset BOLD_RED  
unset BOLD_PURPLE  
unset YELLOW  
unset WHITE  
unset RESET  

