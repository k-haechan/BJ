# 구간 합 구하기 4, 2023년 11월 28일 01:04:22, 67220kb, 1856ms, 744b
import java.util.*;
import java.io.*;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] n_m=br.readLine().split(" ");
		
		int n=Integer.parseInt(n_m[0]);
		int m=Integer.parseInt(n_m[1]);
		
		String[] str_input=br.readLine().split(" ");
		int[] sum_input = new int[n+1];
		sum_input[0]=0;//Integer.parseInt(str_input[0]);
		
		for(int i=1;i<n+1;i++) {
			sum_input[i]=Integer.parseInt(str_input[i-1]) + sum_input[i-1];
		}
		
		for(int x=0;x<m;x++) {
			String[] tmp=br.readLine().split(" ");
			int i=Integer.parseInt(tmp[0]);
			int j=Integer.parseInt(tmp[1]);
			System.out.println(sum_input[j]-sum_input[i-1]);
		}
	}
}
