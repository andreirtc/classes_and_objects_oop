# 2. When the class or the blueprint of the TV is done, create another file named test_tv.py to test and produce the channel and volume level of tv 1 and tv 2

from TV import TV

def test_TV():
    tv1 = TV()
    tv2 = TV()

    tv1.turn_on
    tv1.set_channel(30)
    tv1.set_volume(3)

    tv2.turn_on
    tv2.set_channel(3)
    tv2.set_volume(2)