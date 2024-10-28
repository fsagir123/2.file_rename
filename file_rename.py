# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 13:11:33 2023

@author: fsagir
"""

import os

def rename_files(folder_path, rename_list):
    for old_name, new_name in rename_list:
        old_file_path = os.path.join(folder_path, old_name)
        new_file_path = os.path.join(folder_path, new_name)
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} -> {new_file_path}")

# Replace this with your desired folder path and rename list
folder_path = 'C:/Users/fsagir/Desktop/Renaming'
rename_list = [
('INT_AM_001 - NB.rbc','1. 2050 NB AM_Wentzville Pkwy & Pearce.rbc'),
('INT_AM_002 - NB.rbc','2. 2050 NB AM_Wentzville Pkwy & I70 WB Ramp.rbc'),
('INT_AM_003 - NB.rbc','3. 2050 NB AM_Wentzville Pkwy & I70 EB Ramp-SOR.rbc'),
('INT_AM_004 - NB.rbc','4. 2050 NB AM_US 61 NB Ramp & Pitman.rbc'),
('INT_AM_005 - NB.rbc','5. 2050 NB AM_US 61 SB Ramp & Pitman.rbc'),
('INT_AM_006 - NB.rbc','6. 2050 NB AM_US 61 NB Ramp & RTA.rbc'),
('INT_AM_007 - NB.rbc','7. 2050 NB AM_US 61 SB Ramp & RTA.rbc'),
('INT_AM_008 - NB.rbc','8. 2050 NB AM_I70 EB & RTA.rbc'),
('INT_AM_009 - NB.rbc','9. 2050 NB AM_I70 WB & RTA.rbc'),
('INT_AM_012 - NB.rbc','10. 2050 NB AM_Wentzville & Luetkenhaus.rbc'),
('INT_AM_013 - NB.rbc','11. 2050 NB AM_Route Z & Interstate Dr..rbc'),
('INT_AM_013 - Copy - NB.rbc','12. 2050 NB AM_Luetkenhaus & Pearce Blvd.rbc'),





    # Add more tuples for the remaining files
]

rename_files(folder_path, rename_list)


#Replace /path/to/your/folder with the actual path to the folder where your files are located. In the rename_list, provide pairs of old and new file names that you want to change. Make sure to add all 14 files in the same format as the examples shown. The code will iterate through the list and rename the files accordingly.

#Remember to customize the file names and extensions in the rename_list to match the files you have in your folder. As always, be cautious when renaming files and have a backup of your data before making changes.





