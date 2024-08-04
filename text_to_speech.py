import torch
from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none
import soundfile as sf
import sounddevice as sd

class Text2SpeechEPS():
    def __init__(self, model_name='kan-bayashi/tsukuyomi_full_band_vits_prosody'):
        # lang = 'Japanese'
        vocoder_tags = [None, 
         "parallel_wavegan/jsut_parallel_wavegan.v1", 
         "parallel_wavegan/jsut_multi_band_melgan.v2", 
         "parallel_wavegan/jsut_style_melgan.v1", 
         "parallel_wavegan/jsut_hifigan.v1"]
        vocoder_tag = vocoder_tags[0]

        self.text2speech = Text2Speech.from_pretrained(
            model_tag=model_name,
            vocoder_tag=vocoder_tag,
            device="cuda",
            # Only for Tacotron 2 & Transformer
            threshold=0.5,
            # Only for Tacotron 2
            minlenratio=0.0,
            maxlenratio=10.0,
            use_att_constraint=False,
            backward_window=1,
            forward_window=3,
            # Only for FastSpeech & FastSpeech2 & VITS
            speed_control_alpha=1.0,
            # Only for VITS
            noise_scale=0.333,
            noise_scale_dur=0.333,
        )
        self.sample_rate=self.text2speech.fs

    def do(self, text, save_file="./sample.wav"):
        with torch.no_grad():
            wav = self.text2speech(text)["wav"]

        audio_array = wav.view(-1).cpu().numpy()
        sf.write(save_file, audio_array, self.sample_rate)
        return audio_array
    
    def play(self, text):
        with torch.no_grad():
            wav = self.text2speech(text)["wav"]

        audio_array = wav.view(-1).cpu().numpy()
        sd.play(audio_array, self.sample_rate)
        sd.wait()
        return "done"

def main():
    t2s = Text2SpeechEPS()
    t2s.do("今日も良い天気だね", save_file="./tmp_audio/output.wav")

if __name__ == '__main__':
    main()