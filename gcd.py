def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Main function
def main():
    try:
        # Prompt the user to enter two integers
        A = int(input("Enter the first integer (A): "))
        B = int(input("Enter the second integer (B): "))

        # Compute the GCD of the two numbers
        gcd = compute_gcd(A, B)

        # Display the result
        print(f"The GCD of {A} and {B} is: {gcd}")

    except ValueError:
        print("Please enter valid integers.")


# Correctly call the main function
if __name__ == "__main__":
    main()