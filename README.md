# Neuropixels
Load, save, and plot raw neuropixels data and Kilosort outputs with Neuropyxels.
Some files from the official npyx (NeuroPyxels) library [[1]](#1) have been modified to suit our data.
Check the original library for additional details on post-processing like high-pass filtering, etc.

## Tutorial to load, plot, and get raw traces from Neuropixels recordings: 
Load_Neuropixels_data_with_Neuropyxels.ipynb

### Folder structure to specify path to load data from ('dp' in notebook) :
- Kilosort output files from "imec_pec" (extracted, not .zip)
- \*.imec0.bin file (already present in imec_pec, which is a concatenated version of \*imec0.bin files from all 4 sessions). To load one session, replace this with the recordings from individual sessions, e.g.:"Kavorka_190620/26525_kavorka_190620_1835_intermediate_s1_light/recording/*.bin"
- \*.imec0.meta file (needs to be copied from one of the sessions), for e.g.: "Kavorka_190620/26525_kavorka_190620_1835_intermediate_s1_light/recording/*.meta"

### Requirements
Tested on Ubuntu 22.04

Install npyx (refer to npyx [[1]](#1) for additional installation instructions/support).
```python
pip install npyx
```
- python 3.10
- joblib 1.3.1
- numpy 1.24.4
- opencv 4.8.0
  
## References
<a id="1">[1]</a> 
NeuroPyxels: loading, processing and plotting Neuropixels data in python"
doi: 10.5281/zenodo.5509733 [Link](https://github.com/m-beau/NeuroPyxels/tree/master)
