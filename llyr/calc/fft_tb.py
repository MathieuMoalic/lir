import numpy as np

from ..base import Base


class fft_tb(Base):
    def calc(
        self,
        dset: str,
        tmax: int = None,
        tmin: int = None,
        tstep: int = 1,
        normalize: bool = False,
    ):
        y = self.m[f"table/{dset}"][slice(tmin, tmax, tstep)]
        ts = self.m["table/t"][:]
        table_dt = (ts[-1] - ts[0]) / len(ts)
        x = np.fft.rfftfreq(y.shape[0], table_dt * tstep) * 1e-9
        y -= y[0]
        y -= np.average(y)
        y = np.multiply(y, np.hanning(y.shape[0]))
        y = np.fft.rfft(y)
        y = np.abs(y)
        if normalize:
            y /= y.max()
        return x, y
