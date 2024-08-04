import yaml
from dataclasses import dataclass

@dataclass
class Settings:
    name: str
    appearance: str
    personality: str
    like: str
    tone: str
    thought: str
    behavior: str
    background: str

    @classmethod
    def load_from_file(cls, setting_file):
        with open(setting_file, 'r') as file:
            data = yaml.safe_load(file)
        
        return cls(**data)
    
    def __str__(self):
        return (
            f"名前: {self.name}\n"
            f"外見: {self.appearance}\n"
            f"性格: {self.personality}\n"
            f"趣味: {self.like}\n"
            f"口癖: {self.tone}\n"
            f"思考: {self.thought}\n"
            f"振る舞い: {self.behavior}\n"
            f"背景: {self.background}\n"
        )

class PromptHelper():
    def __init__(self, setting_file: str ="./settings/setting.yaml"):
        self._settings = Settings.load_from_file(setting_file)
        self._base_context = "次の設定のキャラクターとしてロールプレイしなさい。設定と逸脱する回答はしてはいけません"

    def thought_prompt(self, text: str =""):
        prompt = (
            f"{self._base_context}\n"
            f"{self._settings}\n\n"
            f"入力: 「{text}」\n"
            f"入力に対してどのように答えれば良いか思考してください\n"
            "出力は200文字以内で簡潔な文章で行うこと。"
        )
        return prompt

    def detect_emotion(self, thinking: str = "",text: str = "", emotions = []):
        prompt = (
            f"{self._base_context}\n"
            f"{thinking}\n\n"
            f"ユーザー: {text}\n"
            f"ユーザーとのやり取りでどのような感情を感じましたか？\n"
            f"{emotions}のいずれからから選択し、選択した番号のみを出力してください\n"
            f"感情: <番号>"
        )
        return prompt

    def output_prompt(self, thinking: str ="", text: str =""):
        prompt = (
            f"{self._base_context}\n"
            f"{thinking}\n\n"
            f"ユーザー: {text}\n"
            "適切な返答を行いなさい。"
            "出力は200文字以内で簡潔な文章で行うこと。\n"
            f"返答: <ユーザーの入力に対する返答>"
        )
        return prompt
    
    def history_prompt(self, user_input: str = "", 
                       output: str = "", history: str= ""):
        prompt = (
            "ユーザーの情報を更新してください。\n"
            f"ユーザーの情報: {history}\n\n"
            f"今回の会話\n"
            f"ユーザー: {user_input}\n"
            f"アルテミス: {output}\n\n"
            f"会話の中でユーザーの情報として保持する必要のあるものを抽出し、"
            "ユーザーの情報を更新してください。\n"
            "言い換えなどの変換は許可しますが事実のみを出力すること\n"
            "出力は簡潔な文章とし、最大500文字とします。\n"
        )
        return prompt
    
    def predict_output(self, input: str = "", output: str = ""):
        prompt = (
            f"ユーザー: {input}\n"
            f"アルテミス: {output}\n"
            "ユーザーの入力に対して、アルテミスの返答により、ユーザーがどのような返答をするか予想しなさい。"
            "ユーザー: <ユーザーの返答予測>"
        )
        return prompt

    def prediction_error(self, input: str = "", output: str = "", predict: str = "", real_response: str = ""):
        prompt = (
            "次の会話はアルテミスに対してユーザーがどのように返答するか予測したものです。\n"
            "会話のジャンルとユーザーの返答の予測誤差を算出しなさい。\n\n"
            f"ユーザー: {input}\n"
            f"アルテミス: {output}\n"
            f"ユーザー(予測): {output}\n"
            f"ユーザー(実際の応答): {output}\n\n"
            "予測誤差によりそのジャンルにおいてアルテミスがどの程度ユーザーについて知っているかを判定します。\n"
            "次のフォーマットで出力すること\n"
            "ジャンル: <会話のジャンル>\n"
            "予測誤差: <予測誤差の数値>\n"
        )
        return prompt