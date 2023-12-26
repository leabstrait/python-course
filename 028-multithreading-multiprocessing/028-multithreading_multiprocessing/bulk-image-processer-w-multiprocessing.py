import time
import os
import concurrent.futures

from PIL import Image, ImageFilter


imgs = [
    'downloaded-images/photo-1516117172878-fd2c41f4a759.jpg',
    'downloaded-images/photo-1532009324734-20a7a5813719.jpg',
    'downloaded-images/photo-1524429656589-6633a470097c.jpg',
    'downloaded-images/photo-1530224264768-7ff8c1789d79.jpg',
    'downloaded-images/photo-1564135624576-c5c88640f235.jpg',
    'downloaded-images/photo-1541698444083-023c97d3f4b6.jpg',
    'downloaded-images/photo-1522364723953-452d3431c267.jpg',
    'downloaded-images/photo-1513938709626-033611b8cc03.jpg',
    'downloaded-images/photo-1507143550189-fed454f93097.jpg',
    'downloaded-images/photo-1493976040374-85c8e12f0c0e.jpg',
    'downloaded-images/photo-1504198453319-5ce911bafcde.jpg',
    'downloaded-images/photo-1530122037265-a5f1f91d3b99.jpg',
    'downloaded-images/photo-1516972810927-80185027ca84.jpg',
    'downloaded-images/photo-1550439062-609e1531270e.jpg',
    'downloaded-images/photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()
size = (1200, 1200)

def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed-images/{img_name[18:]}')
    print(f'{img_name} was processed...')

if not os.path.exists('processed-images'):
    os.mkdir('processed-images')

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, imgs)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')