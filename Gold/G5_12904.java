# A와 B, 2023년 11월 29일 22:19:43, 14236kb, 140ms, 650b
import java.io.*;

public class Main {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder S,T;
	static int sLen, tLen;
	
	public static void main(String args[]) throws IOException {
		S=new StringBuilder(input.readLine());
		T=new StringBuilder(input.readLine());
		
		sLen=S.length();
		tLen=T.length();
		
		game();
	}
	
	public static void game() {
		while(sLen!=tLen--) {
			if(T.charAt(tLen)=='A') {
				T.deleteCharAt(tLen);
			}else {
				T.deleteCharAt(tLen);
				T.reverse();
			}
		}
		if(T.toString().equals(S.toString())) System.out.println(1);
		else 			System.out.println(0);
	}
}
