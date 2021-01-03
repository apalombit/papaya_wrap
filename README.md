# Papaya wrap

Script wraps papaya to use for quick check of image registration results.

Use case: you just completed a registration step, say T1w-MRI to CT and want to check without external viewer how well these are aligned.

It includes all configuration from a template html, default is simple overlay with a quick toggle button altering overlay transparency.

## Why this?

You just completed one/many registrations between two 3D volumes (here example is CT vs 3D-T1w-MRI) and need to check quickly alignment is ok without pulling all the dataset to local (or no suitable viewer available).

Adding a line of code to call this wrapper after each registration provides a self-contained registration qc - like similar approaches with animation but with nice viewer capabilities.

Different modalities and checks are easy to configure defining a different html template (or scripting template generation in a notebook?).


## Usage example

`python3 gen_view.py --bg ${dataset}/T1.nii.gz --fg ${dataset}/CT.nii.gz --out ${dataset}/build_out/ --browser open`


## Installation
### Linux and MacOS
On a fresh python3 virtual environment install `papaya_wrap` via

`git clone https://github.com/apalombit/papaya_wrap.git`

Dependencies (from Papaya) include JVM7 etc... (see Papaya page: https://github.com/rii-mango/Papaya)
