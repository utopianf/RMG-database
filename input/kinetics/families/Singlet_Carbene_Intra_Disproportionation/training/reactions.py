#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_Carbene_Intra_Disproportionation/training"
shortDesc = "Reaction kinetics used to generate rate rules"
longDesc = """
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""
entry(
    index = 0,
    label = "C6H6 <=> C6H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.067e+10,'s^-1'), n=0.649, Ea=(8.03,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
"""
Taken from entry: A <=> IV
""",
)

entry(
    index = 1,
    label = "C6H6-3 <=> C6H6-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.454e+12,'s^-1'), n=0.178, Ea=(0.205,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
"""
Taken from entry: IX <=> VII
""",
)

entry(
    index = 2,
    label = "C6H6-5 <=> C6H6-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.865e+11,'s^-1'), n=0.577, Ea=(29.169,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
"""
Taken from entry: X <=> IX
""",
)

entry(
    index = 3,
    label = "C6H6-7 <=> C6H6-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.355e+12,'s^-1'), n=0.294, Ea=(35.954,'kcal/mol'), T0=(1,'K')),
    rank = 5,
    shortDesc = """Training reaction from kinetics library: 2003_Miller_Propargyl_Recomb_High_P""",
    longDesc = 
"""
Taken from entry: X <=> XI
""",
)

