import cv2


def faceBox(net, frame, conf_threshold=0.7):
    frameDnn = frame.copy()
    frameHeight = frameDnn.shape[0]
    frameWidth = frameDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()


    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameDnn, (x1, y1), (x2, y2), (0, 255, 0), 1)
    return frameDnn, bboxes

faceProto = r"C:\Users\ELCOT\Downloads\Gender-and-Age-Detection-master\opencv_face_detector.pbtxt"
faceModel = r"C:\Users\ELCOT\Downloads\Gender-and-Age-Detection-master\opencv_face_detector_uint8.pb"

ageProto = r"C:\Users\ELCOT\Downloads\Gender-and-Age-Detection-master\age_deploy.prototxt"
ageModel = r"C:\Users\ELCOT\Downloads\Gender-and-Age-Detection-master\age_net.caffemodel"

genderProto = r"C:\Users\ELCOT\Downloads\Gender-and-Age-Detection-master\gender_deploy.prototxt"
genderModel = r"C:\Users\ELCOT\Downloads\Gender-and-Age-Detection-master\gender_net.caffemodel"


MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Male', 'Female']

# Load network
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)
faceNet = cv2.dnn.readNet(faceModel, faceProto)

# Open a video file or an image file or a camera stream
video = cv2.VideoCapture('4.mp4')

while True:
    ret, frame = video.read()

    frameFace, bboxes = faceBox(faceNet, frame)

    for bbox in bboxes:
        face = frame[bbox[1]:bbox[3],bbox[0]:bbox[2]]

        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]

        label = "{},{}".format(gender, age)
        cv2.rectangle(frameFace, (bbox[0], bbox[1]-30), (bbox[2], bbox[1]), (0, 255, 0), -1)
        cv2.putText(frameFace, label, (bbox[0], bbox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Age-Gender", frameFace)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()


faceNet=cv2.dnn.readNet(faceModel, faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = [('(0, 2)', '0-2'), ('2', '0-2'), ('3', '0-2'), ('(4, 6)', '4-6'), ('(8, 12)', '8-13'), ('13', '8-13'), ('22', '15-20'), ('(8, 23)','15-20'), ('23', '25-32'), ('(15, 20)', '15-20'), ('(25, 32)', '25-32'), ('(27, 32)', '25-32'), ('32', '25-32'), ('34', '25-32'), ('29', '25-32'), ('(38, 42)', '38-43'), ('35', '38-43'), ('36', '38-43'), ('42', '48-53'), ('45', '38-43'), ('(38, 43)', '38-43'), ('(38, 42)', '38-43'), ('(38, 48)', '48-53'), ('46', '48-53'), ('(48, 53)', '48-53'), ('55', '48-53'), ('56', '48-53'), ('(60, 100)', '60+'), ('57', '60+'), ('58', '60+')]
genderList = ['Male', 'Female']
padding=20

""" Face highliting """

def faceBox(faceNet, frames):
    frameHeight=frames.shape[0]
    frameWidth=frames.shape[1]
    blob=cv2.dnn.blobFromImage(frames, 1.0, (300,300), [104,117,123], swapRB=False)
    faceNet.setInput(blob)
    detection=faceNet.forward()
    bboxs=[]
    for i in range(detection.shape[2]):
        confidence=detection[0,0,i,2]
        if confidence>0.7:
            x1=int(detection[0,0,i,3]*frameWidth)
            y1=int(detection[0,0,i,4]*frameHeight)
            x2=int(detection[0,0,i,5]*frameWidth)
            y2=int(detection[0,0,i,6]*frameHeight)
            bboxs.append([x1,y1,x2,y2])
            cv2.rectangle(frames, (x1,y1),(x2,y2),(0,255,0), 1)
    return frames, bboxs

""" Video display """

def DisplayVid():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('testvideo', fourcc, 20.0, (640, 480))

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while (True):
        ret, frame = cap.read()
        frameFace, bboxes = faceBox(faceNet, frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)

        for bbox in bboxes:
            face = frame[bbox[1]:bbox[3], bbox[0]:bbox[2]]

            blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
            genderNet.setInput(blob)
            genderPreds = genderNet.forward()
            gender = genderList[genderPreds[0].argmax()]

            ageNet.setInput(blob)
            agePreds = ageNet.forward()
            age = ageList[agePreds[0].argmax()]

            label = "{},{}".format(gender, age)
            cv2.rectangle(frameFace, (bbox[0], bbox[1] - 30), (bbox[2], bbox[1]), (0, 255, 0), -1)
            cv2.putText(frameFace, label, (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2,
                        cv2.LINE_AA)
        cv2.imshow("Age-Gender", frameFace)
        k = cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if not (cap.isOpened()):
            print("Could not open video device")

    cap.release()
    out.release()
    cv2.destroyAllWindows()

DisplayVid()