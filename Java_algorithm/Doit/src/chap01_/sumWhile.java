package chap01_;

import java.util.Scanner;

public class sumWhile {

	// a와 b 사이의 모든 정수의 합 출력
	static int sumof(int a, int b) {
		int result = 0 ;
		if (a < b)
			for( ; a <= b ; a++) {
				result += a;
			} // for end
		else if (a > b) // a : 6, b : 4
			for( ; b <= a ; b++) {
				result += b;
			} // for end
		else return 0;
		return result;
	}	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("a부터 b까지의 합을 구합니다.");
		System.out.print("a의 값 : "); int num1 = sc.nextInt();
		System.out.print("b의 값 : "); int num2 = sc.nextInt();
		
		System.out.println("a, b사이의 모든 정수의 합 : " + sumof(num1, num2));
		
		/* 1 + 2 + 3 = 6의 형식으로 출력
		int sum = 0, i = 1;
		for ( ; i < num; i++) {
			sum += i;
			System.out.print(i + " + ");
		}
		sum += i;
		System.out.print(i + " = " + sum);
		*/
		
		/* 가우스 덧셈. (1+n)*5 : 1부터 n까지의 합.
		int result;
		result = (1 + num) * 5;
		System.out.println(result);
		*/
	}

}
