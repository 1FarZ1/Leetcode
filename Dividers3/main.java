package Dividers3;

public class main {
    public static void main(String[] args) {
        isThree(5);
    }

    static public boolean isThree(int n) {

        int count = 1;
        for (int i = 1; i <= n / 2; i++) {
            if (n % i == 0) {
                count++;
            }
        }
        if (count == 3) {
            return true;
        } else {
            return false;
        }
    }

}
