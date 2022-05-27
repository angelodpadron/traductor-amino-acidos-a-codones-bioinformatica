# Script to translate an amino acid sequence into one of its possible codons sequence (ARN nucleotides)

import random
from dictionary import Codons


def translate_sequence(sequence):
    output_sequence = ""
    for residue in sequence:
        output_sequence += "-" + get_codon_for(residue)
    output_sequence = set_bounds_for(output_sequence)
    return output_sequence


def get_codon_for(residue):
    if residue in Codons:
        return random.choice(Codons[residue])
    return "???"


def set_bounds_for(sequence):
    if not sequence[:3] in Codons["START"]:
        sequence = random.choice(Codons["START"]) + sequence
    if not sequence[-3:] in Codons["STOP"]:
        sequence = sequence + "-" + random.choice(Codons["STOP"])

    return sequence


if __name__ == '__main__':
    result = translate_sequence(input("Enter proteic sequence: "))
    print("Codon sequence: ", result)
