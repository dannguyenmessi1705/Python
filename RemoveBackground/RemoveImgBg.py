from rembg import remove
from PIL import Image
input_path = 'thang.jpg'
output_path = 'thang_RemoveBg.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path) # type: ignore