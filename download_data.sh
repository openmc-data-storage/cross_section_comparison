#!/usr/bin/env bash

pip install openmc_data

convert_fendl --release 3.2
convert_fendl --release 3.1d
convert_fendl --release 3.1a
convert_fendl --release 3.0
convert_fendl --release 2.1

convert_jeff32 --temperatures 293
convert_jeff33 --temperatures 293

download_endf --release b7.1
download_endf --release b8.0

download_tendl --release 2019
download_tendl --release 2021