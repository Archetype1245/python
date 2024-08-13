import unittest
import television

"""
I opted to access the private variables via their obfuscated names for the unit tests,
rather than using the __str__ method and comparing the resulting strings.

I think with more freedom in the assignment, I would have just included getter/setter methods
and accessed those for unit testing purposes, as that's likely what I'd be doing with other languages anyway.
"""


class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv = television.Television()

    def test___init__(self):
        self.assertFalse(self.tv._Television__status)
        self.assertFalse(self.tv._Television__muted)
        self.assertEqual(self.tv._Television__volume, television.Television.MIN_VOLUME)
        self.assertEqual(self.tv._Television__channel, television.Television.MIN_CHANNEL)

    def test_power(self):
        self.tv.power()
        self.assertTrue(self.tv._Television__status)
        self.tv.power()
        self.assertFalse(self.tv._Television__status)

    def test_mute(self):
        # check if mute method doesn't mute tv is power is off
        self.tv.mute()
        self.assertFalse(self.tv._Television__muted)

        # check if mute method works once the tv is on
        self.tv.power()
        self.tv.mute()
        self.assertTrue(self.tv._Television__muted)
        self.assertEqual(self.tv._Television__volume, television.Television.MIN_VOLUME)

        # check if muting when already muted properly unmutes tv
        self.tv.mute()
        self.assertFalse(self.tv._Television__muted)

        # check if tv gets properly muted when it has a volume value other than the minimum
        self.tv._Television__volume = 2
        self.tv.mute()
        self.assertTrue(self.tv._Television__muted)

        # check if unmuting properly retains the original volume value that was held when muted
        self.tv.mute()
        self.assertEqual(self.tv._Television__volume, 2)

        # check that unmuting does nothing if the tv is off
        self.tv.mute()
        self.assertTrue(self.tv._Television__muted)  # ensures tv is muted
        self.tv.power()
        self.assertFalse(self.tv._Television__status)  # ensures tv is off
        self.tv.mute()
        self.assertEqual(self.tv._Television__volume, television.Television.MIN_VOLUME)

        # checks that turning a muted tv off/on and then unmuting retains expected volume value
        self.tv.power()
        self.tv.mute()
        self.assertEqual(self.tv._Television__volume, 2)

    def test_channel_up(self):
        # checks that channel_up method does nothing when tv is off
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, television.Television.MIN_CHANNEL)

        # checks if channel_up method properly increments the channel value when tv is on
        self.tv.power()
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, television.Television.MIN_CHANNEL + 1)

        # checks if channel_up method wraps channel value back around to the minimum value when used at the max channel
        self.tv._Television__channel = television.Television.MAX_CHANNEL
        self.tv.channel_up()
        self.assertEqual(self.tv._Television__channel, television.Television.MIN_CHANNEL)

    def test_channel_down(self):
        # checks that channel_down method does nothing when tv is off
        self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, television.Television.MIN_CHANNEL)

        # checks that channel_down method properly wraps the channel value around to the max value when used at the min
        self.tv.power()
        self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, television.Television.MAX_CHANNEL)

        # checks that the channel_down method properly decrements the channel value when the tv is on
        self.tv.channel_down()
        self.assertEqual(self.tv._Television__channel, television.Television.MAX_CHANNEL - 1)

    def test_volume_up(self):
        # checks that volume_up method does nothing when tv is off
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, television.Television.MIN_VOLUME)

        # checks that volume_up method properly increments volume when tv is on
        self.tv.power()
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, television.Television.MIN_VOLUME + 1)

        # checks that volume_up method properly unmutes and increments the volume when the tv is on and muted
        self.tv.mute()
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, television.Television.MIN_VOLUME + 2)

        # checks that the volume_up method does not increment the volume value if volume is already at max
        self.tv._Television__volume = television.Television.MAX_VOLUME
        self.tv.volume_up()
        self.assertEqual(self.tv._Television__volume, television.Television.MAX_VOLUME)

    def test_volume_down(self):
        # checks that volume_down method does nothing when tv is off
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, television.Television.MIN_VOLUME)

        # checks that volume_down method does nothing when tv is on and volume is already at minimum value
        self.tv.power()
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, television.Television.MIN_VOLUME)

        # checks that volume_down method properly decrements the volume value when tv is on
        self.tv._Television__volume = television.Television.MAX_VOLUME
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, television.Television.MAX_VOLUME - 1)

        # checks that volume_down method properly unmutes and decrements the volume when the tv is on and muted
        self.tv.mute()
        self.tv.volume_down()
        self.assertEqual(self.tv._Television__volume, television.Television.MAX_VOLUME - 2)


if __name__ == '__main__':
    unittest.main()
