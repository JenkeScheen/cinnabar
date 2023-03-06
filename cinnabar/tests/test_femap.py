from importlib import resources
import pytest

from openff.units import unit

import cinnabar
from cinnabar import femap


@pytest.fixture
def example_csv():
    with resources.path('cinnabar.data', 'example.csv') as f:
        yield f


def test_read_csv(example_csv):
    data = femap.read_csv(example_csv)

    assert 'Experimental' in data
    assert len(data['Experimental']) == 36

    assert 'Calculated' in data
    assert len(data['Calculated']) == 58


def test_femap():
    m = cinnabar.FEMap()

    m1 = cinnabar.RelativeMeasurement(labelA='ligA', labelB='ligB', DDG=1.1 * unit.kilojoule_per_mole,
                                      uncertainty=0.1 * unit.kilojoule_per_mole, computational=True)
    m2 = cinnabar.AbsoluteMeasurement(label='ligA', DG=10.0 * unit.kilojoule_per_mole,
                                      uncertainty=0.2 * unit.kilojoule_per_mole, computational=False)
    m3 = cinnabar.AbsoluteMeasurement(label='ligB', DG=11.0 * unit.kilojoule_per_mole,
                                      uncertainty=0.3 * unit.kilojoule_per_mole, computational=False)

    m.add_measurement(m1)
    m.add_measurement(m2)
    m.add_measurement(m3)

    assert m.n_ligands == 2