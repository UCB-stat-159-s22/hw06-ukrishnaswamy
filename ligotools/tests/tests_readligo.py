import ligotools
from ligotools import readligo as rl
from ligotools import utils

import matplotlib.mlab as mlab
import numpy as np

from scipy import signal
from scipy.interpolate import interp1d
from scipy.io import wavfile
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz

import json
import h5py
import os
import pytest

fnjson = "BBH_events_v3.json"

events = json.load(open('data/' + fnjson,"r"))

event = events['GW150914']
eventname = 'GW150914'

fn_H1 = event['fn_H1']
fn_L1 = event['fn_L1']
tevent = event['tevent']            # Set approximate event GPS time
fband = event['fband']     

fs = event['fs']  
NFFT = 4*fs

strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/' + fn_H1, 'H1')
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
psd_H1 = interp1d(freqs, Pxx_H1)


# readligo 4 tests

def test_readdatainstance():
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
	
	isinstance(strain_H1, np.ndarray)
	isinstance(time_H1, np.ndarray)
	isinstance(chan_dict_H1, dict)


def test_shapes():
	strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
	
	assert strain_H1.shape == strain_L1.shape 
	
def test_dictionary():
	strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
	
	chan_dict_L1.keys() == chan_dict_H1.keys()
	
def test_time():
	strain_L1, time_L1, chan_dict_L1 = rl.loaddata(fn_L1, 'L1')
	strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
	
	assert (time_L1 == time_H1).all()
	

# utils tests

def test_whiten():
	strain_H1_whiten = utils.whiten(strain_H1,psd_H1,0.000244140625)
	isinstance(strain_H1_whiten, np.ndarray)
	
	
def test_reqshift():
	strain_H1_whiten = utils.whiten(strain_H1,psd_H1,0.000244140625)
	
	fs = 4096
	fshift = 400.
	
	array_reqshift = utils.reqshift(strain_H1_whiten, fshift, fs)
	
	assert min(array_reqshift) == -317.81028383942373
	assert np.count_nonzero(array_reqshift) == len(array_reqshift)
	
	
def test_write_wavfile():
	strain_H1_whiten = utils.whiten(strain_H1,psd_H1,0.000244140625)
	utils.write_wavfile('GW150914', 4096, strain_H1_whiten)
	read_in = wavfile.read('GW150914')
	
	assert read_in[0] == 4096
	
	isinstance(read_in[1], np.ndarray)
	
	os.remove('GW150914')
