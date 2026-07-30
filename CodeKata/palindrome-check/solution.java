import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int i = 0;
        int j = s.length()-1;
        boolean flag = true;
        while(i<j)
        {
            if(s.charAt(i) != s.charAt(j)){
                flag=false;
                break;
            }
            i++;
            j--;
            
        }
        if(flag) System.out.println("yes");
        else System.out.println("no");
        
    }
}