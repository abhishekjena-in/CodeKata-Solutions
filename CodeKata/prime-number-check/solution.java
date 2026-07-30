import java.util.Scanner;
public class Main {
    public boolean checkPrime(int num){
        if(num<=1) return false;
        
        for(int i=2; i*i<=num; i++)
        {
            if(num % i ==0) return false;
        }
        
        return true;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        Main obj = new Main();
        boolean res = obj.checkPrime(num);
        if(res) System.out.println("yes");
        else System.out.println("no");
    }
}