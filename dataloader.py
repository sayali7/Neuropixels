import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
from npyx import *



class NeuroLoader():
    """
    Dataloader wrapper to load neuropixels data from kilosort output files using npyx. Refer to official npyx 
    documentation for more details and additional functions.
    """
    def __init__(self,BASE_PATH):
        self.BASE_PATH=BASE_PATH
        self.meta=read_metadata(self.BASE_PATH)
        self.fs=self.meta['highpass']['sampling_rate']
        
        print(f"Neuropixels probe {self.meta['probe_version']} acquired with {self.meta['acquisition_software']}.")
        print(f"Highpass filtered data at {self.meta['highpass']['binary_relative_path']} was acquired at {self.fs} Hz.")
        
        
    def load_units(self,file_name="cluster_KSLabel.tsv", group_col="KSLabel",quality="all"):
        """
        get list of units from 
        params:
        file_name: str, file containing cluster information outoput from Kilosort (e.g., cluster*.tsv)
        group_col: str, column name containing cluster ids in the file_name file 
        quality: str, either one of ["all", "good", "mua", "noise", "unsorted"]. Default: "all"
        
        return: 
        array of unit ids
        """
        units = get_units(self.BASE_PATH,f=file_name, group_col=group_col,quality=quality)
        return units
    
    def get_spike_times_for_unit(self,unit_id):
        """
        get spike times of the unit in samples and seconds
        params:
        unit_id: int, id of unit 
        
        return:
        spike times in samples and seconds
        """
        t = trn(self.BASE_PATH, unit_id) # t: spike times for unit 'u' in samples
        print(f"Neuron {unit_id} has {t.shape[0]} spikes across 4 sessions")
        t_fs = t / self.fs
        return t,t_fs
    
    def get_waveforms_for_unit(self,unit_id,t_waveforms=82, n_waveforms=100):
        """
        params:
        unit_id: int, id of unit
        n_waveforms: int, number of waveform to return, selected according to the periods parameter. Default 100
        t_waveforms: int, temporal span of waveforms. Default 82 (about 3ms)
        
        return:
        waveforms: 3-D array of shape #spikes(n_waveforms)*#samples(t_waveforms)*channels
        peak_channel: waveform on peak channel of the unit_id
        """
        waveforms = wvf(self.BASE_PATH, unit_id, t_waveforms=t_waveforms, n_waveforms=n_waveforms) 
        spikes, samples, channels = waveforms.shape
        print(f"waveform extracted is an array of shape {spikes} spikes by {samples} samples (time) by {channels} channels.")
        
        peak_channel = waveforms.mean(0).max(0).argmax()
        print (f"Peak channel for unit {unit_id} is: {peak_channel}")
        print(f"We define the peak channel as the channel with maximum amplitude")
        
        return waveforms,peak_channel

    def extract_raw_recording_chunk(self, times, channels=np.arange(384)):
        """
        params:
        times: list, time interval (seconds) over which to extract waveform. Default [0,0.07]
        channels: list, channel numbers for which to extract raw recordings
        
        returns:
        2-D array containing raw recording chunk of size #channels*#samples
        """
                
        raw_data_chunk = extract_rawChunk(self.BASE_PATH, times, channels=channels)
        channels, samples = raw_data_chunk.shape
        print(f"extract_rawChunk() returns an array of shape {channels} channels x {samples} samples ({round(samples/30)}ms)")
        return raw_data_chunk
    
    
    def plot_raw_recording_chunk(self, units, times=[0,0.07], channels = np.arange(50), figsize=(6,10), 
                                 offset=450,  Nchan_plot=10):
        """
        plot raw recording for specified units over specified channels and time interval (refer to official
        npyx documentation for additional arguments to the function)
        
        params:
        times: list, time interval (seconds) over which to extract waveform. Default [0,0.07]
        units: list of units to plot and color across channels
        channels: list, channel numbers for which to extract raw recordings
        offset: graphical offset between channels, in uV (ise to scale up/down in y). Default 450
        Nchan_plot: int, number of channels over which to plot colored unit spikes. Default 10
        """
        fig = plot_raw_units(self.BASE_PATH, times=times, units = units, channels = channels,
                             figsize=figsize,offset=offset,  Nchan_plot=Nchan_plot)

        