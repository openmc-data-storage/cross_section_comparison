# Cross Section Comparison

This repository shows how to make a comparison of a specific reaction for multiple cross section libraries

## ✨ Try it in your browser ✨

👉 [https://openmc-data-storage.github.io/cross_section_comparison/](https://openmc-data-storage.github.io/cross_section_comparison/)

## Install

First install OpenMC

Then install the dependencies

```bash
pip install openmc_data
pip install plotly
```

The clone the repository and change into the repository directory

```bash
git clone https://github.com/openmc-data-storage/cross_section_comparison.git
cd cross_section_comparison
```

## Produce a comparison plot

Run the download data script.

```bash
bash download_data.sh
```

Run the plotting script

```bash
python plot_reaction.py
```
