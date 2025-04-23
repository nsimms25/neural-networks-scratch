# neural-networks-scratch

🔁 Common Activation Functions
1. Sigmoid
 sigmoid(z) = 1 / (1+e^(−z))

    Range: (0, 1)

    Used in: Output layer for binary classification

    Problem: Can cause vanishing gradients in deep networks

Visual: S-shaped curve
2. Tanh (Hyperbolic Tangent)
 tanh(z) = (e^(z) − e^(−z)) / (e^(z) + e^(−z))

    Range: (-1, 1)

    Zero-centered (better than sigmoid in practice)

    Still suffers from vanishing gradients, but less than sigmoid

3. ReLU (Rectified Linear Unit)
 ReLU(z)=max⁡(0,z)

    Range: [0, ∞)

    Very common in hidden layers

    Fast to compute

    Issue: “Dying ReLU” — neurons can get stuck and always output 0