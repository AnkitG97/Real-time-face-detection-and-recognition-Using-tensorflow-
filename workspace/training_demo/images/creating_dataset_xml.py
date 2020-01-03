
from yattag import Doc, indent
import cv2
import os
import glob
from PIL import Image
import cv2
import os, time
path="train"
folder=path

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user name end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    #img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    im_face=img.copy()

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2) 
        #print("xmin: "+ str(x) + " ymin: "+str(y)+" xmax: "+str(x+w)+" ymax: "+str(y+h)+" image dimensions: "+str(img.shape))    
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("train/" + str(face_id) + '.' + str(count) + ".jpg", im_face)
        cv2.imshow('image', img)






        image=str(face_id) + '.' + str(count) + ".jpg"
        #print(image)
        doc, tag, text = Doc().tagtext()
           
        cv_img = cv2.imread(image)    

        dirpath = os.getcwd()
        path=os.path.join(dirpath, image)
        
        
        name=image.split(".")
        name=name[0]
        #print(name)
        splt_char = "."
        temp = image.split(splt_char) 
        #print(imagePath[1])
        name_of_file = splt_char.join(temp[:2]), splt_char.join(temp[2:]) 
        name_of_file=name_of_file[0]
        #print(name_of_file)
        filename=image
        #print(name_of_file)
            
        dimensions=gray.shape
        xmin=str(x)
        ymin=str(y)
        xmax=str(x+w)
        ymax=str(y+h)
        width=dimensions[1]
        height=dimensions[0]

        truncated=0
        segmented=0
        difficult=0
        depth=1

        with tag('annotation'):
            with tag('folder'):
                text(folder)
            with tag('filename'):
                text(filename)
            with tag('path'):
                text(path)
            with tag('source'):
                with tag('database'):
                    text('Unknown')
            with tag('size'):
                with tag('width'):
                    text(width)
                with tag('height'):
                    text(height)
                with tag('depth'):
                    text(depth)
                with tag('segmented'):
                    text(segmented)
            with tag('object'):
                with tag('name'):
                    text(name)
                with tag('pose'):
                    text('Unspecified')
                with tag('truncated'):
                    text(truncated)
                with tag('difficult'):
                    text(difficult)
                with tag('bndbox'):
                    with tag('xmin'):
                        text(xmin)
                    with tag('ymin'):
                        text(ymin)
                    with tag('xmax'):
                        text(xmax)
                    with tag('ymax'):
                        text(ymax)

            
        result = indent(
            doc.getvalue(),
            indentation = ' '*4,
            newline = '\r\n'
        )
            
            
        f= open(('train/⁩'+name_of_file + '.xml'),"w+")
        f.write( result)
        del(doc)
        f.close()




            





    time.sleep(0.38)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 150: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


