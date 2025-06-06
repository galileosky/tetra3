#==============================================================================
#
#
#
#==============================================================================

"""
This example loads the tetra3 default database and solves for every image in the
tetra3/examples/data directory.
"""

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

for impath in path.glob('*'):
    print('Solving for image at: ' + str(impath))
    with Image.open(str(impath)) as img:
        # Here you can add e.g. 
        #   `fov_estimate`/`fov_max_error` to improve speed or 
        #   a `distortion` range to search (default assumes undistorted image)
        #
        # There are many optional returns, e.g. `return_matches` or `return_visual`.
        # A core aspect of the solution is centroiding (detecting the stars in the image).
        # You can use `return_images` to get a second return value to check the
        # centroiding process, the key `final_centroids` is especially useful.


        # https://tetra3.readthedocs.io/en/latest/api_docs.html
        #
        # solve_from_image(
        #   image, 
        #   fov_estimate=None, fov_max_error=None, 
        #   pattern_checking_stars=8, match_radius=0.01, match_threshold=0.001, 
        #   solve_timeout=None, target_pixel=None, distortion=0, 
        #   return_matches=False, return_visual=False, **kwargs
        #   )
        #
        # Negative distortion is barrel, positive is pincushion
        #
        #solution = t3.solve_from_image(img, distortion=[-.2, .1])
        #solution = t3.solve_from_image(img, distortion=[-.2, .1], return_matches=True)
        solution = t3.solve_from_image(img, distortion=[-.2, .1], return_matches=True, return_visual=True)


    

    # ’visual’: 
    #   A PIL image with 
    #       . spots for the given centroids in white, 
    #       . the coarse FOV and distortion estimates in orange, 
    #       . the final FOV and distortion estimates in green
    #       . Also has circles for the catalogue stars in green or red
    #         for successful/unsuccessful match. 
    #
    #   Not included if return_visual=False. 
    #


    print('Solution: ' + str(solution))

    visual = solution['visual']

    visual_file_name = 'v'+str(i)+'.png'
    print(f'Save viual file :  {visual_file_name}')
    visual.save(visual_file_name)
    i += 1



 
    print(f'T_extract =  {solution["T_extract"]:6.2f} ms')
    print(f'T_solve   =  {solution["T_solve"]:6.2f} ms')
    print(f'RA        =  {solution["RA"]:6.2f} deg')
    print(f'Dec       =  {solution["Dec"]:6.2f} deg')
    print(f'Roll      =  {solution["Roll"]:6.2f} deg')
    print(f'Matches   =  {solution["Matches"]:3d}')
    print(f'RMSE      =  {solution["RMSE"]:6.2f} arsec')
    print(f'Prob      =  {solution["Prob"]}')
    print(f'match_catID=  {solution["matched_catID"]}')

    print()
    print()
    


# property  database_properties
print(f't3.database_properties =  {t3.database_properties}')


# property  debug_folder
print(f't3.debug_folder =  {t3.debug_folder}')


# property  pattern_largest_edge
print(f't3.pattern_largest_edge =  {t3.pattern_largest_edge}')


# property  star_catalog_IDs
print(f't3.star_catalog_IDs =  {t3.star_catalog_IDs}')


# property  star_table
print(f't3.star_table =  {t3.star_table}')
