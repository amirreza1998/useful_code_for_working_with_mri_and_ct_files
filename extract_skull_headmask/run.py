import nibabel as nib
import numpy as np
from skull_headmask_extractor import bone_calculator
from Write_Image_affine import Write_Image_affine
from pathlib import Path
import os



# CT_path = r"C:\Users\amirreza\Desktop\New folder (4)\New_T1.nii"#set your path of ct image or you could uncomment code below and use tkinter

###----------------------open_file_with_tkinter-------------------------###
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
CT_path = filedialog.askopenfilename( title="Select a CT Image:",
                                        filetypes=(
                                            ('nii files', '*.nii'),
                                            ('image files', '*.img'),
                                            ('All files', '*.*')
                                        )
                                        )
###---------------------------------------------------------------------###




###---------------load_CT_file--------------###
CT = nib.load(CT_path)
affine_ct = CT.affine
CT=np.array(CT.dataobj)
###-----------------------------------------###

###-------------extract_bone_and_headmask--------------###
headmask,skull = bone_calculator(CT)
###----------------------------------------------------###



###-------------save_result_in_beside_file_folder_extraction_result--------------###
path_file = Path(CT_path)
path_file_parent = path_file.parent
outputPath = path_file_parent / "extraction_result"
if not os.path.isdir(outputPath):
    os.mkdir(outputPath)

Write_Image_affine(skull, "Skull", outputPath,affine_ct)
Write_Image_affine(headmask, "Headmask", outputPath,affine_ct)
###------------------------------------------------------------------------------###