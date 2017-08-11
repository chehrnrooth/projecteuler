import java.util.ArrayList;

public class Euler2 {
    public static void main(String[] args) {
    	int fibonacci;
    	int num = 0;
    	int num2 = 1;
    	int loop;
    	int sum = 0;
    	//System.out.println(num2);
    		for (fibonacci = 0; fibonacci < 4000000; fibonacci++) { //finding all fibonacci numbers,here for the under 4 million
    			fibonacci = num + num2;
    			num = num2;
    			num2 = fibonacci;
    			//System.out.println("Fibonacci number : " + fibonacci);
    		
    			if (fibonacci%2 == 0) { // locating even fibonacci numbers
    				System.out.println("This is the even fibonacci number  " + fibonacci);
    				sum += fibonacci;
    				System.out.println(sum);
    			}
    		}
    }
}
//answer is 4613732