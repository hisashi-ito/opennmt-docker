#! /bin/sh
MODEL=$1
GPU="0"
th ./tools/release_model.lua -model ${MODEL} -output_model ${MODEL}.cpu -gpuid ${GPU} -fallback_to_cpu
