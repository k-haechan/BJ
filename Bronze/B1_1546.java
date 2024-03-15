# 평균, 2023년 11월 27일 18:30:33, 14316kb, 128ms, 478b
import java.io.*;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String[] records = br.readLine().split(" ");
		float avrg=0;
		int max=0;
		for(int i=0;i<n;i++) {
			int record=Integer.parseInt(records[i]);
			if(max<record)
				max=record;
			avrg+=record;
		}
		avrg=(avrg*100)/(max*n);
		System.out.println(avrg);
	}
}
