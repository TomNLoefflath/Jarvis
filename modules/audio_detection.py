"""
Jarvis Voice and Sound Recognition Module
Detects claps and other sounds to trigger commands
"""

import numpy as np
import threading
from pathlib import Path

try:
    import sounddevice as sd
    import soundfile as sf
except ImportError:
    print("Note: Audio features require additional packages")

class AudioListener:
    def __init__(self):
        self.clap_count = 0
        self.clap_cooldown = 0
        self.is_listening = False
        self.callbacks = {}
        
    def start_listening(self):
        """Start listening for claps"""
        self.is_listening = True
        threading.Thread(target=self._listen_loop, daemon=True).start()
        
    def _listen_loop(self):
        """Listen for audio input"""
        try:
            # Try to detect loud sounds (claps)
            duration = 1  # Listen for 1 second at a time
            samplerate = 44100
            
            while self.is_listening:
                try:
                    audio = sd.rec(int(samplerate * duration), samplerate=samplerate, channels=1)
                    sd.wait()
                    
                    # Check if audio volume is high (clap)
                    volume = np.abs(audio).mean()
                    if volume > 0.1:  # Threshold for clap detection
                        self.clap_count += 1
                        
                        # If 2 claps detected, trigger callback
                        if self.clap_count >= 2:
                            if "double_clap" in self.callbacks:
                                self.callbacks["double_clap"]()
                            self.clap_count = 0
                except Exception as e:
                    pass
                    
        except Exception as e:
            print(f"Audio listening error: {e}")
    
    def stop_listening(self):
        """Stop listening"""
        self.is_listening = False
    
    def on_double_clap(self, callback):
        """Register callback for double clap"""
        self.callbacks["double_clap"] = callback
