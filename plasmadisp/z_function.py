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
import scipy


def plasma_dispersion(value):
    """
    This function leverages the Fadeeva function in scipy to calculate the Z function

    :param value:
    :return:
    """
    return scipy.special.wofz(value) * np.sqrt(np.pi) * 1j


def plasma_dispersion_prime(value):
    """
    This is a simple relation for Z-prime, which happens to be directly proportional to Z

    :param value:
    :return:
    """
    return -2.0 * (1.0 + value * plasma_dispersion(value))


def get_roots_to_electrostatic_dispersion(wp_e, vth_e, k0, maxwellian_convention_factor=2.0, initial_root_guess=None):
    """
    This function calculates the root of the plasma dispersion relation

    :param wp_e:
    :param vth_e:
    :param k0:
    :param maxwellian_convention_factor:
    :param initial_root_guess:
    :return:
    """
    from scipy import optimize

    plasma_epsilon, initial_root_guess = get_dispersion_function(
        wp_e, vth_e, k0, maxwellian_convention_factor, initial_root_guess
    )

    epsilon_root = optimize.newton(plasma_epsilon, initial_root_guess)

    return epsilon_root * k0 * vth_e * np.sqrt(maxwellian_convention_factor)


def get_dispersion_function(wp_e, vth_e, k0, maxwellian_convention_factor=2.0, initial_root_guess=None):
    """
    This function calculates the root of the plasma dispersion relation

    :param wp_e:
    :param vth_e:
    :param k0:
    :param maxwellian_convention_factor:
    :param initial_root_guess:
    :return:
    """
    if initial_root_guess is None:
        initial_root_guess = np.sqrt(wp_e**2.0 + 3 * (k0 * vth_e) ** 2.0)

    chi_e = np.power((wp_e / (vth_e * k0)), 2.0) / maxwellian_convention_factor

    def plasma_epsilon(x):
        val = 1.0 - chi_e * plasma_dispersion_prime(x)
        return val

    return plasma_epsilon, initial_root_guess


def get_depsdw(kld):
    wax = np.linspace(1.0, 1.5, 2048)
    eps = 1 - 1.0 / wax**2.0 - 3 * 1 / wax**2.0 * (kld / wax) ** 2.0

    disp_fn, wrg = get_dispersion_function(1.0, 1.0, kld)

    disp_arr = np.array([np.real(disp_fn((val) / (kld * 1.0 * np.sqrt(2.0)))) for val in wax])

    ddisp = np.gradient(disp_arr, wax[2] - wax[1])
    deps = np.gradient(eps, wax[2] - wax[1])

    wr = np.real(
        get_roots_to_electrostatic_dispersion(1.0, 1.0, kld, maxwellian_convention_factor=2.0, initial_root_guess=None)
    )

    iw = np.argmin(np.abs(wax - wr))

    return ddisp[iw], deps[iw]
