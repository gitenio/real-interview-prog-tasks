package org.primec.app.infra;

/*
 * Copyright (C) 2026. Primechannel Corporation Ltd.
 *
 * Project : compare-comparator-fun
 * File name : NumericComparator.java
 * Last modified : 9/11/26, 10:28 AM
 * Author : Jack Malik
 */

import org.primec.app.entity.Player;

import java.util.*;

public class NumericComparator implements Comparator<Player> {
    @Override
    public int compare(Player a, Player b) {
        //  return a.getAge() < b.getAge() ? -1 : a.getAge() == b.getAge() ? 0 : 1;
        return Integer.compare(a.getAge(), b.getAge());
    }
}
