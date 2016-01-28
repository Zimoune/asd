# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2015, december
"""

import sys
import experience
import sorting

global cpt


def compare(m1, m2):
    return experience.compare(m1, m2)


def compare_cpt(m1, m2):
    global cpt
    cpt += 1
    return compare(m1, m2)


# STRATEGY 1
def negative_markers1(markers, positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    :param markers: The list of markers
    :type markers: List of String
    :param positive: The list of positive markers
    :type markers: List of String
    :return: The list of negative markers
    :rtype: List of String
    """
    negative = []

    for m in markers:
        i = 0
        while i < len(positive) and compare_cpt(m, positive[i]) != 0:
            i += 1
        if i < len(positive):
            negative += [m]
        i = 0
    return negative


# STRATEGY 2
def negative_markers2(markers, positive):
    positive_l = sorting.merge_sort(positive , compare_cpt)
    negative = []
    for m in markers:
        a = 0
        b = len(positive)
        find = False
        while (not find) and a < b:
            mid = (a+b)//2
            comp = compare_cpt(m, positive[mid])
            if comp == 0:
                find = True
            elif comp == 1:
                a = mid +1
            else:
               b = mid -1
        if find == False:
            negative += [m]
    return negative


# STRATEGY 3
def negative_markers3(markers, positive):
    negative = []
    return negative
        
if __name__ == "__main__":
    p = int(sys.argv[1])
    m = int(sys.argv[2])

    markers = experience.markers(m)
    positive = experience.experience(p, markers)

    print("Markers: %s" % (markers))
    print("Positive markers: %s" % (positive))

    
    # test stategy 1
    cpt = 0
    print("Negative markers: %s" % (negative_markers1(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))
    cpt_strat1 = cpt

    # test stategy 2
    cpt = 0
    print("Negative markers: %s" % (negative_markers2(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))
    cpt_strat2 = cpt
    # test stategy 3
    cpt = 0
    print("Negative markers: %s" % (negative_markers3(markers,positive)))
    print("Nb. comparisons: %d" % (cpt))
    cpt_strat3 = cpt

    data = open("gnup_tab.txt","wr")

    for i in range(1, 11):
        data.write(str(m)+' '+str(p)+' '+ str(
