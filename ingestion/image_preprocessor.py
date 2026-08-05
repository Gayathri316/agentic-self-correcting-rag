"""
Image preprocessing before OCR.
"""

from pathlib import Path
import cv2


class ImagePreprocessor:

    def preprocess(self, image_path: str) -> str:

        image = cv2.imread(image_path)

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Reduce noise
        gray = cv2.GaussianBlur(gray, (3, 3), 0)

        # Improve contrast
        processed = cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            11
        )

        output_path = Path(image_path).with_name(
            Path(image_path).stem + "_processed.png"
        )

        cv2.imwrite(str(output_path), processed)

        return str(output_path)