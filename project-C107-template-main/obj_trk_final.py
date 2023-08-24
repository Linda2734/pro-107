import cv2
import math

video = cv2.VideoCapture("footvolleyball.mp4")

# Load tracker 
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)

# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)

# center point of basket
p1 = 530
p2 = 300

xs = []
ys = []

print(bbox)

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])

    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)

    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

def goal_track(img, bbox):
    x, y,w, h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    # center point of ball
    bx = x+int(w/2)
    by = y+int(h/2)
    cv2.circle(img,(bx,by),2,(255,0,255),5)
    cv2.circle(img,(p1,p2),2,(255,0,255),5)
    distance = math.sqrt((bx-p1)**2+(by-p2)**2)
    if distance<= 20:
        cv2.putText(img,"goal",(200,200),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),2)

    

    
    xs.append(bx)
    ys.append(by)
    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]),2,(123,221,213),5)



    

while True:
    
    check, img = video.read()   

    # Update the tracker on the img and the bounding box
    success, bbox = tracker.update(img)

    if success:
        (xs)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    goal_track(img,bbox)

    cv2.imshow("result", img)
            
    key = cv2.waitKey(25)
    if key == 32:
        print("Stopped")
        break

video.release()
cv2.destroyALLwindows()