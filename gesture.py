import cv2
import mediapipe as mp
from pydobot import Dobot

# Initialize Dobot Magician
port = 'COM3' 
dobot = Dobot(port=port)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

move_step = 10

object_grasped = False

def control_robot(gesture):
    global object_grasped
    
    if gesture == "Left":
        dobot.move_to(dobot.x - move_step, dobot.y, dobot.z)
    elif gesture == "Right":
        dobot.move_to(dobot.x + move_step, dobot.y, dobot.z)
    elif gesture == "Up":
        dobot.move_to(dobot.x, dobot.y + move_step, dobot.z)
    elif gesture == "Down":
        dobot.move_to(dobot.x, dobot.y - move_step, dobot.z)
    elif gesture == "Grab":
        if not object_grasped:
            dobot.grip(True)
            object_grasped = True
            print("Object Grasped!")
    elif gesture == "Release":
        if object_grasped:
            dobot.grip(False) 
            object_grasped = False
            print("Object Released!")

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)  # Flip horizontally for mirror effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            thumb_x = hand_landmarks.landmark[4].x
            index_finger_x = hand_landmarks.landmark[8].x
            palm=hand_landmarks.landmark[0].y
            up=hand_landmarks.landmark[20].y
           
            if thumb_x < index_finger_x:
                gesture = "Left"
            else:
                gesture = "Right"

            thumb_tip_y = hand_landmarks.landmark[4].y
            index_tip_y = hand_landmarks.landmark[8].y
            if thumb_tip_y < index_tip_y:
                gesture = "Grab"
            else:
                gesture = "Release"
            if up<palm :
                gesture="Up"
            else:
                gesture="Down"
            control_robot(gesture)
    
    cv2.imshow('Gesture Control', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
