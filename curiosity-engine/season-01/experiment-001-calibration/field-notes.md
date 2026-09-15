# Experiment 001 — Calibration 🧪

**Status:** Complete  
**Artifact:** Specimen Intake Terminal v1  
**Skill Tree:** Programming ●

## What I made

A small Python specimen intake terminal that accepts a specimen name, location, and danger level; calculates the remaining danger capacity out of 10; and generates an archive label from the entered values.

## Skills used

- Variables
- Strings and integers
- `input()`
- `int()` conversion
- Arithmetic
- `print()`
- f-string formatting

## Experimental evidence

The first version stored the specimen name and location directly in the code. It was then changed so the operator could enter them, turning the script into a reusable intake terminal rather than a program for one predetermined specimen.

### Unexpected specimen: `{3}`

An early version used `{remaining_danger}` outside the f-string. Python interpreted the braces as a set, so the terminal printed `{3}` instead of `3`.

The output was corrected by printing the variable directly.

## Final behaviour

The terminal now:

1. asks for a specimen name;
2. asks where it was found;
3. asks for a danger level;
4. calculates remaining danger capacity;
5. prints the specimen record;
6. constructs an archive label dynamically from the stored values.

## Calibration result

Demonstrated working familiarity with variables, input, type conversion, arithmetic, output, and basic formatted strings. When something behaved unexpectedly, the problem could be corrected from a small hint rather than a supplied solution.

**Artifact acquired:** Specimen Intake Terminal v1
