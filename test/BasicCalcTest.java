import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class BasicCalcTest {

    @org.junit.jupiter.api.BeforeEach
    void setUp() {
    }

    @org.junit.jupiter.api.AfterEach
    void tearDown() {
    }

    @org.junit.jupiter.api.Test
    public void addTest() throws Exception {
        int result = BasicCalc.add( 10, 4);
        assertEquals(14,result);
    }

    @org.junit.jupiter.api.Test
    public void divTest() throws Exception {
        int result = BasicCalc.div( 8, 4);
        assertEquals(2,result);
    }

    @org.junit.jupiter.api.Test
    public void subTest() throws Exception {
        int result = BasicCalc.sub( 50, 3);
        assertEquals(47,result);
    }

    @org.junit.jupiter.api.Test
    public void multiTest() throws Exception {
        int result = BasicCalc.mult( 10, 10);
        assertEquals(100,result);
    }

    @org.junit.jupiter.api.Test
    public void multiTest2() throws Exception {
        int result = BasicCalc.mult( 10, 10);
        assertTrue(result>10);
    }

    @org.junit.jupiter.api.Test
    public void divideByZero(){
        assertThrows(ArithmeticException.class, ()->{
            int result = BasicCalc.div( 8, 0);
        } );
    }

    @org.junit.jupiter.api.Test
    public void floorDiv(){
       float result = BasicCalc.div(10, 3);
       assertNotEquals(3.33, result);
    }




}