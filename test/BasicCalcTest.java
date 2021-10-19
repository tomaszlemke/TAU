import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

class BasicCalcTest {

    @BeforeEach
    void setUp() {
    }

    @AfterEach
    void tearDown() {
    }

    @Test
    public void addTest() throws Exception {
        int result = BasicCalc.add( 10, 4);
        assertEquals(14,result);
    }

    @Test
    public void divTest() throws Exception {
        int result = BasicCalc.div( 8, 4);
        assertEquals(2,result);
    }

    @Test
    public void subTest() throws Exception {
        int result = BasicCalc.sub( 50, 3);
        assertEquals(47,result);
    }

    @Test
    public void multiTest() throws Exception {
        int result = BasicCalc.mult( 10, 10);
        assertEquals(100,result);
    }

    @Test
    public void multiTest2() throws Exception {
        int result = BasicCalc.mult( 10, 10);
        assertTrue(result>10);
    }

    @Test
    public void divideByZero(){
        assertThrows(ArithmeticException.class, ()->{
            BasicCalc.div( 8, 0);
        } );
    }

    @Test
    public void floorDiv(){
       float result = BasicCalc.div(10, 3);
       assertNotEquals(3.33, result);
    }

}