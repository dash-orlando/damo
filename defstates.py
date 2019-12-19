'''
defstates.py

Generate TetGen meshes of all deformation states found in the FEBio logfile

Fluvio L Lobo Fenoglietto
12/19/2019
'''

# import libraries and modules
from    _febio      import  *
from    _tetgen     import  _get_state
from    _tetgen     import  _write_node

# variables
input_dir   = r'input'
log_file    = r'arch_3.log'
file        = '{}\{}'.format( input_dir, log_file )

# GO!!!
data = _get_state( file )

node    = data['10']['node']
x       = data['10']['x']
y       = data['10']['y']
z       = data['10']['z']

print( len(node) )

_write_node( node, x, y, z, 'arch_3_s10.node')
