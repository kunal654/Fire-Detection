

# Fire Detection with YOLOv8

This project utilizes YOLOv8, an ultralytics implementation based on YOLOv3, for detecting flames in images or videos. The goal is to accurately identify flames and evaluate their height in order to assess the intensity or severity of a fire.

## Requirements

- Python 3
- OpenCV (`pip install opencv-python`)
- YOLOv8 (`pip install git+https://github.com/ultralytics/yolov8`)

## Installation and Setup

1. **Clone the Repository:**

   Begin by cloning the project repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/fire-detection.git
   ```

2. **Install Dependencies:**

   Navigate to the project directory and install the required Python packages using pip.

   ```bash
   cd fire-detection
   pip install -r requirements.txt
   ```

3. **Download YOLOv8 Pre-trained Weights:**

   Obtain the YOLOv8 pre-trained weights (e.g., `best.pt`) from the [YOLOv8 GitHub repository](https://github.com/ultralytics/yolov8). Place the downloaded weights file in the project directory.

## Usage

1. **Run the Fire Detection Script:**

   Modify the `Flame_Video.mp4` file path in the `fire_detection.py` script to specify your input video or image containing flames.

   ```bash
   python fire_detection.py
   ```

   This script will perform the following tasks:
   - Initialize the YOLOv8 model with the pre-trained weights.
   - Read the input image or video file.
   - Detect flames in the image/video using YOLOv8.
   - Calculate the height of each detected flame.
   - Evaluate flame heights against predefined criteria and print the results.

## Project Details

### `fire_detection.py`

The main script `fire_detection.py` is responsible for flame detection and height evaluation using the YOLOv8 model.

- **Functions**:
  - `cm_to_feet(cm)`: Helper function to convert flame height from centimeters to feet.
  - `check_flame_height(height_cm)`: Function to evaluate flame height based on predefined criteria.

- **Workflow**:
  1. Initialize the YOLOv8 model with pre-trained weights (`best.pt`).
  2. Load the input image or video file.
  3. Use YOLOv8 to detect flames in the input.
  4. Calculate the height of each detected flame.
  5. Evaluate flame heights and provide feedback based on predefined criteria:
     - "Perfect heat" for flame heights around 4 feet.
     - "Too high flame but acceptable" for flame heights exceeding 7 feet.
     - "Too low, requires more heat" for flame heights below 4 feet.
  6. Display the detected flames overlaid on the input image or video with flame height evaluations.

## Results

Upon running the script, the detected flames along with their respective heights will be displayed on the input image or video. The script will also print the evaluation of each flame's height to the console.

