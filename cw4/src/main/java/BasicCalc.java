import guru.springframework.norris.chuck.ChuckNorrisQuotes;

import java.util.Scanner;
import java.lang.Math;

public class BasicCalc {
    public static void main(String[] args)
    {
        System.out.println("Enter first and second number:");
        Scanner inp= new Scanner(System.in);
        int num1,num2;
        num1 = inp.nextInt();
        num2 = inp.nextInt();
        int ans;
        System.out.println("Enter your selection: 1 for Addition, 2 for subtraction, 3 for Multiplication, 4 for division, 5 power of :");
        int choose;
        choose = inp.nextInt();
        switch (choose) {
            case 1 -> System.out.println(add(num1, num2));
            case 2 -> System.out.println(sub(num1, num2));
            case 3 -> System.out.println(mult(num1, num2));
            case 4 -> System.out.println(div(num1, num2));
            case 5 -> System.out.println(power(num1, num2));
            default -> System.out.println("Illegal Operation");
        }

        ChuckNorrisQuotes jokes = new ChuckNorrisQuotes();
        System.out.println(jokes.getRandomQuote());


    }
    public static int add(int x, int y)
    {
        return x + y;
    }
    public static int sub(int x, int y)
    {
        return x-y;
    }
    public static int mult(int x, int y)
    {
        return x*y;
    }
    public static int div(int x, int y)
    {
        return x/y;
    }
    public static double power(double x, double y)
    {
        return Math.pow(x,y);
    }


}

