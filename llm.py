from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.generativeai import GenerationConfig
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import time


class Generator():
    def __init__(self):
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path)

        api_key=os.environ["API_KEY"]
        default_model="models/gemini-1.5-pro"
        default_model="models/gemini-1.5-flash"
        # default_model="models/gemini-1.5-pro-latest"
        model_name=os.environ.get('MODEL', default_model)

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.config = GenerationConfig(
            max_output_tokens=128, temperature=0.4, top_p=1, top_k=32,
            candidate_count=1
        )
        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]

    def _gen(self, text):
        ok = False
        try:
            time.sleep(2)
            response = self.model.generate_content(text, generation_config=self.config, safety_settings=self.safety_settings)
            ok = True
        except Exception as e:
            print('wait...')
            time.sleep(5)
            response = None
            ok = False
        return ok, response

    def gen_text(self, text):
        print('[debug] prompt: ', text)
        while(True):
            ok, response = self._gen(text)
            if ok:
                break
        print('[debug] response: ', response.text)
        return response.text