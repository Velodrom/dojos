Implement a digital FIR filter of the form

y[n] = Sum_{k=0...N-1}(h[k]*x[n-k]),

where N=4 is the filter length.
The filter coefficients are h=[0.5, 0.3, 0.2, 0.1]

Input x[n] is a vector of real valued floating point numbers. The input vector can be of any length.
Output y[n] is a vector of the filtered values.



