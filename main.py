import re

from gui import create_gui
from llm import Generator
from prompt_helper import PromptHelper
from emotions import Emotions
from history import History

def main():
    generator = Generator()
    prompt_helper = PromptHelper()
    emotions = Emotions()
    history = History(history_file="./history/log.txt")

    def on_submit(input_text):
        return input_text, emotions.default
        # current_history = history.get()
        # p = prompt_helper.thought_prompt(input_text)
        # thinking = generator.gen_text(p)

        # emotion_prompt = prompt_helper.detect_emotion(thinking=thinking, text=input_text, emotions=emotions)
        # emotion_result = generator.gen_text(emotion_prompt)
        # match = re.search(r'.*?(\d+).*', emotion_result)
        # index = match.group(1) if match else None
        # current_emotion = emotions.get_by_idx(index)

        # response_prompt = prompt_helper.output_prompt(thinking=thinking, text=input_text)
        # result = generator.gen_text(response_prompt)
        
        # history_prompt = prompt_helper.history_prompt(user_input=input_text, output=result, history=current_history)
        # new_history = generator.gen_text(history_prompt)
        # history.update_with_load(new_history)

        # return result, current_emotion

    create_gui(on_submit)
    

if __name__ == '__main__':
    main()