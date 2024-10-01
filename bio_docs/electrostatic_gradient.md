# Electrostatic Gradient

Bept utilises `numpy.gradient` to calculate the gradient of the grid box which encloses the protein. The function traditionally calculates the gradient of an N-dimensional array.

Let's understand the concept of gradient in the context of electrostatics.

## Gradient Calculation

The gradient is computed using second order accurate central differences in the interior points and either first or second order accurate one-sides (forward or backwards) differences at the boundaries.

It takes four parameters:
`numpy.gradient(f, \*varargs, axis=None, edge_order=1)`

- **f**: N-dimensional array containing samples of a scalar function.
- **varargs**: list of scalar or array, optional
- **axis**: None or int or tuple of ints, optional
- **edge_order**: {1, 2}, optional

### The Formula:

The definition of a derivative is `f'(x) = (f(x+h)-f(x))/h` (forward difference) or you can take say `f'(x) = (f(x+h)-f(x-h))/(2h)` (central difference).

We can calculate the derivatives easily when the value of h is small enough (curve is smooth). However, things become a bit tricky if we do not know the function and only some values of x and its corresponding f(x). Then our best guess for h is not tiny but identical to the spacing between neighboring x values.

For the values in the middle we can use central difference, forward difference at starting and leftmost difference at end values.

Effectively any point has a hd (the forward step size) and a hs (the backward step size) and the formula is not just (f(x+h<sub>d</sub>)-f(x-h<sub>s</sub>))/(h<sub>d</sub>+h<sub>s</sub>) but instead that bigger expression given in the documentation, where the values of h<sub>d</sub> and h<sub>s</sub> act as some kind of weights. np.gradient is backwards, central, and forward difference combined.

Let h<sub>\*</sub> be a non-homogeneous step size, we minimize the “consistency error” `nf*i(x*{i+1})` between the true gradient and its estimate from a linear combination of the neighboring grid-points:

```latex
$$n_i = f_i^{(1)} - [a f(x_i) + b f(x_i+h_d) + c f(x_i-h_s)]$$
```

Given that finite differences do work out, this approach should work as well and generalize the idea. Expand f(x+hd) and f(x-hs) with their Taylor series:

```latex
$$f(x+h_d) = f(x) + h_d f'(x) + h_d^2 f''(x)/2 + ...$$ $$f(x-h_s) = f(x) - h_s f'(x) + h_s^2 f''(x)/2 + ...$$
```

We get the following equations after substitution:

```latex
$$a+b+c = 0$$
$$bh_d-ch_s = 1$$
$$bh_d^2 + ch_s^2 = 1$$
```

Resulting approximation of f<sub>i</sub><sup>(1)</sup> is:

```latex
$$f_i^{(1)} = {h_s^2f(x_{i} + h_d) + (h_d^2 - h_s^2)f(x_i)- h_d^2f(x_{i} - h_s) \over h_sh_d(hs+h_d)} + O({h_sh_d^2 + h_dh_s^2 \over h_s + h_d})$$
```

If we consider h<sub>s</sub> = h<sub>d</sub> (data is evenly spaced) then we get:

```latex
$$f_i^{(1)} = {f(x_{i+1}) - f(x_{i-1}) \over 2h} + O(h^2)$$
```

### Implementation

- Creating Grid: We extract the values of grid dimensions n<sub>x</sub>, n<sub>y</sub> and n<sub>z</sub> from our file and use numpy.meshgrid to generate a 3-D grid using array.

- Computing Potential: The potential function is vectorized using numpy.vectorize, allowing it to compute the potential over all grid points simultaneously.

- Computing Field: The potential gradient is computed using numpy.gradient. Since the electric field is the negative gradient of the potential, the gradients in the x, y, and z directions are negated.

The function returns the x, y, and z components of the electric field (Ex, Ey, Ez).
