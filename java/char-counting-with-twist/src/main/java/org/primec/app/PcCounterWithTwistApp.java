package org.primec.app;

/*
 * Copyright (C) 2026. Primechannel Corporation Ltd.
 *
 * Project : char-counting-with-twist
 * File name : PcCounterWithTwistApp.java
 * Last modified : 9/11/26, 3:47 PM
 * Author : Jack Malik
 */
import java.security.SecureRandom;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Stream;
import static java.lang.System.exit;

/**
 * CS - Test
 * Spec:
 *
 * Given a sorted array of N elements with duplicates, for example:
 *  a,b,b,b,b,b,d,h,h,h,p
 * count the number of occurrences of each unique element.
 *   1a) Solve this with an O(N) algorithm
 *   1b) Solve this with a better-than-O(N) algorithm and analyze
 *   its time complexity.
 * While it may be useful to run your code with the example array above,
 * please also test it with a larger (ex., 100-1000 elements) randomly generated, sorted array.
 *
 *
 */

public class PcCounterWithTwistApp {

    public static int RANDOM_SEED_LEN = 20;
    public static char CS_INPUT[] = "abbbbbdhhhp".toCharArray();

    public static Stream<Character> GetRandomCharArray(int length){
        /***
         * Takes integer value and returns a Java Stream object containing
         * the 'length' number of characters. The characters in the stream
         * are in the ordered sequence but as explained elsewhere the algorithm
         * counting character occurences in an array of characters is inherently
         * of O(n) complexity regardless of whether or not the input array is
         * sorted or not sorted.
         ***/

        Stream<Character> randomCharStream =
                new SecureRandom(new SecureRandom()
                        .generateSeed(RANDOM_SEED_LEN))
                        .ints(Character.MIN_CODE_POINT, Character.MAX_CODE_POINT)
                        .mapToObj(i -> (char)i)
                        .filter(c -> c >= '0' && c <= 'z' && Character.isLetterOrDigit(c))
                        .limit(length);
        return randomCharStream.sorted();
    }

    public static Map<Character, Integer> Count(Stream<Character> inputCharArrayStream) {
        /***
         * Generate random array of characters in the Stream and count how
         * many times each of the characters in the array appear in that array.
         * Store count data in HashMap with key to be the character and an Integer
         * value storing the count.
         ***/

        HashMap<Character, Integer> countMap = new HashMap<>();
        if (inputCharArrayStream == null) {
            return countMap;
        }

        // Traverse char[] implicitly by retrieving from Stream and get character count
        inputCharArrayStream.forEach(
                i -> {
                    final Integer count = countMap.containsKey(i)? countMap.put(i, countMap.get(i)+1): countMap.put(i, 1);
                }
        );
        return countMap;
    }

    public static void Display(Map<Character, Integer> char2CountMap) {
        char2CountMap.forEach((aChar, count) -> {
            System.out.println("Char '" + aChar + "' found " + count + " times in random string.");
        });
    }

    public static void main(String[] args) {
        /***
         * Main driver for the coding exercise. Please view Readme.md for test description
         * and algorithm analysis.
         */
        System.out.print("Enter random string length: ");
        try {
            // Get user input and create random char array and wrap in Stream
            int length = Integer.parseInt(new Scanner(System.in).next());
            System.out.printf("\t... generating random array of characters of length: %d ..", length);
            Stream<Character> inputCharArrayStream = GetRandomCharArray(length);

            // Perform count
            Map<Character, Integer> char2CountMap = PcCounterWithTwistApp.Count(inputCharArrayStream);

            // Display results
            PcCounterWithTwistApp.Display(char2CountMap);
        } catch (NumberFormatException ex) {
            System.out.printf("Invalid number: '%s' .. Enter a valid number ..", ex.toString());
            exit(1);
        } catch (Exception ex) {
            System.out.printf("Unexpected exception '%s' .. Aborting ..", ex.toString());
            exit(1);
        }
        exit(0);
    }

}
