from gammapy.spectrum import SpectrumAnalysis
from gammapy.datasets import gammapy_extra
from astropy.io import fits
from gammapy.extern.pathlib import Path

f = gammapy_extra.filename('test_datasets/spectrum/spectrum_analysis_example.yaml')
ana = SpectrumAnalysis.from_configfile(f)
ana.write_ogip_data(outdir='.')

# TODO : Do not hardcode
for pha in ['pha_run23526.pha', 'pha_run23592.pha']:
    h = fits.open(pha)[1]
    for f in ['RESPFILE', 'ANCRFILE', 'BACKFILE']:
        temp = h.header[f]
        #Replace absolute path with env variable
        ss = 'gammapy-extra'
        pos = temp.find(ss) + len(ss)
        val = temp[pos:-1]
        new = '$GAMMAPY_EXTRA' + val
        h.header[f] = new