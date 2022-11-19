import numpy as np
import nibabel as nib
def bone_calculator(CT_bn):
    # dataArrayVal = np.expand_dims(dataArray, axis=3)

    shape_ct = CT_bn.shape
    [N, M, L] = shape_ct
    shape_checker = list()
    max_CT_bn = np.max(CT_bn)
    min_CT_bn = np.min(CT_bn)
    for i in shape_ct:
        shape_checker.append([round(i / 2) - round(i / 5), round(i / 2) + round(i / 5)])
    CT_bn = np.divide((CT_bn - min_CT_bn), (max_CT_bn - min_CT_bn))

    ###-----------------headmask---------------------###
    threshold_head = 0.1
    Img_out_head = (CT_bn > threshold_head) * 1
    # Write_Image(Img_out_head, "cN{}_headmask".format(ii), outputPath_skull, affine_ct)
    ###----------------------------------------------###

    ###-------------------skull----------------------###
    ranger = list(np.arange(0.0, 1.0, 0.02))
    ranger.reverse()
    status = False
    for ranger_index in range(len(ranger)):
        threshold = round(ranger[ranger_index], 2)
        print(f"this is threshold:{threshold}")
        Img_out = np.multiply(CT_bn, (CT_bn > threshold) * 1)
        # Img_out=Img_out*((1-0)/(threshold-0))
        for i in range(shape_checker[0][0], shape_checker[0][1]):
            for j in range(shape_checker[1][0], shape_checker[1][1]):
                for k in range(shape_checker[2][0], shape_checker[2][1]):
                    if Img_out[i, j, k] != 0:
                        status = True
        print(f"this is ranger_index:{ranger_index}")
        if status == True:
            break

    threshold = round(ranger[ranger_index - 1], 2)
    print(threshold)
    Img_out = (CT_bn > threshold) * 1
    # Write_Image(Img_out, "cN{}_skull".format(ii), outputPath_skull, affine_ct)
    ###----------------------------------------------###
    return Img_out_head, Img_out
