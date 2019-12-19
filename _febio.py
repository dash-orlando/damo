'''
_febio.py

Deformation-based Additive Manufacturing Optimization
FEBio interface module


    FEATURES:
    ---------
        - Given a list input "variables", the program extracts their corresponding "values" from the FEBio log file


    LIMITATIONS:
    ------------
        - If the variable name is repeated, the value will be overwritten (e.g. 'laugon' is repeated on every contact constrained)


Fluvio L. Lobo Fenoglietto
12/19/2019
'''

# variables
variables = [ 'Number of timesteps',
              'Time step size']
values = []

# functions ========================================================================== #

def _get_variables( file, variables ):

    with open( file ) as log:
        for line in log:
            trimmed_line = line.strip('\t').strip('\n').split(' ')
            ## print( trimmed_line )

            # if the first element of the line is blank, pass...
            if trimmed_line[0] == '':
                pass

            # if the line cotains less than 4 elements, pass... 
            elif  len( trimmed_line ) < 4:
                pass

            # if the first 4 elements of the line contain this string, end the process...
            elif '{} {} {} {}'.format( trimmed_line[0], trimmed_line[1], trimmed_line[2], trimmed_line[3] ) == '===== beginning time step':
                break

            # otherwise...
            else:
                # match each input variable to the incoming line, element by element
                # if a perfect match is found, store tha associated value
                for i in range( 0, len( variables ) ):
                    variable = variables[i].split(' ')
                    match_index = 0
                    for j in range( 0, len( variable ) ):
                        if trimmed_line[j] == variable[j]:
                            match_index += 1
                    if match_index == 3:
                        values.append( trimmed_line[len(trimmed_line)-1] )

    return variables, values

# GO ================================================================================= #


variables, values = _get_variables( file, variables )
