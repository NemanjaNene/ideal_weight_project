# Rezultati testiranja

## Jedinični testovi

| Test naziv                   | Očekivani rezultat | Status      |
|------------------------------|--------------------|-------------|
| test_male_normal_height      | 67.8              | Prošao      |
| test_female_normal_height    | 61.7              | Prošao      |
| test_boundary_height         | 48, 45.5          | Prošao      |
| test_invalid_gender          | ValueError        | Prošao      |
| test_negative_height         | ValueError        | Prošao      |
| test_non_numeric_height      | ValueError        | Prošao      |

## Zaključak

Svi testovi su uspešno prošli, što potvrđuje ispravnost implementacije funkcije `calculate_ideal_weight`.
