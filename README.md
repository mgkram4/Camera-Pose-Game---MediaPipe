# MediaPipe-Camera-Pose-Game
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
python fitness_game.py
```

- The game will access your camera and display the feed with pose detection overlays.
- Follow the instructions on the screen to perform the requested exercises.
- The game will cycle through 10 random exercises.
- Press 'q' to quit the game at any time.

## Customization

You can easily add new exercises or modify the existing ones by editing the detection functions in the script.

## Contributing

Contributions to improve the game or add new features are welcome! Please feel free to submit a pull request or open an issue for discussion.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Acknowledgments

This project uses the MediaPipe library for pose detection, developed by Google.
