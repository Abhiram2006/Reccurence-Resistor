# Reccurent Resistor Networks

Extrapolating limits for Delta-Y transformation based Resistor Networks.

Question from OPhO 2022.

<img width="926" alt="Screenshot 2022-07-31 at 5 08 23 PM" src="https://user-images.githubusercontent.com/65448559/182024484-a8f5626d-a248-4557-832c-b287318c10e0.png">



## Method Approached

Notably, we can slowly perform Delta-Y transformations and just keep appending to a strand of resistors. Thus, we can first draw out the first Delta, which starts at **a**.

$$R_{strand} = \frac{R_b R_c}{\sum R}$$

We also keep alternately adding 1 ohm to each of the other resulting connections due to the 1 ohm connections.

Thus, for any resistor network of size $n$, we perform Delta-Y at $2n$ times.

## Results
![Loss Curve](./loss_curve.png)

This was the computed loss curve for $\frac{R_{eff}}{n}$.
