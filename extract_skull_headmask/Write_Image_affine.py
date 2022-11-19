import os
import nibabel as nib
import numpy as np
import scipy.io as sio


def Write_Image_affine(Img_out, name, path, affine_ct_func=None):
    """
    write numpy array of image in nifty image version of file
    ---------
    output_path: Path
        the path for save file
    name: Str
        file name to save
    Img_out: numpy
        numpy that include value for saving them in nifty file

    Returns
    ------
    None
    """
    if affine_ct_func.all()!=None:
        img = nib.Nifti1Image(Img_out, affine_ct_func)
    elif affine_ct_func.all()==None:
        img = nib.Nifti1Image(Img_out, np.eye(4))
    nib.save(img,os.path.join(path, name+'.nii'))

    
def Write_Image(Img_out, name, path, affine_ct_func=None):
    """
    write numpy array of image in nifty image version of file
    ---------
    output_path: Path
        the path for save file
    name: Str
        file name to save
    Img_out: numpy
        numpy that include value for saving them in nifty file

    Returns
    ------
    None
    """
    if affine_ct_func.all()!=None:
        img = nib.Nifti1Image(Img_out, affine_ct_func)
    elif affine_ct_func.all()==None:
        img = nib.Nifti1Image(Img_out, np.eye(4))
    nib.save(img,os.path.join(path, name+'.nii'))
