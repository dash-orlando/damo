'''
defstates.py

Generate TetGen meshes of all deformation states found in the FEBio logfile

Fluvio L Lobo Fenoglietto
12/19/2019
'''

# import libraries and modules
#from    _febio      import  *
from    _tetgen     import  _get_state
from    _tetgen     import  _write_node

# variables
input_dir   = r'input'
log_file    = r'arch_4.log'
file        = '{}\{}'.format( input_dir, log_file )

# GO!!!
data = _get_state( file )

##node    = data['10']['node']
##x       = data['10']['x']
##y       = data['10']['y']
##z       = data['10']['z']
##
##_write_node( node, x, y, z, 'arch_4_s10.node')

for i in range( 0, len( data ) ):
    node    = data[str(i+1)]['node']
    x       = data[str(i+1)]['x']
    y       = data[str(i+1)]['y']
    z       = data[str(i+1)]['z']

    filename = 'arch_4_s{}.node'.format( str(i+1) )
    _write_node( node, x, y, z, filename )
    


