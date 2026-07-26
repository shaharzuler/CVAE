# Systole-Conditioned Generative Cardiac Motion Using Deep Learning

We present a method to generate synthetic 3D flow fields for myocardium deformation, conditioning on real cardiac CT frames using a Conditional Variational Autoencoder (CVAE). These synthetic data serve as ground truth annotations for training myocardium motion models. For a full explanation and results, visit the [project page](https://shaharzuler.github.io/GenerativeCardiacMotion_Page).

## Installation

To install the necessary dependencies for the project, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/shaharzuler/GenerativeCardiacMotion.git
2. Navigate to the project directory:
    ```bash
    cd GenerativeCardiacMotion
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```


## Dataset Preparation

To prepare the dataset, use `create_cvae_dataset.py`. The `data_source` directory must contain:
- `template_img_<number>` files as 3D numpy arrays (shape: x, y, z) representing systole frames.
- `flow_<number>` files as numpy arrays (shape: 3, x, y, z) representing the flow fields.

Adjust the `data_source` and `target_dir` paths in the script and run it to generate the dataset, extracting features from the pyramid feature extractor.


## Training

To train the model, use `train.py`:

- Adjust `top_out_path` and `dataset_path` to the correct directories.
- You can enable multiprocessing for running 4 parallel trainings, looping over the entire 44 samples, or specify a single sample using `l1o_idx`.
- The script outputs tensorboard logs, model weights, generated flow, and a 3D conditioned image to the output directory.
- Modify hyperparameters in `config.json` as needed.

Results and logs will be saved in the specified `top_out_path`.


## Inference

To perform inference using the trained model, run `infer.py`:

- Adjust `top_out_path`, `final_model` (weights path), and `dataset_path`.
- Set `num_generations` to specify how many samples to generate.
- Select the type of latent space sampling to perform from the methods detailed below:

#### Latent Space Sampling Methods:

1. **Random Sampling**: Samples latent vectors from a standard normal distribution, creating diverse outputs.
2. **Grid Search**: Explores the latent space systematically by generating flow fields along a predefined grid of latent variables.
3. **2D Plane Sampling**: Random sampling is restricted to a selected 2D plane within the latent space, allowing exploration of variations constrained to a specific slice of the latent distribution.

## Publication

This work was published as a peer-reviewed book chapter:

**[Systole-Conditioned Generative Cardiac Motion Using Deep Learning](https://www.intechopen.com/online-first/1242893)**  
Shahar Zuler, Gal Lifshitz, Hadar Averbuch-Elor, and Dan Raviv  
In *Artificial Intelligence in Medicine and Surgery – An Exploration of Current Trends, Potential Opportunities, and Evolving Threats, Volume 5*, IntechOpen, 2026.

**DOI:** [10.5772/intechopen.1015635](https://doi.org/10.5772/intechopen.1015635)

## Citation

If you use this work or code, please cite:

```bibtex
@incollection{Zuler2026SystoleConditioned,
  author    = {Zuler, Shahar and Lifshitz, Gal and Averbuch-Elor, Hadar and Raviv, Dan},
  title     = {Systole-Conditioned Generative Cardiac Motion Using Deep Learning},
  booktitle = {Artificial Intelligence in Medicine and Surgery: An Exploration of Current Trends, Potential Opportunities, and Evolving Threats, Volume 5},
  editor    = {Stawicki, Stanislaw P. and Wojda, Thomas R.},
  publisher = {IntechOpen},
  address   = {London},
  year      = {2026},
  doi       = {10.5772/intechopen.1015635},
  url       = {https://doi.org/10.5772/intechopen.1015635}
}
```


The script will generate synthetic flow fields based on the latent space exploration, outputting the results in the specified path.
