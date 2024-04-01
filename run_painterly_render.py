# -*- coding: utf-8 -*-
# Author: ximing
# Description: the main func of this project.
# Copyright (c) 2023, XiMing Xing.
# License: MIT License

import os
import sys
import argparse
from datetime import datetime
import random
import ast
from typing import Any, List
from functools import partial

from accelerate.utils import set_seed
import omegaconf

sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0])

from libs.engine import merge_and_update_config
from libs.utils.argparse import accelerate_parser, base_data_parser


def render_batch_wrap(args: omegaconf.DictConfig,
                      seed_range: List,
                      pipeline: Any,
                      **pipe_args):
    start_time = datetime.now()
    for idx, seed in enumerate(seed_range):
        args.seed = seed  # update seed
        print(f"\n-> [{idx}/{len(seed_range)}], "
              f"current seed: {seed}, "
              f"current time: {datetime.now() - start_time}\n")
        pipe = pipeline(args)
        pipe.painterly_rendering(**pipe_args)


def main(args, seed_range):
    args.batch_size = 1  # rendering one SVG at a time

    render_batch_fn = partial(render_batch_wrap, args=args, seed_range=seed_range)

    from pipelines.painter.VectorFusion_pipeline import VectorFusionPipeline

    if args.path_schedule == 'list' and not isinstance(args.schedule_each, omegaconf.ListConfig):
        args.schedule_each = ast.literal_eval(args.schedule_each)
    if not isinstance(args.sds.t_range, omegaconf.ListConfig):
        args.sds.t_range = ast.literal_eval(args.sds.t_range)

    if not args.render_batch:
        pipe = VectorFusionPipeline(args)
        pipe.painterly_rendering(args.prompt)
    else:  # generate many SVG at once
        render_batch_fn(pipeline=VectorFusionPipeline, text_prompt=args.prompt)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="vectorfusion rendering",
        parents=[accelerate_parser(), base_data_parser()]
    )
    # config
    parser.add_argument("-c", "--config",
                        required=True, type=str,
                        default="vectorfusion.yaml",
                        help="YAML file for configuration.")
    # prompt
    parser.add_argument("-pt", "--prompt", default="A horse is drinking water by the lake", type=str)
    parser.add_argument("-npt", "--negative_prompt", default="", type=str)
    # DiffSVG
    parser.add_argument("--print_timing", "-timing", action="store_true",
                        help="set print svg rendering timing.")
    # diffuser
    parser.add_argument("--download", action="store_true",
                        help="download models from huggingface automatically.")
    parser.add_argument("--force_download", "-download", action="store_true",
                        help="force the models to be downloaded from huggingface.")
    parser.add_argument("--resume_download", "-dpm_resume", action="store_true",
                        help="download the models again from the breakpoint.")
    # rendering quantity
    # like: python main.py -rdbz -srange 100 200
    parser.add_argument("--render_batch", "-rdbz", action="store_true")
    parser.add_argument("-srange", "--seed_range",
                        required=False, nargs='+',
                        help="Sampling quantity.")
    # visual rendering process
    parser.add_argument("-mv", "--make_video", action="store_true",
                        help="make a video of the rendering process.")
    parser.add_argument("-frame_freq", "--video_frame_freq",
                        default=1, type=int,
                        help="video frame control.")
    parser.add_argument("-framerate", "--video_frame_rate",
                        default=24, type=int,
                        help="by adjusting the frame rate, you can control the playback speed of the output video.")
    args = parser.parse_args()

    # set the random seed range
    seed_range = None
    if args.render_batch:
        # random sampling without specifying a range
        start_, end_ = 1, 1000000
        if args.seed_range is not None:  # specify range sequential sampling
            seed_range_ = list(args.seed_range)
            assert len(seed_range_) == 2 and int(seed_range_[1]) > int(seed_range_[0])
            start_, end_ = int(seed_range_[0]), int(seed_range_[1])
            seed_range = [i for i in range(start_, end_)]
        else:
            # a list of lengths 1000 sampled from the range start_ to end_ (e.g.: [1, 1000000])
            numbers = list(range(start_, end_))
            seed_range = random.sample(numbers, k=1000)

    args = merge_and_update_config(args)

    set_seed(args.seed)
    main(args, seed_range)
