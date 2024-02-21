from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.floatlayout import FloatLayout

class SoundPlayer(FloatLayout):
    def play_sound1(self):
     sound = SoundLoader.load("yt1s.com - Fart sound effect.mp3")
     if sound:
        sound.play()
    def play_sound2(self):
     sound = SoundLoader.load("yt1s.com - MEME SOUND 2.mp3")
     if sound:
        sound.play()
    def play_sound3(self):
     sound = SoundLoader.load("yt1s.com - MEMEYeet Sound Effect.mp3")
     sound.volume = 0.5
     if sound:
        sound.play()
    def play_sound4(self):
     sound = SoundLoader.load("yt1s.com - root beer no .mp3")
     sound.volume = 0.5
     if sound:
        sound.play()


class MyApp(App):
    def build(self):
        return SoundPlayer()

MyApp().run()
