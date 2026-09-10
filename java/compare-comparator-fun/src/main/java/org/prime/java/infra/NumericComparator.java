package org.prime.java.infra;

/*
 * Copyright (C) 2026. Primechannel Corporation Ltd.
 *
 * Project : compare-comparator-fun
 * File name : NumericComparator.java
 * Last modified : 9/10/26, 6:44 PM
 * Author : Jack Malik
 */

import org.prime.java.entity.Player;

import java.util.*;

public class NumericComparator implements Comparator<Player> {
    @Override
    public int compare(Player a, Player b) {
        //  return a.getAge() < b.getAge() ? -1 : a.getAge() == b.getAge() ? 0 : 1;
        return Integer.compare(a.getAge(), b.getAge());
    }
}
