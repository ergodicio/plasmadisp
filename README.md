## What does this do?
This package calculates the roots to the electrostatic dispersion relation given by 

<img src="https://render.githubusercontent.com/render/math?math={\color{white}1+\frac{\omega_p^2}{k^2} \int du \frac{d_u g(u)}{\omega/k - u} = 0}#gh-dark-mode-only">

where <img src="https://render.githubusercontent.com/render/math?math=g(u)"> is the 1D distribution function, here assumed
to be a Maxwell-Boltzmann.

## Installation & Usage
To install, after activating your environment, run

```shell
pip3 install -e git+https://github.com/ergodicio/plasmadisp.git#egg=plasmadisp
```

Then, you can

```python
from plasmadisp import electrostatic
kk = 0.3
answer = electrostatic.get_roots_to_electrostatic_dispersion(wp_e=1.0, vth_e=1.0, k0=kk)
print(answer)
```
where the temperature and density of the plasma can be inserted by varying the plasma frequency and thermal velocity. 
For more on this, please refer to an introductory plasma physics textbook like Chen [2] or Bellan [3].

This will print a complex number where the real part is the resonant mode and the imaginary part is the Landau damping 
rate of that mode

## Tests
The results of this solver are tested against the values published in Canosa1973 [1]

## Solver
This uses `scipy`'s optimize functionality as well as it's Fadeeva special function to represent the plasma dispersion.

## Contribute/Questions
Please start an issue if you have any questions or would like to make contributions. At the moment, this package is 
intentionally limited in scope.


[1]: Canosa, José. “Numerical Solution of Landau’s Dispersion Equation.” Journal of Computational Physics 13, no. 1 (September 1973): 158–60. https://doi.org/10.1016/0021-9991(73)90131-9.
[2]: Chen, Francis F. Introduction to Plasma Physics and Controlled Fusion. Boston, MA: Springer US, 1984. https://doi.org/10.1007/978-1-4757-5595-4.
[3]: Bellan, P. M. Fundamentals of Plasma Physics. Vol. 173, n.d. https://doi.org/10.2277/0521821169.