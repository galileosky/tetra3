#==============================================================================
# Extract spot centroids from an image and calculate statistics.
#
#
#==============================================================================

"""
This example loads the tetra3 default database and solves for every image in the
tetra3/examples/data directory.
"""



# https://tetra3.readthedocs.io/en/latest/api_docs.html
#
# tetra3.get_centroids_from_image(
#   image, sigma=2, image_th=None, crop=None, downsample=None,
#   filtsize=25, 
#   bg_sub_mode='local_mean', sigma_mode='global_root_square',
#   binary_open=True, centroid_window=None, max_area=100, min_area=5,
#   max_sum=None, min_sum=None, max_axis_ratio=None, max_returned=None,
#   return_moments=False, 
#   return_images=False
# )


'''
This is a versatile function for finding spots (e.g. stars or satellites) in an
image and calculating/filtering their positions (centroids) and statistics
(e.g. sum, area, shape).

The coordinates start at the top/left edge of the pixel, i.e. x=y=0.5 is the
centre of the top-left pixel. 
To convert the results to integer pixel indices use the floor operator.


To aid in finding optimal settings pass return_images=True to get back a
dictionary with partial extraction results and tweak the parameters accordingly.
The dictionary entry binary_mask shows the result of the raw star detection and
final_centroids labels the centroids in the original image (green for accepted,
red for rejected).




'''





#==============================================================================
#
#
#
#==============================================================================

import sys
sys.path.append('..')

from PIL import Image
from pathlib import Path

EXAMPLES_DIR = Path(__file__).parent

import tetra3


#==============================================================================
#
#
#
#==============================================================================



#==============================================================================
#
#
#
#==============================================================================

# Create instance and load the default database, built for 30 to 10 degree field of view.
# Pass `load_database=None` to not load a database, or to load your own.
t3 = tetra3.Tetra3()



# Path where images are
print(f'EXAMPLES_DIR =  {EXAMPLES_DIR}')
path = EXAMPLES_DIR / 'data'

print(f'path         =  {path}')

print()





i = 0
file_no = 0

for impath in path.glob('*'):
    print('Solving for image at: ' + str(impath))
    with Image.open(str(impath)) as img:


        # https://tetra3.readthedocs.io/en/latest/api_docs.html
        #
        # tetra3.get_centroids_from_image(
        #   image, sigma=2, image_th=None, 
        #   crop=None, downsample=None,
        #   filtsize=25, 
        #   bg_sub_mode='local_mean', sigma_mode='global_root_square',
        #   binary_open=True, centroid_window=None, max_area=100, min_area=5,
        #   max_sum=None, min_sum=None, max_axis_ratio=None, max_returned=None,
        #   return_moments=False, 
        #   return_images=False
        # )
        #
        #centroids = tetra3.get_centroids_from_image(img)
        #centroids = tetra3.get_centroids_from_image(img, return_moments=True)
        centroids = tetra3.get_centroids_from_image(img, return_images=True)


        cropped_and_downsampled = centroids[1]['cropped_and_downsampled']
        binary_mask = centroids[1]['binary_mask']
        final_centroids = centroids[1]['final_centroids']       

    #print('centroids: ' + str(centroids))
    print(f'centroids =\n{centroids}')
    print(f'{len(centroids[0])} stars found')
    print(f'cropped_and_downsampled =  {cropped_and_downsampled}')
    print(f'binary_mask =  {binary_mask}')
 
 
    x = 0
    y = 0
    count = 0
    for row in binary_mask:
        for col in row:
            if col == True:
                #print(f'({x}, {y}) :  {col}')
                count += 1
            x += 1
        y += 1
        x = 0

    print(f'binary_mask TRUE count =  {count}')
 
    final_centroids.save('final_centroids_'+str(file_no)+'.png')
    file_no += 1

    print()


