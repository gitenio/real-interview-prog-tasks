package org.prime.java.entity;

/*
 * Copyright (C) 2026. Primechannel Corporation Ltd.
 *
 * Project : compare-comparator-fun
 * File name : Player.java
 * Last modified : 9/10/26, 6:25 PM
 * Author : Jack Malik
 */
import java.util.*;
import lombok.NonNull;
import org.jetbrains.annotations.NotNull;

public class Player implements Comparable<Player>, Comparator<Object> {

    private String id;
    private String name;
    private int age;

    public Player(final String id, final String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    public String getName() { return name; }
    public int getAge() { return age; }
    public String getId() { return id; }
    public void setName(String name) {  this.name = name; };


    /**
     * alternative solution to Player compare() method
     * Note signature not compatibile with Comparator which accepts Object type references
     * which passes objects to compare() method
     * @param o1 - Player instance
     * @param o2 - Player instance
     * @return integer value negative int, 0 or positive int
     */
    public int compare(@NotNull Player o1, @NotNull Player o2) {
        return Integer.compare(o1.age, o2.age);
        /**
         *          * brute force approach - own implementation
         *         if (o1.age > o2.age) {
         *             return 1;
         *         }
         *         if (o1.age < o2.age) {
         *             return -1;
         *         }
         *
         */
    }

    @Override
    public int compare(Object o1, Object o2) {
        Player tmp1 = (Player)o1;
        Player tmp2 = (Player)o2;
        return Integer.compare(tmp1.age, tmp2.age);
    }

    public int myCompare(Player that) {
        // return Comparator.comparing(this.age, that.age);
        return Integer.compare(this.age, that.age);
        //return Integer.compare(this.age, that.age);
    }

    // Implements Comparable.compareTo(Player p)
    @Override
    /**
     * Returns integer according to java compare semantics.
     * Note: implemented as part of Comparable<Player> interface
     */

    public int compareTo(@NotNull Player o) {
        return Comparator.comparing(Player::getName)
                .thenComparing(Player::getAge)
                .thenComparing(Player::getId) //, Comparator.nullsLast(Comparator.naturalOrder()))
                .compare(this, o);
    }

    /**
     * returns boolean true if the objects are equal, false otherwise
     * @param object   the reference object with which to compare.
     * @return boolean value true if successful, false otherwise
     */
    public boolean equals(Object object) {
        if (this == object) return true;
        if (object == null || getClass() != object.getClass()) return false;
        if (!super.equals(object))
            return false;
        Player player = (Player) object;
        return age == player.age && java.util.Objects.equals(name, player.name);
    }

    /**
     * Generates hash code based on name and age data members
     * @return
     */
    public int hashCode() {
        return Objects.hash(super.hashCode(), name, id);
    }

    public String toString() {
        return "ID=" + this.id + "|NAME=" + this.name + "|AGE=" + this.age;
    }
}
