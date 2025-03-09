
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

print("Imports finished! numpy, PIL and matplotlib.pyplot")
image_path = "DB3_B/101_5.tif"  # See README for whence info. Note: All DB3_B images are '300 by 300' tiffs 
new_png_filename = "fingerprint_101_TEST.png"


image = Image.open(image_path)
image_gray = image.convert("L") # Grayscale good! Color bad!
image_array = np.array(image_gray)

image_vector = image_array.ravel()
avg_gray_value = np.mean(image_vector)
vector_adjusted = image_vector - avg_gray_value
# Back to the orig 300 by 300 ( or whatever the first image's height width was ) 
image_adjusted_from_vector = vector_adjusted.reshape(image_array.shape)
# 128? Yeah, numpy will have vectorized around 0 as the mean. 
# Because I, as a human, want to see this, I upshift the values from a mean of 0 to a mean of 128. 
image_normalized_from_vector = np.clip(image_adjusted_from_vector + 128, 0, 255).astype(np.uint8)

# L = luminance
new_image_from_vector = Image.fromarray(image_normalized_from_vector, mode="L")




print("Image successfully vectorized and reconstructed.")

new_image_from_vector.save(new_png_filename)
print("Saved new_png_filename as '{}'".format(new_png_filename)) 





