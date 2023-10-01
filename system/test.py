from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton
from kivy.clock import Clock
import cv2
import numpy as np

KV = '''
BoxLayout:
    orientation: 'vertical'

    Camera:
        id: camera_widget
        resolution: (640, 480)  # Set your desired camera resolution here
        play: True  # Start camera off by default

    MDRaisedButton:
        text: 'Start Camera'
        on_release: app.start_camera()

    MDRaisedButton:
        text: 'Stop Camera'
        on_release: app.stop_camera()

    Image:
        id: image_widget
        allow_stretch: True  # Stretch the image to fill the widget
'''

class CameraApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def start_camera(self):
        self.root.ids.camera_widget.play = True
        self.update_camera()  # Start updating the camera frames

    def stop_camera(self):
        self.root.ids.camera_widget.play = False

    def update_camera(self, dt=1 / 30):
        if self.root.ids.camera_widget.play:
            # Capture a frame from the camera
            frame = self.root.ids.camera_widget.export_as_image()

            # Convert the frame to a format suitable for Kivy's Image widget
            frame_bytes = frame.texture.pixels
            frame_np = np.frombuffer(frame_bytes, dtype=np.uint8)
            frame_bgr = frame_np.reshape(frame.height, frame.width, 4)[:, :, :3]

            # Convert the BGR frame to RGB for display
            frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

            # Update the Image widget with the camera frame
            self.root.ids.image_widget.texture = frame_rgb.tostring()

if __name__ == '__main__':
    CameraApp().run()
