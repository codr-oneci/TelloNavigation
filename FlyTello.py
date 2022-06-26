from djitellopy import Tello
import cv2
import time
width=320
height=240
startCounter=0

tello = Tello()

tello.connect()
#tello.takeoff()

#tello.move_left(20)
#tello.rotate_counter_clockwise(90)
#tello.move_forward(20)

#tello.land()

print(tello.get_battery())

tello.streamon()

while True:
    frame_read=tello.get_frame_read()
    myFrame=frame_read.frame
    #img=cv2.resize(myFrame,(width,height))
    img=myFrame
    #if startCounter==0:
        #tello.takeoff()
        #tello.move_left(20)
        #tello.rotate_clockwise(90)

    cv2.imshow("My Result", img)
    time.sleep(0.1)
    #tello.move_forward(20)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        tello.land()
        break

