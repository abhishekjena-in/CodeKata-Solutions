import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        long N = sc.nextLong();
        if(N % 7 ==0) System.out.println("yes");
        else System.out.println("no");
    }
}