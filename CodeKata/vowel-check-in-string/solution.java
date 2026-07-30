import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        boolean flag = false;
        for(int i=0; i<s.length(); i++)
        {
            char ch = Character.toLowerCase(s.charAt(i));
            switch(ch){
                case 'a':
                    flag = true;
                    break;
                case 'b':
                    flag = true;
                    break;
                case 'i':
                    flag = true;
                    break;
                case 'o':
                    flag = true;
                    break;
                case 'u':
                    flag = true;
                    break;
                default:
                    continue;
            }
        }
        
        if(flag) System.out.println("yes");
        else System.out.println("no");
    }
}