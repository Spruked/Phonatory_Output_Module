# tests/test_phonitory_output.py

from phonitory_output_module import PhonatoryOutputModule
import os

def test_phonate():
    text = "This is the voice of the Promethean system. I am now online."
    output = "promethean_voice.wav"
    emitter = PhonatoryOutputModule()
    path = emitter.phonate(text, out_path=output)
    assert os.path.exists(path), "Output voice file was not created."