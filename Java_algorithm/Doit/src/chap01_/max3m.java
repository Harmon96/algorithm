package chap01_;

public class max3m {

	static int max3(int a, int b, int c) {
		int max = a;
		if (b > max)
			max = b;
		if (c > max)
			max = c;
		
		return max;
	}
	
	public static void main(String[] args) {

		System.out.println(max3(3, 5, 7));
		System.out.println(max3(5, 3, 7));
		System.out.println(max3(7, 5, 3));

	}

}
