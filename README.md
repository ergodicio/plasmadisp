## What does this do?
This package calculates the roots to the electrostatic dispersion relation given by 

$$ 1 + \frac{\omega_p^2}{k^2} \int du \frac{d_u g(u)}{\omega/k - u} = 0$$ 

where $$g(u)$$ is the 1D distribution function in the direction $$u$$.

## Installation & Usage
To install, after activating your environment, run

```shell
pip3 install -e git+https://github.com/ergodicio/plasmadisp.git#egg=plasmadisp
```

Then, you can simply

```python
from plasmadisp import electrostatic
kk = 0.3
answer = electrostatic.get_roots_to_electrostatic_dispersion(wp_e=1.0, vth_e=1.0, k0=kk)
print(answer)
```

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

