import random
import time

import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils


def detect_lunge(landmarks):
    # Simple lunge detection (you may need to adjust these thresholds)
    left_knee = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
    right_knee = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]
    return abs(left_knee.y - right_knee.y) > 0.1


def detect_arms_outstretched(landmarks):
    # Detect if arms are outstretched
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    return (
        left_wrist.y < left_shoulder.y
        and right_wrist.y < right_shoulder.y
        and abs(left_wrist.x - left_shoulder.x) > 0.2
        and abs(right_wrist.x - right_shoulder.x) > 0.2
    )


def detect_touch_toes(landmarks):
    # Detect if touching toes
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
    right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]
    return left_wrist.y > left_ankle.y and right_wrist.y > right_ankle.y


def detect_jumping_jack(landmarks):
    # Detect jumping jack pose
    left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
    right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value]
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]

    # Check if arms are raised above shoulders and legs are spread
    arms_raised = (left_wrist.y < left_shoulder.y) and (
        right_wrist.y < right_shoulder.y
    )
    legs_spread = abs(left_ankle.x - right_ankle.x) > abs(
        left_shoulder.x - right_shoulder.x
    )
    return arms_raised and legs_spread


exercises = ["lunge", "arms outstretched", "touch toes", "jumping jacks"]
current_exercise = random.choice(exercises)
score = 0
exercise_count = 0

cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened() and exercise_count < 10:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the BGR image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # Draw pose landmarks
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
        )

        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark

            # Check for current exercise
            if current_exercise == "lunge" and detect_lunge(landmarks):
                score += 1
                exercise_count += 1
                current_exercise = random.choice(exercises)
            elif current_exercise == "arms outstretched" and detect_arms_outstretched(
                landmarks
            ):
                score += 1
                exercise_count += 1
                current_exercise = random.choice(exercises)
            elif current_exercise == "touch toes" and detect_touch_toes(landmarks):
                score += 1
                exercise_count += 1
                current_exercise = random.choice(exercises)
            elif current_exercise == "jumping jacks" and detect_jumping_jack(landmarks):
                score += 1
                exercise_count += 1
                current_exercise = random.choice(exercises)

        # Display exercise and score
        cv2.putText(
            frame,
            f"Do: {current_exercise}",
            (10, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )
        cv2.putText(
            frame,
            f"Score: {score}",
            (10, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )
        cv2.putText(
            frame,
            f"Exercises: {exercise_count}/10",
            (10, 150),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

        cv2.imshow("Fitness Game", frame)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()

print(f"Game Over! Final Score: {score}/10")
