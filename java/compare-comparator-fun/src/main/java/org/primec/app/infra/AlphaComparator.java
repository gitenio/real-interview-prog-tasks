package org.primec.app.infra;

/*
 * Copyright (C) 2026. Primechannel Corporation Ltd.
 *
 * Project : compare-comparator-fun
 * File name : AlphaComparator.java
 * Last modified : 9/11/26, 10:28 AM
 * Author : Jack Malik
 */
import org.primec.app.entity.Player;
import java.util.*;
public class AlphaComparator implements Comparator<Player> {
    @Override
    public int compare(Player a, Player b) {
        return a.getName().compareToIgnoreCase(b.getName());
    }


}
