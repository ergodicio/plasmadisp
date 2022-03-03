# MIT License
#
# Copyright (c) 2022 Ergodic LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import numpy as np

from tests.extras import canosa_values
from plasmadisp.electrostatic import get_roots_to_electrostatic_dispersion


def test_z_solver():
    k0 = canosa_values.k0
    w_real_actual = canosa_values.w_real
    w_imag_actual = canosa_values.w_imag

    for kk, wr, wi in zip(k0, w_real_actual, w_imag_actual):
        answer = get_roots_to_electrostatic_dispersion(wp_e=1.0, vth_e=1.0, k0=kk)

        np.testing.assert_almost_equal(wr + 1j * wi, answer, decimal=4)
