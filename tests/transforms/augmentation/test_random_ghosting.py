import pytest

from torchio import RandomGhosting

from ...utils import TorchioTestCase


class TestRandomGhosting(TorchioTestCase):
    """Tests for `RandomGhosting`."""

    def test_with_zero_intensity(self):
        transform = RandomGhosting(intensity=0)
        transformed = transform(self.sample_subject)
        self.assert_tensor_almost_equal(
            self.sample_subject.t1.data,
            transformed.t1.data,
        )

    def test_with_zero_ghost(self):
        transform = RandomGhosting(num_ghosts=0)
        transformed = transform(self.sample_subject)
        self.assert_tensor_almost_equal(
            self.sample_subject.t1.data,
            transformed.t1.data,
        )

    def test_with_ghosting(self):
        transform = RandomGhosting()
        transformed = transform(self.sample_subject)
        self.assert_tensor_not_equal(
            self.sample_subject.t1.data,
            transformed.t1.data,
        )

    def test_intensity_range_with_negative_min(self):
        with pytest.raises(ValueError):
            RandomGhosting(intensity=(-0.5, 4))

    def test_wrong_intensity_type(self):
        with pytest.raises(ValueError):
            RandomGhosting(intensity='wrong')

    def test_negative_num_ghosts(self):
        with pytest.raises(ValueError):
            RandomGhosting(num_ghosts=-1)

    def test_num_ghosts_range_with_negative_min(self):
        with pytest.raises(ValueError):
            RandomGhosting(num_ghosts=(-1, 4))

    def test_not_integer_num_ghosts(self):
        with pytest.raises(ValueError):
            RandomGhosting(num_ghosts=(0.7, 4))

    def test_wrong_num_ghosts_type(self):
        with pytest.raises(ValueError):
            RandomGhosting(num_ghosts='wrong')

    def test_out_of_range_axis(self):
        with pytest.raises(ValueError):
            RandomGhosting(axes=3)

    def test_out_of_range_axis_in_tuple(self):
        with pytest.raises(ValueError):
            RandomGhosting(axes=(0, -1, 2))

    def test_wrong_axes_type(self):
        with pytest.raises(ValueError):
            RandomGhosting(axes=None)

    def test_out_of_range_restore(self):
        with pytest.raises(ValueError):
            RandomGhosting(restore=-1)

    def test_wrong_restore_type(self):
        with pytest.raises(ValueError):
            RandomGhosting(restore='wrong')
