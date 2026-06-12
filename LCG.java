/*
    Método: Linear Congruential Generator
    https://en.wikipedia.org/wiki/Linear_congruential_generator
*/ 

public class LCG {

    public static long randomNum(long xi, long a, long c, long m) {
        long xii;
        xii = (a * xi + c) % m;
        return xii;
    }

    public static void main(String[] args) {
        int n = 500;        
        long a = (long) Math.pow(7, 5); 
        long c = 0;                     
        long m = Integer.MAX_VALUE;     
        
        long x0 = 123456789; 
        long xi = x0;

        double[] values = new double[n]; 
        values[0] = (double) x0 / m; 

        for (int i = 1; i < n; i++) {
            xi = randomNum(xi, a, c, m);
            
            values[i] = (double) xi / m; 
            
            System.out.printf(values[i] + " ");
        }
        System.out.println();
    }
}
