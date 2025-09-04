import numpy as np
import cv2 as cv

def ft_load(path: str) -> np.ndarray:
    """
    Loads an image in RGB format and prints its shape.
    """
    if not path.lower().endswith(('.jpg', '.jpeg')):
        raise ValueError("Only JPG/JPEG files are supported")
    
    img = cv.imread(path)
    if img is None:
        raise FileNotFoundError(f"Image at {path} could not be read")
    
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    print(f"The shape of image is : {img.shape}")

    return img

