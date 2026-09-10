package org.prime.java.infra;

import org.prime.java.entity.Player;
import java.util.*;
/*
 * Copyright (C) 2026. Primechannel Corporation Ltd.
 *
 * Project : compare-comparator-fun
 * File name : AlphaComparator.java
 * Last modified : 9/10/26, 6:42 PM
 * Author : Jack Malik
 */
public class AlphaComparator implements Comparator<Player> {
    @Override
    public int compare(Player a, Player b) {
        return a.getName().compareToIgnoreCase(b.getName());
    }


}
