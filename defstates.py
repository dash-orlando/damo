'''
defstates.py

Generate TetGen meshes of all deformation states found in the FEBio logfile

Fluvio L Lobo Fenoglietto
12/19/2019
'''

# import libraries and modules
from    _febio      import  *
from    _tetgen     import  _get_state

# variables
input_dir   = r'input'
log_file    = r'arch_3.log'
file        = '{}\{}'.format( input_dir, log_file )

# GO!!!
data = _get_state( file )
