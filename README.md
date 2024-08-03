# Camera-Based Fitness Game

This project is an interactive fitness game that uses your computer's camera and pose detection to guide you through a series of exercises. It's a fun way to stay active and challenge yourself!

## Features

- Real-time pose detection using MediaPipe
- Random selection of exercises
- Score tracking
- Visual feedback on the camera feed

## Exercises

The game currently includes four exercises:
1. Lunges
2. Arms outstretched
3. Touch toes
4. Jumping jacks

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/fitness-game.git
   cd fitness-game
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the game by executing the Python script:

```
python main.py
```

- The game will access your camera and display the feed with pose detection overlays.
- Follow the instructions on the screen to perform the requested exercises.
- The game will cycle through 10 random exercises.
- Press 'q' to quit the game at any time.

## How It Works

The game uses MediaPipe's pose detection to track your body's key points. It then analyzes these points to determine if you're performing the requested exercise correctly. The game randomly selects exercises and keeps track of your score as you complete them.

## Customization

You can easily add new exercises or modify the existing ones by editing the detection functions in `main.py`. To add a new exercise:

1. Create a new detection function (e.g., `detect_new_exercise(landmarks)`)
2. Add the new exercise to the `exercises` list
3. Add a new condition in the main loop to check for the new exercise

## Contributing

Contributions to improve the game or add new features are welcome! Please feel free to submit a pull request or open an issue for discussion.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Acknowledgments

This project uses the MediaPipe library for pose detection, developed by Google.
