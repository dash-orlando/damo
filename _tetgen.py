'''
_tetgen.py

Deformation-based Additive Manufacturing Optimization
TETGEN interface module


    FEATURES:
    ---------
        - Generates tetgen meshes from each deformation state described in the FEBio log file

    LIMITATIONS:
    ------------
        - This program assumes that the format for the output data, in the log file, follows;
            x; y; z; ux; uy; uz

Fluvio L. Lobo Fenoglietto
12/19/2019
'''


# functions ========================================================================== #

def _get_state( file ):
    '''
    _get_data(X)
    Retrieves nodal position data from FEBio logfile
    This data can be used to:
        - Reconstruct meshes
        - Calculate displacement, deformation gradients
    '''

    # variables
    data    = {}
    state   = []
    time    = []
    node    = []
    x       = []
    y       = []
    z       = []

    # flags
    record  = False
    num     = False

    # function start...
    with open( file ) as log:
        for line in log:
            trimmed_line = line.strip('\t').strip('\n').split(' ')

            if len( trimmed_line ) >= 2 and '{} {}'.format( trimmed_line[0], trimmed_line[1] ) == 'Data Record':
                record = True

            if record == True:

                if trimmed_line[0] == '=':
                    pass

                elif trimmed_line[0] == '':
                    record  = False
                    num    = False

                    # save data
                    data[state[len(state)-1]]           = {}
                    data[state[len(state)-1]]['time']   = time[len(time)-1]
                    data[state[len(state)-1]]['node']   = node
                    data[state[len(state)-1]]['x']      = x
                    data[state[len(state)-1]]['y']      = y
                    data[state[len(state)-1]]['z']      = z

                    # clear arrays
                    node    = []
                    x       = []
                    y       = []
                    z       = []

                elif trimmed_line[0] == 'Step':
                    state.append( trimmed_line[ len( trimmed_line ) - 1 ] )

                elif trimmed_line[0] == 'Time':
                    time.append( trimmed_line[ len( trimmed_line ) - 1 ] )

                elif trimmed_line[0] == '1':
                    node.append(    trimmed_line[0] )
                    x.append(       trimmed_line[1] )
                    y.append(       trimmed_line[2] )
                    z.append(       trimmed_line[3] )
                    num = True

                elif num == True:
                    node.append(    trimmed_line[0] )
                    x.append(       trimmed_line[1] )
                    y.append(       trimmed_line[2] )
                    z.append(       trimmed_line[3] )


        return data

# ------------------------------------------------------------------------------------ #


def _write_node( node, x, y, z, file ):

    '''
    Write-out .node file for the input coordinates {x,y,z} [1]
    '''
    
    node_file = open( file, "w" )

    for i in range( 0, len( node ) ):
        if i == 0:
            node_file.write( '{} {} {} {} \n'.format( len( node ), 3, 0, 0 ) )
        node_file.write( '{} {} {} {} \n'.format( node[i], x[i], y[i], z[i] ) )

    node_file.close()
    

# ------------------------------------------------------------------------------------ #


'''
References
1. .node files (https://wias-berlin.de/software/tetgen/fformats.node.html)

'''
