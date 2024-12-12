# Image Formatter Library

A simple Python library for basic image manipulation, including functions for resizing, cropping, rotating, flipping, and converting formats.

---

## Table of Contents

- [Installation]
  - [Setup for Local Development]
  - [Setup for Virtual Environment]
  - [Setup for Docker]
- [Usage]
- [Testing]
- [Contributing]

---

## Installation

### Setup for Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/image-formatter.git
   cd image-formatter
   ```

2. **Install dependencies**:
   To install the required dependencies, use `pip`. Make sure you are using a Python version that is supported (e.g., Python 3.6+).

   ```bash
   pip install -r requirements.txt
   ```
   
3. **Install the library in editable mode**:
   To allow local development with live changes:
   ```bash
   pip install -e .
   ```

### Setup for Virtual Environment

1. **Create a Virtual Environment**:
   ```bash
   python -m venv image_lib_env
   ```

2. **Activate the Virtual Environment**:
   - On **Windows**:
     ```bash
     image_lib_env\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source image_lib_env/bin/activate
     ```
3. **Install dependencies in the virtual environment**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the library in editable mode**:
   ```bash
   pip install -e .
   ```

### Setup for Docker

1. **Build the Docker image**:
   ```bash
   docker build -t image-formatter .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -it image-formatter
   ```
   
3. **Running Tests Inside Docker**:
   If you want to run the tests inside the Docker container, follow these steps after building the image:
   ```bash
   docker run -it image-formatter pytest
   ```
   
## Usage

Once you have installed the library, you can start using the image formatting functions.

### Example Usage
```
python
from image_formatter.formatter import ImageFormatter

# Resize an image
ImageFormatter.resize('path/to/input/image.jpg', 'path/to/output/resized.jpg', (200, 200))

# Crop an image
ImageFormatter.crop('path/to/input/image.jpg', 'path/to/output/cropped.jpg', (50, 50, 150, 150))

# Rotate an image
ImageFormatter.rotate('path/to/input/image.jpg', 'path/to/output/rotated.jpg', 45)

# Flip an image (horizontal or vertical)
ImageFormatter.flip('path/to/input/image.jpg', 'path/to/output/flipped.jpg', 'horizontal')

# Convert an image to grayscale
ImageFormatter.grayscale('path/to/input/image.jpg', 'path/to/output/grayscale.jpg')
```

## Testing

To ensure everything is working correctly, you can run the tests in the `tests/` folder.

1. **Install dependencies** if you haven’t already:
   ```bash
   pip install -r requirements.txt
   
   pytest tests
   ```
   
## Contributing

We welcome contributions! To contribute to this project:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your forked repository and submit a pull request.
