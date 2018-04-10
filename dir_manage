import os
import shutil

# working_dir = os.environ['HOME']+'Python/Dir'
working_dir = os.getcwd()
scripts_dir = working_dir + '/scripts'
input_dir = working_dir + '/input'
output_dir = working_dir + '/output'

# routines below are written by Johannes Keller https://github.com/jjokella

def py_output_dir(tag, ending):
    """
    Generate Python output directory according to tag ending.

    Parameters
    ----------
    tag : string
        Subdirectory name in ~/PythonDir/output

    ending : string
        File ending of output.
        Examples: npy, png, jpg, eps, pdf

    Returns
    ----------
    py_output_dir : string
        Designated output directory.
    """
    py_output_dir = (working_dir + "/"
                     + tag + "/"
                     + ending)

    return py_output_dir


def py_output_filename(tag, filename, spec, ending):
    """
    Generate Python output filename (with specifier)
    according to filename (without ending), tag ending, spec.

    Parameters
    ----------
    tag : string
        Subdirectory name in ~/PythonDir/output

    filename : string
        Filename body, without ending.

    spec : string
        Output identifier that will be added to the filename.

    ending : string
        File ending of output.
        Examples: npy, png, jpg, eps, pdf

    Returns
    ----------
    py_output_filename : string
        Absolute filename for output file.

    Notes
    ----------
    spec is added to filename to form the body filename body.

    The format-convention for spec is of the following form
    (see mypackage.tools.plot.spec.specl()):
        'model_2018_01_01_b'
    In principle any string can be used as spec.
    """

    py_output_filename = (py_output_dir(tag, ending) + "/"
                          + filename + "_" + spec + "."
                          + ending)

    return py_output_filename


def py_simple_output_filename(filename, tag, ending):
    """
    Generate Python simple output filename (without specifier)
    according to filename (without ending), tag, ending.

    Parameters
    ----------
    filename : string
        Filename body, without ending.

    tag : string
        Subdirectory name in ~/PythonDir/output

    ending : string
        File ending of output.
        Examples: npy, png, jpg, eps, pdf

    Returns
    ----------
    py_simple_output_filename : string
        Absolute filename for output file.

    Notes
    ----------
    filename is used as body of the output-filename, nothing is added.
    """

    py_simple_output_filename = (py_output_dir(tag, ending) + "/"
                                 + filename + "."
                                 + ending)

    return py_simple_output_filename
