#!/usr/bin/env bash

pip install openmc_data

convert_fendl --release 3.2
convert_fendl --release 3.1d
convert_fendl --release 3.1a
convert_fendl --release 3.0
convert_fendl --release 2.1

convert_jeff32
convert_jeff33

download_endf b7.1
download_endf b8.0

download_tendl 2019
download_tendl 2021