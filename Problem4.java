//Find the largest palindrome made from the product of two 3-digit numbers
/*First have to find all the multiples of xxx * yyy,
 then find the palindromes, then find the largest ones */
/*import java.util.*;
class Problem4  {
	public static void main(String[] args) {
		for (int i = 900; i < 1000; i++){
			for (int j = 100; j < 1000; j++){
				int product = i * j;
				if (product > 900000) {
					int palindrome = product;
					int reverse = 0;
					reverse = (reverse*10) + palindrome%10;
				}
			}
		}		
	}
}*/
public class Problem4 {

public static void main(String[] args) {

    int x = 999; // largest 3-digit number
    int largestProduct = 0;

    for(int y=x; y>99; y--){
        int product = x*y;

        if(isPalindormic(x*y)){
            if(product>largestProduct){
                largestProduct = product;
                System.out.println("3-digit numbers product palindormic number : " + x + " * " + y + " : " + product);
            }
        }

        if(y==100 || product < largestProduct){y=x;x--;}
    }


}

public static boolean isPalindormic(int n){ //public, static, return type boolean, method name isPalindromic, value passed to method int n

    int palindormic = n;
    int reverse = 0;

    while(n>9){
        reverse = (reverse*10) + n%10;
        n=n/10;
    }
    reverse = (reverse*10) + n;     
    return (reverse == palindormic);
}
}
