# easyTui

Very simple TUI module for python

## Capabilities
-Print title
using
```
import easyTui as tui
tui.title('Text Sample')

#Outputs
#=================
#-- Text Sample --
#=================
```
-Print label
using
```
import easyTui as tui
tui.label('Text Sample')

#Outputs
#  Text Sample
#-----------------
```
-Print score
using
```
import easyTui as tui
val = 5
tui.score('Text Sample', val)

#Outputs
# Text Sample :  5
# ----------------------
```
-Print updating score
using
```
import easyTui as tui
val = 5
tui.updatingScore('Text Sample', val, 1)

#Outputs val, wait for 1 second and \r
# Text Sample :  5
```
-Print Unordered list
using
```
import easyTui as tui
tui.ul(['Text Sample', '2 Sample', '3 Sample'])

#Outputs
#  - Text Sample
#  - 2 Sample
#  - 3 Sample
#------------------------
```
-Print Ordered list
using
```
import easyTui as tui
tui.ol(['Text Sample', '2 Sample', '3 Sample'])

#Outputs
#  [0] Text Sample
#  [1] 2 Sample
#  [2] 3 Sample
#------------------------
```
