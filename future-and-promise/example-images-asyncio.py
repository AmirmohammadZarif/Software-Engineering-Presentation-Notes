import asyncio
from PIL import Image, ImageFilter

async def process_image(image_path):
    img = Image.open(image_path)
    img = img.filter(ImageFilter.BLUR)
    output_path = f"processed_{image_path}"
    img.save(output_path)
    await asyncio.sleep(1) 
    return f"Processed and saved: {output_path}"

async def main():
    images = ["image1.jpg", "image2.jpg", "image3.jpg"]  
    tasks = [process_image(img) for img in images]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())