from PIL import Image

class ImageFormatter:
    @staticmethod
    def resize(image_path: str, output_path: str, size: tuple):
        """
        Resize an image to the given size.

        Args:
            image_path (str): Path to the input image.
            output_path (str): Path to save the resized image.
            size (tuple): New size as a tuple (width, height).
        """
        with Image.open(image_path) as img:
            img_resized = img.resize(size)
            img_resized.save(output_path)

    @staticmethod
    def crop(image_path: str, output_path: str, box: tuple):
        """
        Crop an image to the given box.

        Args:
            image_path (str): Path to the input image.
            output_path (str): Path to save the cropped image.
            box (tuple): The crop rectangle, as a tuple (left, upper, right, lower).
        """
        with Image.open(image_path) as img:
            img_cropped = img.crop(box)
            img_cropped.save(output_path)

    @staticmethod
    def rotate(image_path: str, output_path: str, angle: float):
        """
        Rotate an image by the given angle.

        Args:
            image_path (str): Path to the input image.
            output_path (str): Path to save the rotated image.
            angle (float): Angle to rotate the image, in degrees.
        """
        with Image.open(image_path) as img:
            img_rotated = img.rotate(angle)
            img_rotated.save(output_path)

    @staticmethod
    def flip(image_path: str, output_path: str, mode: str):
        """
        Flip an image (horizontal or vertical).

        Args:
            image_path (str): Path to the input image.
            output_path (str): Path to save the flipped image.
            mode (str): Flip mode, either "horizontal" or "vertical".

        Raises:
            ValueError: If the mode is not "horizontal" or "vertical".
        """
        with Image.open(image_path) as img:
            if mode == "horizontal":
                img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif mode == "vertical":
                img_flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
            else:
                raise ValueError("Mode must be 'horizontal' or 'vertical'")
            img_flipped.save(output_path)

    @staticmethod
    def grayscale(image_path: str, output_path: str):
        """
        Convert an image to grayscale.

        Args:
            image_path (str): Path to the input image.
            output_path (str): Path to save the grayscale image.
        """
        with Image.open(image_path) as img:
            img_gray = img.convert("L")
            img_gray.save(output_path)
