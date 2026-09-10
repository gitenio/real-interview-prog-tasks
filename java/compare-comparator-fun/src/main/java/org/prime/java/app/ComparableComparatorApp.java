package org.prime.java.app;

/*
 * Copyright (C) 2026. Primechannel Corporation Ltd.
 *
 * Project : compare-comparator-fun
 * File name : ComparableComparatorApp.java
 * Last modified : 9/10/26, 6:08 PM
 * Author : Jack Malik
 */

import java.util.*;

import org.prime.java.entity.Player;
import org.prime.java.infra.AlphaComparator;
import org.prime.java.infra.NumericComparator;

public class ComparableComparatorApp {

    public static void main(String[] args) {
        List<Player> footballTeam = new ArrayList<>();
        Player player1 = new Player("59", "John", 55);
        Player player2 = new Player("67", "Roger", 44);
        Player player3 = new Player("45", "Steven", 77);
        Player player4 = new Player("45", "Steven", 14);
        footballTeam.add(player1);
        footballTeam.add(player2);
        footballTeam.add(player3);
        footballTeam.add(player4);
        System.out.println("---------- Sorting players in football team -------- ");

        // Sorting using default toCompare()
        System.out.println("Before Sorting: ");
        footballTeam.stream().forEach(player -> {
            System.out.println("\t" + "Player: " + player);
        });
        Collections.sort(footballTeam);
        System.out.println("After Sorting: ");
        footballTeam.stream().forEach(player -> {
            System.out.println("\t" + "Player: " + player);
        });

        // Sorting using comparator instances
        System.out.println("------ Sorting players by name only --------");
        // Create suitable comparator using name comparison only
        AlphaComparator lc = new AlphaComparator ();
        footballTeam.stream().forEach(player -> {
            System.out.println("\tPlayer: " + player);
        });
        Collections.sort(footballTeam, lc);
        System.out.println("After Sorting:");
        footballTeam.forEach(player -> {
            System.out.println("\tPlayer: " + player);
        });
        System.out.println("------ Sorting players by age --------");
        NumericComparator ac = new NumericComparator();
        Map<Player, Integer> playerIntegerMap = new HashMap<>();

        playerIntegerMap.put(player1, player1.getAge());
        playerIntegerMap.put(player2, player2.getAge());
        playerIntegerMap.put(player3, player3.getAge());
        playerIntegerMap.put(player4, player4.getAge());
        playerIntegerMap.forEach((key, value) -> {
            System.out.println("\tMap KEY: " + key + " - Map VAL: " + value);
        });
        // demonstrating attempt to inplace sort immutable Set collection
        Set<Player> playersSet = playerIntegerMap.keySet();
        System.out.println("\tBefore Sorting : " + playersSet);
        try {
            Collections.sort(List.copyOf(playersSet), ac);
        } catch (UnsupportedOperationException ex) {
            System.out.println("Expected exception: Failed sorting set.stream.toList() collection." +
                    ex.getClass().getName());
        }

        Collections.sort(footballTeam, ac); // could use List.
        System.out.println("\tAfter Sorting : " + footballTeam);
    }
}
