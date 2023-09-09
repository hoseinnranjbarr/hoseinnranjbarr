position = "right"
direction = "left"

for i in range (1,20,1):
    if position == "right":
        print ("right")
        position = "center"
        direction = "left"


    elif position == "center":
        print ("center")
        if direction == "left":
            position = "left"
        elif direction == "right":
            position = "right"

    elif position == "left":
        print ("left")
        position = "center"
        direction = "right"

