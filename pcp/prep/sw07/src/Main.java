import java.util.Collection;
import java.util.Collections;
import java.util.stream.IntStream;

public class Main {

    public static void main(String[] args) {

        System.out.println("Hello World!");

        int x = IntStream.range(0, 10)
                .reduce(0, (a, b) -> a + b);

        int y = IntStream.range(0, 10)
                .filter(i -> i % 3 == 0)
                .map(i -> i + 1)
                .reduce(1, (a, b) -> a * b);

        System.out.println(x + ", " + y);

    }

}
