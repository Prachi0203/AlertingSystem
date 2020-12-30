from cv2 import cv2
import winsound
import clx.xms
import requests

client = clx.xms.Client(service_plan_id='7cd0ec2b5cd64b9e838a70aabbe531e1', token='71469a83d0d84cc7965f120d57f04599')

create = clx.xms.api.MtBatchTextSmsCreate()
create.sender = '447537404817'
create.recipients = {'918882057962'}
create.body = 'This is a test message from your Sinch account'
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detector = cv2.CascadeClassifier("C:/Users/Prachi Bindal/Downloads/haarcascade_frontalface_default.xml")
counter = 0
while True:
    
    ret, img = cap.read()

    if ret:

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(gray, 1.1, 4)

        for face in faces:
            
            x, y, w, h = face
            
            if(face.any() and counter ==0):
                try:
                   batch = client.create_batch(create)
                except (requests.exceptions.RequestException, clx.xms.exceptions.ApiException) as ex:
                    print('Failed to communicate with XMS: %s' % str(ex))
                #sms ends here

            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
  
        cv2.imshow("Face", img)
        counter = 1
    
    key = cv2.waitKey(1)
    #sms starts here


    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()