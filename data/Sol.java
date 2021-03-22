import java.util.*;

public class Sol {
public static void main(String[] args){
        int a[] = new int[11];
        Scanner sc = new Scanner(System.in);
        int i, j,k,mi,n;

        for(i=0; i<11; i++) {
                a[i] = sc.nextInt();
        }

        k = a[0];
        j = 1;
        int m = 0;
        int hops=0;
        while(j < 11) {
                n = m;
                mi = -1;
                for(int q =1; q<=k; q++) {
                        if(a[m+q] >= mi) {
                                mi = a[m+q];
                                n = q;
                        }
                }
                j = j+n;
                m = m+n;
                k = a[m];
                hops++;
                if(j+mi >= 11)
                        break;
        }

        System.out.println(hops+1);
}
}
