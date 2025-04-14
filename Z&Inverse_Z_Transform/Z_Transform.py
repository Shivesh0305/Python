import sympy as sp

def compute_z_transform():
    # Define symbols
    n, z = sp.symbols('n z')

    print("Enter the sequence as a function of n (e.g., n**2, 2**n, sin(pi*n)): ")
    user_input = input("Sequence: ")

    try:
        # Parse the user input with proper mapping of math functions to SymPy
        sequence = sp.sympify(user_input, locals={"sin": sp.sin, "cos": sp.cos, "exp": sp.exp, "pi": sp.pi, "sqrt": sp.sqrt})

        # Ensure the sequence is expressed as a function of 'n'
        if not sequence.has(n):
            raise ValueError("The input must be a function of 'n'.")

        # Compute the Z-transform
        z_transform = sp.summation(sequence * z**(-n), (n, 0, sp.oo))

        print("\nZ-Transform of the given sequence:")
        print(z_transform)

    except Exception as e:
        print("\nError in computing Z-transform. Please check your input.")
        print(f"Error details: {e}")

if __name__ == "__main__":
    print("Z-Transform Solver\n")
    compute_z_transform()
