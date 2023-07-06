import dbus

from dbus import SessionBus, Dictionary
from dbus.service import Object, BusName
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository.GLib import MainLoop

from mpris2.constants import PlayerInterface, AppInterface
from mpris2.enums import PlaybackStatus, ShuffleMode


class Mpris2Service(Object):
    def __init__(self):
        self.loop = MainLoop()

        session_bus = SessionBus(mainloop=DBusGMainLoop())
        bus = BusName('org.mpris2.MediaPlayer2.gmd', session_bus)

        super().__init__(bus, '/org/mpris2/MediaPlayer2')

        self.state = {
            'playback_status': PlaybackStatus.Stopped
        }

    def enable(self):
        try:
            self.loop.run()
        finally:
            self.loop.quit()

    @dbus.service.method(PlayerInterface, in_signature='', out_signature='')
    def PlayPause(self):
        if self.state['playback_status'] == PlaybackStatus.Playing:
            self.state['playback_status'] = PlaybackStatus.Paused
            self.PropertiesChanged(PlayerInterface, {'PlaybackStatus': 'Paused'}, [])
        else:
            self.state['playback_status'] = PlaybackStatus.Playing
            self.Set(PlayerInterface, 'PlaybackStatus', 'Playing')

    @dbus.service.method(PlayerInterface, in_signature='', out_signature='')
    def Next(self):
        print("dbus Next method")

    @dbus.service.method(PlayerInterface, in_signature='', out_signature='')
    def Previous(self):
        print("dbus Previous method")

    @dbus.service.method(PlayerInterface, in_signature='s', out_signature='')
    def OpenUri(self, uri):
        pass

    @dbus.service.method(PlayerInterface, in_signature='ox', out_signature='')
    def SetPosition(self, track_id, position):
        pass

    @dbus.service.signal(dbus.PROPERTIES_IFACE, signature='sa{sv}as')
    def PropertiesChanged(self, interface, changed_properties, invalidated_properties=None):
        pass

    @dbus.service.method(dbus.PROPERTIES_IFACE, in_signature='ss', out_signature='v')
    def Get(self, interface, prop):
        return self.GetAll(interface)[prop]

    @dbus.service.method(dbus.PROPERTIES_IFACE, in_signature='ssv')
    def Set(self, interface, prop, value):
        self.PropertiesChanged(interface, {prop: value}, [])

    @dbus.service.method(dbus.PROPERTIES_IFACE, in_signature='s', out_signature='a{sv}')
    def GetAll(self, interface):
        if interface == PlayerInterface:
            return Dictionary(
                {
                    'Metadata': Dictionary(
                        {
                            'xesam:artist': ['Celldweller'],
                            'xesam:album': 'SwitchBack',
                            'xesam:title': 'SwitchBack'
                        },
                        signature='sv'
                    ),
                    'Rate': 1.0,
                    'MinimumRate': 1.0,
                    'MaximumRate': 1.0,
                    'CanGoNext': True,
                    'CanGoPrevious': True,
                    'CanControl': True,
                    'CanSeek': True,
                    'CanPause': True,
                    'CanPlay': True,
                    'Position': 0,
                    'Shuffle':  ShuffleMode.Off.value,
                    'PlaybackStatus': self.state['playback_status'].value,
                    'Volume': 0,
                },
                signature='sv', variant_level=2
            )
        if interface == AppInterface:
            return Dictionary(
                {
                    'Identity': 'org.mpris2.MediaPlayer2.gmd',
                    'CanQuit': True,
                    'CanRaise': True,
                    'HasTrackList': False,
                    'SupportedUriSchemes': ['http', 'file', 'fuo'],
                    'SupportedMimeTypes': [
                        'audio/aac',
                        'audio/m4a',
                        'audio/mp3',
                        'audio/wav',
                        'audio/wma',
                        'audio/x-ape',
                        'audio/x-flac',
                        'audio/x-ogg',
                        'audio/x-oggflac',
                        'audio/x-vorbis'
                    ]
                },
                signature='sv'
            )
        raise dbus.exceptions.DBusException(
            'com.example.UnknownInterface',
            f'The Foo object does not implement the {interface} interface'
        )

    @dbus.service.method(AppInterface, in_signature='', out_signature='')
    def Quit(self):
        exit()

    @dbus.service.method(AppInterface, in_signature='', out_signature='')
    def Raise(self):
        pass
