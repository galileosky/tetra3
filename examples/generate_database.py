"""
This example generates a tetra3 database from a star catalogue. You must have the catalogue file
hip_main.dat in the same directory as tetra3.py to run this example. You can download it from
https://cdsarc.u-strasbg.fr/ftp/cats/I/239/
"""

import sys
sys.path.append('..')

import tetra3

# Create instance without loading any database.
t3 = tetra3.Tetra3(load_database=None)

# Generate and save database.
# NumPy file optimized for fast matching.

#    def generate_database(self, max_fov, min_fov=None, save_as=None,
#                          star_catalog='hip_main', pattern_stars_per_fov=10,
#                          verification_stars_per_fov=30, star_max_magnitude=7,
#                          pattern_max_error=.005, simplify_pattern=False,
#                          range_ra=None, range_dec=None,
#                          presort_patterns=True, save_largest_edge=False,
#                          multiscale_step=1.5, epoch_proper_motion='now'):

#t3.generate_database(save_as='t3_fov20-30_mag7', max_fov=30, min_fov=20,
#                     star_max_magnitude=7, star_catalog='hip_main')

#t3.generate_database(save_as='t3_fov20-30_mag7_bcs5', max_fov=30, min_fov=20,
#                     star_max_magnitude=7, save_largest_edge=True, star_catalog='bsc5')
t3.generate_database(save_as='t3_fov20-30_mag7_bcs5', max_fov=50, min_fov=10,
                     star_max_magnitude=7, save_largest_edge=True, star_catalog='bsc5')

# the default catalog, takes 15 minutes to build
#  
#t3.generate_database(max_fov=30, min_fov=10, star_max_magnitude=7, save_as='default_database')