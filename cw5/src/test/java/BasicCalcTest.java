import guru.springframework.norris.chuck.ChuckNorrisQuotes;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import static org.mockito.BDDMockito.*;
import org.kohsuke.randname.RandomNameGenerator;

import static org.junit.jupiter.api.Assertions.*;

public class BasicCalcTest {

    @BeforeEach
    public void setUp() {
    }

    @AfterEach
    public void tearDown() {
    }

    @Test
    public void addTest() {
        System.out.println("1. Testing: Adding");
        int result = BasicCalc.add( 10, 4);
        assertEquals(14,result);
    }

    @Test
    public void divTest() {
        System.out.println("2. Testing: Dividing");
        int result = BasicCalc.div( 8, 4);
        assertEquals(2,result);
    }

    @Test
    public void subTest() {
        System.out.println("3. Testing: Subtracting");
        int result = BasicCalc.sub( 50, 3);
        assertEquals(47,result);
    }

    @Test
    public void multiTest() {
        System.out.println("4. Testing: Multiplying");
        int result = BasicCalc.mult( 10, 10);
        assertEquals(100,result);
    }

    @Test
    public void multiTest2()  {
        System.out.println("5. Testing: Multiplying - True or False");
        int result = BasicCalc.mult( 10, 10);
        assertTrue(result>10);
    }

    @Test
    public void divideByZero(){
        System.out.println("6. Testing: Dividing by zero");
        assertThrows(ArithmeticException.class, ()->{
            BasicCalc.div( 8, 0);
        } );
    }

    @Test
    public void floorDiv(){
        System.out.println("7. Testing: Floor Dividing");
        float result = BasicCalc.div(10, 3);
        assertNotEquals(3.33, result);
    }

    @Test
    public void multi3(){
        System.out.println("8. Testing: Swap multiplication");
        int result = BasicCalc.mult( 8, 9);
        int result2 = BasicCalc.mult( 9, 8);
        assertEquals(result, result2);
    }

    @Test
    public void subTest2() {
        System.out.println("9. Testing: Subtracting negative number");
        int result = BasicCalc.sub( 10, -3);
        assertEquals(13,result);
    }

    @Test
    public void comboTest() {
        System.out.println("10. Testing: Subtracting and addition combo");
        int result = BasicCalc.sub( 10, -3) + BasicCalc.add(7, 20);
        assertEquals(40,result);
    }

    @Test
    public void comboTest2() {
        System.out.println("11. Testing: Division and multiplication combo");
        int result = BasicCalc.div( 10, -2) * BasicCalc.mult(5, 5);
        assertEquals(-125,result);
    }

    @Test
    public void comboTest3() {
        System.out.println("12. Testing: full combo");
        int result = BasicCalc.div( 10, -2) * BasicCalc.mult(5, 5)
                - BasicCalc.sub( 10, -3) + BasicCalc.add(8, 10) / 2;
        assertEquals(-129,result);
    }

    @Test
    public void powerTest() {
        System.out.println("13. Testing: Power X of Y");
        double result = BasicCalc.power(2,4);
        assertEquals(16, result);
    }

    @Test
    public void comboTest5() {
        System.out.println("14. Testing: Zero Power of X");
        double result = BasicCalc.power(80,0);
        assertEquals(1, result);
    }

    @Test
    public void randomName(){
        System.out.println("15. Testing: Random name");
        RandomNameGenerator rnd = new RandomNameGenerator(0);
        String name = rnd.next();
        assertNotSame(name, "rainbow_unicorn");
    }

    @Test
    public void ChuckTestEmpty() {
        System.out.println("16. Testing: was joke generated ?");
        ChuckNorrisQuotes jokes = new ChuckNorrisQuotes();
        assertNotNull(jokes);
    }

    @Test
    public void ChuckTestRepeat() {
        System.out.println("17. Testing: were unique jokes generated ?");
        ChuckNorrisQuotes jokes = new ChuckNorrisQuotes();
        ChuckNorrisQuotes jokes2 = new ChuckNorrisQuotes();
        assertNotEquals(jokes.getRandomQuote(), jokes2.getRandomQuote());
    }

    private int a, x;

    @Test
    public void example() {
        System.out.println("I - checking mockito on basic functions");
        BasicCalc basicCalc = new BasicCalc();
        a = basicCalc.add(2,2);
        assertEquals(4, a);
    }


    @Test
    public void example2() {
        System.out.println("II - AsserEqual with when/then");
        BasicCalc basicCalc = mock(BasicCalc.class);
        when(basicCalc.findDelta(4,90,1)).thenReturn(9);
        a = basicCalc.findDelta(4,90,1);
        assertEquals(9, a);
    }

    @Test
    public void example3() {
        System.out.println("III - AsserEqual with given/will");
        BasicCalc basicCalc = mock(BasicCalc.class);
        given(basicCalc.findDelta(3,4,5)).willReturn(99);
        x = basicCalc.findDelta(3,4,5);
        assertEquals(99, x);
    }

    @Test
    public void example4() {
        System.out.println("IV - AssertNotEqual with given/will");
        BasicCalc basicCalc = mock(BasicCalc.class);
        given(basicCalc.findDelta(3,4,5)).willReturn(99);
        x = basicCalc.findDelta(2,4,5);
        assertNotEquals(99, x);
    }

    @Test
    public void example5() {
        System.out.println("V - AsssertTrue with given/will");
        BasicCalc basicCalc = mock(BasicCalc.class);
        given(basicCalc.findDelta(3,4,5)).willReturn(99);
        x = basicCalc.findDelta(3,4,5);
        assertTrue(99 == x);
    }

    @Test
    public void example6() {
        System.out.println("VI - AssserEquals with given/will on SquareRoot");
        BasicCalc basicCalc = mock(BasicCalc.class);
        given(basicCalc.squareRoot(9)).willReturn(3.00);
        double result = basicCalc.squareRoot(9);
        assertEquals(3.00, result);
    }

    @Test
    public void example7() {
        System.out.println("VII - AssserFalse with given/will on SquareRoot");
        BasicCalc basicCalc = mock(BasicCalc.class);
        given(basicCalc.squareRoot(9)).willReturn(3.00);
        double result = basicCalc.squareRoot(9);
        assertFalse(result != 3.00);
    }

    @Test
    public void example8() {
        System.out.println("VIII - AssserTrue with given/will on CubeRoot");
        BasicCalc basicCalc = mock(BasicCalc.class);
        given(basicCalc.cubeRoot(81)).willReturn(3.00);
        double result = basicCalc.cubeRoot(81);
        assertTrue(result >= 3.00);
    }
}
