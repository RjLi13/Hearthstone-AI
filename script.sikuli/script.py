Settings.MoveMouseDelay = 0 

click(Region(97,29,1073,713))
while True:
    wait("1411538127457.png",120)
    r_width = 220
    
    for x in range(0, 9):
        r = Region(r_width, 690, 460, 58)
        r2 = Region(619,402,74,86) 
        dragDrop(r, r2)
        wait(2)
        r_width += 40

    r_width = 40    
    for x in range(0, 9):
        r = Region(r_width, 414, 605, 104)
        r2 = Region(578,110,126,125)
        dragDrop(r, r2)
        wait(2)
        r_width += 70

    r = Region(704,526,108,100)
    r2 = Region(581,127,124,108)
    dragDrop(r, r2)
    
    click(Region(967,342,97,34))
    try:
         wait("1411538127457.png",120)
         print "MY TURN! :D"
    except FindFailed:
         print "uh oh, turn didn't finish in 120 seconds"