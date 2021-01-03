# Papaya wrap

Script wraps papaya to use for quick check of image registration results.

Use case: you just completed a registration step, say T1w-MRI to CT and want to check without external viewer how well these are aligned.

It includes all configuration from a template html, default is simple overlay with a quick toggle button altering overlay transparency.


## Usage example

`python3 gen_view.py --bg ${dataset}/T1.nii.gz --fg ${dataset}/CT.nii.gz --out ${dataset}/build_out/ --browser open`


## Installation
### Linux and MacOS
On a fresh python3 virtual environment install `papaya_wrap` via

`git clone https://github.com/apalombit/papaya_wrap.git`

Dependencies (from Papaya) include JVM7 etc... (see Papaya page: https://github.com/rii-mango/Papaya)
