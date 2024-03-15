# 숫자의 합, 2023년 11월 27일 18:09:34, 14276kb, 128ms, 412b
// 숫자의 합 구하기
import java.io.*;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n=Integer.parseInt(br.readLine());
		
		String number=br.readLine();
		char[] cNum=number.toCharArray();

		int sum=0;
		for(int i=0;i<n;i++) {
			sum+=cNum[i]-'0';
		}
		System.out.println(sum);
	}
}
	

