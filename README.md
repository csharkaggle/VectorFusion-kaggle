# VectorFusion: Text-to-SVG by Abstracting Pixel-Based Diffusion Models

In this work, the authors show that a text-conditioned diffusion model trained on pixel representations of images can be
used to
generate SVG-exportable vector graphics.

> official website: https://vectorfusion.github.io/

<div align="center">
  <img src="./img/vectorfusion_64paths_72videos_encode2p5k.gif" style="width: 100%; height: auto;" alt="VF video">
  <p>VectorFusion rendering process. (64paths, 72videos, 5k)</p>
</div>

## Updates

- [01/2024] 🔥 **We released the [SVGDreamer](https://ximinng.github.io/SVGDreamer-project/). SVGDreamer is
  a novel text-guided vector graphics synthesis method. This method considers both the editing of vector graphics and
  the quality of the synthesis.**
- [12/2023] 🔥 **We released the [PyTorch-SVGRender](https://github.com/ximinng/PyTorch-SVGRender). Pytorch-SVGRender is
  the go-to library for state-of-the-art differentiable rendering methods for image vectorization.**
- [10/2023] 🔥 **We released the [DiffSketcher code](https://github.com/ximinng/DiffSketcher). A method of synthesizing
  vector sketches by text prompts.**
- [10/2023] 🔥 We reproduce the VectorFusion code.

## Installation Guide

To quickly get started with **DiffSketcher**, follow the steps below.  
These instructions will help you run **quick inference locally**.

#### 🚀 **Option 1: Standard Installation**

Run the following command in the **top-level directory**:

```shell
chmod +x script/install.sh
bash script/install.sh
```

#### 🐳 Option 2: Using Docker

```shell
chmod +x script/run_docker.sh
sudo bash script/run_docker.sh
```

## Quickstart

### Case: Sydney Opera House

**Prompt:** the Sydney Opera House.<br/>
**Style:** iconography <br/>
**Preview:**

| <img src="./img/Icon-SydneyOperaHouse/sample.png" style="width: 250px; height: 250px;"> | <img src="./img/Icon-SydneyOperaHouse/live.svg" style="width: 250px; height: 250px;"> | <img src="./img/Icon-SydneyOperaHouse/finetune.svg" style="width: 250px; height: 250px;"> |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| (a) Sample raster image with Stable Diffusion                                           | (b) Convert raster image to a vector via LIVE                                         | (c) VectorFusion: Fine tune by LSDS                                                       |

**LIVE Rendering Process:**

|                        iter 0                         |                        iter 500                         |                        iter 1000                         |                        iter 1500                         | iter 2500                                                | iter 3500                                                |
|:-----------------------------------------------------:|:-------------------------------------------------------:|:--------------------------------------------------------:|:--------------------------------------------------------:|----------------------------------------------------------|----------------------------------------------------------|
| <img src="./img/Icon-SydneyOperaHouse/svg_iter0.svg"> | <img src="./img/Icon-SydneyOperaHouse/svg_iter500.svg"> | <img src="./img/Icon-SydneyOperaHouse/svg_iter1000.svg"> | <img src="./img/Icon-SydneyOperaHouse/svg_iter1500.svg"> | <img src="./img/Icon-SydneyOperaHouse/svg_iter2500.svg"> | <img src="./img/Icon-SydneyOperaHouse/svg_iter3500.svg"> |

**VectorFusion Rendering Process:**

|                        iter 0                        |                        iter 100                        |                        iter 300                        |                        iter 400                        | iter 700                                               | iter 1000                                            |
|:----------------------------------------------------:|:------------------------------------------------------:|:------------------------------------------------------:|:------------------------------------------------------:|--------------------------------------------------------|------------------------------------------------------|
| <img src="./img/Icon-SydneyOperaHouse/ft_iter0.svg"> | <img src="./img/Icon-SydneyOperaHouse/ft_iter100.svg"> | <img src="./img/Icon-SydneyOperaHouse/ft_iter300.svg"> | <img src="./img/Icon-SydneyOperaHouse/ft_iter400.svg"> | <img src="./img/Icon-SydneyOperaHouse/ft_iter700.svg"> | <img src="./img/Icon-SydneyOperaHouse/finetune.svg"> |

**Script:**

```shell
python run_painterly_render.py \ 
  -c vectorfusion.yaml \
  -pt "the Sydney Opera House. minimal flat 2d vector icon. lineal color. on a white background. trending on artstation" \
  -save_step 50 \ 
  -update "K=6" \ 
  -respath workdir/SydneyOperaHouse \
  -d 15486 \
  --download
```

- `-c` a.k.a `--config`: configuration file.
- `-save_step`: the step size used to save the result (**too frequent calls will result in longer times**).
- `-update`: a tool for editing the hyper-params of the configuration file, so you don't need to create a new yaml.
- `-pt` a.k.a `--prompt`: text prompt.
- `-respath` a.k.a `--results_path`: the folder to save results.
- `-d` a.k.a `--seed`: random seed.
- `--download`: download models from huggingface automatically **when you first run them**.

optional:

- `-npt`, a.k.a `--negative_prompt`: negative text prompt.
- `-mv`, a.k.a `--make_video`: make a video of the rendering process (**it will take much longer**).
- `-frame_freq`, a.k.a `--video_frame_freq`: the interval of the number of steps to save the image.
- `-framerate`, a.k.a `--video_frame_rate`: control the playback speed of the output video.

### Case: Ming Dynasty Vase

**Prompt:** A photo of a Ming Dynasty vase on a leather topped table. <br/>
**Style:** iconography <br/>
**Preview:**

| <img src="./img/Icon-MingVase/sample.png" style="width: 250px; height: 250px;"> | <img src="./img/Icon-MingVase/live.svg" style="width: 250px; height: 250px;"> | <img src="./img/Icon-MingVase/finetune.svg" style="width: 250px; height: 250px;"> |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| (a) Sample raster image with Stable Diffusion                                   | (b) Convert raster image to a vector via LIVE                                 | (c) VectorFusion: Fine tune by LSDS                                               |

**Script:**

```shell
python run_painterly_render.py -c vectorfusion.yaml -pt "A photo of a Ming Dynasty vase on a leather topped table. minimal flat 2d vector icon. lineal color. on a white background. trending on artstation" -save_step 50 -respath ./workdir/vase -d 683692
```

### Case: Astronaut

**Prompt:** An astronaut figure. <br/>
**Style:** iconography <br/>
**Preview:**

| <img src="./img/Icon-Astronaut/sample.png" style="width: 250px; height: 250px;"> | <img src="./img/Icon-Astronaut/live.svg" style="width: 250px; height: 250px;"> | <img src="./img/Icon-Astronaut/finetune.svg" style="width: 250px; height: 250px;"> |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| (a) Sample raster image with Stable Diffusion                                    | (b) Convert raster image to a vector via LIVE                                  | (c) VectorFusion: Fine tune by LSDS                                                |

**Script:**

```shell
python run_painterly_render.py -c vectorfusion.yaml -pt "An astronaut figure. minimal flat 2d vector icon. lineal color. on a white background. trending on artstation" -save_step 50 -respath ./workdir/astronaut -d 522178
```

### Case: Guitar

**Prompt:** Electric guitar. <br/>
**Style:** Pixel-Art <br/>
**Preview:**

| <img src="./img/Pixel-Guitar/sample.png" style="width: 250px; height: 250px;"> | <img src="./img/Pixel-Guitar/live.svg" style="width: 250px; height: 250px;"> | <img src="./img/Pixel-Guitar/finetune.svg" style="width: 250px; height: 250px;"> |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| (a) Sample raster image with Stable Diffusion                                  | (b) Convert raster image to a vector via LIVE                                | (c) VectorFusion: Fine tune by LSDS                                              |

**Script:**

```shell
python run_painterly_render.py -c vectorfusion.yaml -pt "Electric guitar. pixel art. trending on artstation" -save_step 50 -respath ./workdir/guitar -update "style=pixelart" -d 445997  
```

### Case: Dragon

**Prompt:** watercolor painting of a firebreathing dragon. <br/>
**Style:** Sketch <br/>
**Preview:**

| <img src="./img/Sketch-Dragon/svg_iter0.svg"> | <img src="./img/Sketch-Dragon/svg_iter500.svg"> | <img src="./img/Sketch-Dragon/finetune.svg"> |
|-----------------------------------------------|-------------------------------------------------|----------------------------------------------|
| SVG initialization                            | VectorFusion fine-tune 500 step                 | VectorFusion fine-tune 1500 step             |

**Script:**

```shell
python run_painterly_render.py -c vectorfusion.yaml -pt "watercolor painting of a firebreathing dragon. minimal 2d line drawing. trending on artstation" -save_step 50 -respath ./workdir/dragon-sketch -update "style=sketch num_segments=5 radius=0.5 sds.num_iter=1500" -d 106764  
```

### Other Cases

```shell
# Sketch style
CUDA_VISIBLE_DEVICES=0 python run_painterly_render.py -c vectorfusion.yaml -pt "watercolor painting of a firebreathing dragon. minimal 2d line drawing. trending on artstation" -save_step 50 -respath ./workdir/dragon-sketch -update "style=sketch skip_live=True num_paths=32 num_segments=5 radius=0.5 sds.num_iter=1500" -rdbz
CUDA_VISIBLE_DEVICES=0 python run_painterly_render.py -c vectorfusion.yaml -pt "A cat. minimal 2d line drawing. trending on artstation" -save_step 50 -respath ./workdir/cat-sketch -update "style=sketch skip_live=True num_paths=32 num_segments=5 radius=0.5 sds.num_iter=1500" -rdbz
```

**More Examples:**

- check the [Examples.md](https://github.com/ximinng/VectorFusion-pytorch/blob/master/Examples.md) for more cases.

**More Scripts:**

- check the [Run.md](https://github.com/ximinng/VectorFusion-pytorch/blob/master/RUN.md) for more scripts.

## Acknowledgement

The project is built based on the following repository:

- [BachiLi/diffvg](https://github.com/BachiLi/diffvg)
- [huggingface/diffusers](https://github.com/huggingface/diffusers)
- [ximinng/DiffSketcher](https://github.com/ximinng/DiffSketcher)

We gratefully thank the authors for their wonderful works.

## Citation

If you use this code for your research, please cite the following work:

```
@inproceedings{jain2023vectorfusion,
  title={Vectorfusion: Text-to-svg by abstracting pixel-based diffusion models},
  author={Jain, Ajay and Xie, Amber and Abbeel, Pieter},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={1911--1920},
  year={2023}
}
@inproceedings{xing2023diffsketcher,
  title={DiffSketcher: Text Guided Vector Sketch Synthesis through Latent Diffusion Models},
  author={XiMing Xing and Chuang Wang and Haitao Zhou and Jing Zhang and Qian Yu and Dong Xu},
  booktitle={Thirty-seventh Conference on Neural Information Processing Systems},
  year={2023},
  url={https://openreview.net/forum?id=CY1xatvEQj}
}
```

## Licence

This repo is licensed under a MIT License.