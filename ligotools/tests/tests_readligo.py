from ligotools import readligo as rl
from ligotools import utils
import matplotlib.mlab as mlab
from scipy import signal
from scipy.interpolate import interp1d
import json
import pytest

fnjson = "BBH_events_v3.json"

events = json.load(open(fnjson,"r"))

event = events[eventname]

strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, 'H1')
Pxx_H1, freqs = mlab.psd(strain_H1, Fs = fs, NFFT = NFFT)
psd_H1 = interp1d(freqs, Pxx_H1)


# # utils tests

# def test_whiten():
# 	strain_H1_whiten = whiten(strain_H1,psd_H1,0.000244140625)
# 	isinstance(strain_L1_whitenbp, np.ndarray)
	
	
# def test_reqshift():
# 	strain_H1_whiten = whiten(strain_H1,psd_H1,0.000244140625)
	
# 	fs = 4096
# 	fshift = 400.
	
# 	array_reqshift = reqshift(strain_H1_whiten, fshift, fs)
	
# 	assert min(array_reqshift) == -317.81028383942373
# 	assert np.count_nonzero(array_reqshift) == len(array_reqshift)
	
# def test_plotty():
	
	

# def test_write_wavfile():
# 	strain_H1_whiten = whiten(strain_H1,psd_H1,0.000244140625)
#     utils.write_wavfile('GW150914', 4096, strain_H1_whiten)
#     read_in = wavfile.read('GW150914')
# 	assert read_in[0] == 4096
# 	isinstance(read_in[1], numpy.ndarray)
#     os.remove('GW150914')


# readligo 4 tests

# def test