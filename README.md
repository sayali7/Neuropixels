# Neuropixels
Load, save, plot raw and Kilosort neuropixels data with Neuropyxels.
Some files from the original npyx (NeuroPyxels) library [[1]](#1) have been modified to according to our data.

## Folder structure for dp:
- Kilosort output files from "imec_specs"
- \*.imec0.bin file (already present in imec_specs for all 4 sessions). To load one session, replace this with the recordings from individual sessions, e.g.:"Kavorka_190620/26525_kavorka_190620_1835_intermediate_s1_light/recording/*.bin"
- \*.imec0.meta file (needs to be copied from one of the sessions), for e.g.: "Kavorka_190620/26525_kavorka_190620_1835_intermediate_s1_light/recording/*.meta" 
  
## References
<a id="1">[1]</a> 
NeuroPyxels: loading, processing and plotting Neuropixels data in python"
doi: 10.5281/zenodo.5509733 [Link](https://github.com/m-beau/NeuroPyxels/tree/master)
