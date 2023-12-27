// Java program to calculate pow(x,n)

class GFG {
	/* Function to calculate x raised to the power y */
	static int power(int x, int y)
	{
		if (y == 0)
			return 1;
		else if (y % 2 == 0)
			return power(x, y / 2) * power(x, y / 2);
		else
			return x * power(x, y / 2) * power(x, y / 2);
	}

	// Driver code
	public static void main(String[] args)
	{
		int x = 2;
		int y = 3;

		// Function call
		System.out.printf("%d", power(x, y));
	}
}

// This code is contributed by Smitha Dinesh Semwal
