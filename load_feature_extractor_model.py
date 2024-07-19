from easydict import EasyDict

from four_d_ct_cost_unrolling import  infer_backbone
from four_d_ct_cost_unrolling import get_default_backbone_config, get_default_checkpoints_path


args = get_default_backbone_config()
args["inference_args"]["inference_flow_median_filter_size"] = False
args["visualization_arrow_scale_factor"] = 1
args["cuda_device"] = 0
args["scale_down_by"] = 2
args["load"] = get_default_checkpoints_path()

x1_p = backbone_inference_output_path = infer_backbone(
    template_image_path='/home/fiman/projects/DL_course/spectral_diffusion/spectral_diffusion/cardiac_sample_data/cardiac_sample_data/cardiac_sample_data/image_skewed_thetas_100.0_0.0_rs_0.9_0.9_h_0.91_linear_mask_True_blur_radious_1.npy',
    unlabeled_image_path='/home/fiman/projects/DL_course/spectral_diffusion/spectral_diffusion/cardiac_sample_data/cardiac_sample_data/cardiac_sample_data/image_orig_thetas_100.0_0.0_rs_0.9_0.9_h_0.91_linear_mask_True_blur_radious_1.npy',
    template_LV_seg_path='/home/fiman/projects/DL_course/spectral_diffusion/spectral_diffusion/cardiac_sample_data/cardiac_sample_data/cardiac_sample_data/mask_skewed_thetas_100.0_0.0_rs_0.9_0.9_h_0.91_linear_mask_True_blur_radious_1.npy',
    unlabeled_LV_seg_path='/home/fiman/projects/DL_course/spectral_diffusion/spectral_diffusion/cardiac_sample_data/cardiac_sample_data/cardiac_sample_data/mask_orig_thetas_100.0_0.0_rs_0.9_0.9_h_0.91_linear_mask_True_blur_radious_1.npy',
    template_shell_seg_path='/home/fiman/projects/DL_course/spectral_diffusion/spectral_diffusion/cardiac_sample_data/cardiac_sample_data/cardiac_sample_data/extra_mask_skewed_thetas_100.0_0.0_rs_0.9_0.9_h_0.91_linear_mask_True_blur_radious_1.npy',
    unlabeled_shell_seg_path='/home/fiman/projects/DL_course/spectral_diffusion/spectral_diffusion/cardiac_sample_data/cardiac_sample_data/cardiac_sample_data/extra_mask_orig_thetas_100.0_0.0_rs_0.9_0.9_h_0.91_linear_mask_True_blur_radious_1.npy',
    flows_gt_path='/home/fiman/projects/DL_course/spectral_diffusion/spectral_diffusion/cardiac_sample_data/cardiac_sample_data/cardiac_sample_data/flow_for_image_thetas_100.0_0.0_rs_0.9_0.9_h_0.91_linear_mask_True_blur_radious_1.npy',
    args=EasyDict(args),
    feature_extractor_mode=True
    )

print(1)
