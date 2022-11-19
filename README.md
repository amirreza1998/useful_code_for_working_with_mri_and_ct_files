# useful_code_for_working_with_mri
in this ripository i want to share some of my useful code that i design when i working with mri and ct image 

<h3>1-extract atuomaticaly headmask and skull from ct images</h3>
when we want to extract some data like skull and head mask from ct image we usaully use threshold 
but you should try diffrenet threshold by hand and check result for reaching the skull and headmask that seem's good by eye
in this code i make it automatical and no need to measure by eyes but with some measure that i define in algorithm of code like 
noting being in middle cube of ct image
code implement in folder of extract_skull_headmask


<h3>2-extract atuomaticaly scalp from ct images</h3>
the idea of this code is at first extract skull of ct image and then ceate contour around that skull and then fill that countour 
and make logical operation of "or" between ct image and filled contour to extract scalp
code implement in folder of scalp_extractor
