'''
damo.py

Deformation-based Additive Manufacturing Optimization

Fluvio L. Lobo Fenoglietto
12/18/2019
'''

# import libraries and modules
import os

# setup directories
damo_dir                    = os.getcwd()
input_dir                   = r'input'
tetgen_dir                  = r'tetgen1.5.1\build\Debug'
output_dir                  = r'output'

# surface filename
surface_file                = r'arch.stl'

# moving surface file to tetgen directory
cmd                         = 'move {}\{} {}\{}'.format(input_dir, surface_file, tetgen_dir, surface_file)
#print( cmd )
os.system( cmd )



# executing tetgen
tetgen_exe_and_flags        = r'tetgen.exe -pq2.0 -fCVO'
cmd                         = '{}\{} {}\{}'.format( tetgen_dir, tetgen_exe_and_flags, tetgen_dir, surface_file )
#print( cmd )
os.system( cmd )
