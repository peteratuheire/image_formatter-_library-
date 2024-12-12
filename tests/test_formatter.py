import os
from image_formatter.formatter import ImageFormatter

def test_all_functions():
    input_image = "tests/sample.jpg"  # Replace with your test image
    os.makedirs("tests/output", exist_ok=True)

    # Resize Test
    ImageFormatter.resize(input_image, "tests/output/resized.jpg", (200, 200))

    # Crop Test
    ImageFormatter.crop(input_image, "tests/output/cropped.jpg", (50, 50, 150, 150))

    # Rotate Test
    ImageFormatter.rotate(input_image, "tests/output/rotated.jpg", 45)

    # Flip Test
    ImageFormatter.flip(input_image, "tests/output/flipped.jpg", "horizontal")

    # Grayscale Test
    ImageFormatter.grayscale(input_image, "tests/output/grayscale.jpg")

if __name__ == "__main__":
    test_all_functions()
    print("All tests ran successfully.")
