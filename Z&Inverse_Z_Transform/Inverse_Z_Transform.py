import sympy as sp

def compute_inverse_z_transform():
    # Define symbols
    n, z = sp.symbols('n z')

    print("Enter the Z-transform as a function of z (e.g., 1/(1 - 0.5*z**(-1)), z/(z - 2)): ")
    user_input = input("Z-Transform: ")

    try:
        # Parse the user input
        z_transform = sp.sympify(user_input)

        # Perform partial fraction decomposition (if necessary)
        partial_fractions = sp.apart(z_transform, z)

        print("\nPartial Fraction Decomposition:")
        print(partial_fractions)

        # Manually compute inverse Z-transform using residues
        terms = sp.Add.make_args(partial_fractions)
        inverse_transform = 0

        for term in terms:
            residue, pole = sp.fraction(term)
            if pole.has(z):
                pole_root = sp.roots(pole, z)
                if len(pole_root) == 1:
                    root = list(pole_root.keys())[0]
                    coeff = residue.subs(z, root)
                    inverse_transform += coeff * (root ** n)

        print("\nInverse Z-Transform of the given Z-transform (in terms of n):")
        print(inverse_transform)

    except Exception as e:
        print("\nError in computing inverse Z-transform. Please check your input.")
        print(f"Error details: {e}")

if __name__ == "__main__":
    print("Inverse Z-Transform Solver\n")
    compute_inverse_z_transform()
