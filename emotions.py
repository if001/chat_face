from dataclasses import dataclass
@dataclass
class Emotion:
    value: str
    img_path: str


@dataclass
class Emotions:
    default: Emotion = Emotion("ニュートラル", "./images/default.jpg")
    anger: Emotion = Emotion("怒り", "./images/anger.jpg")
    crying: Emotion = Emotion("悲しみ", "./images/crying.jpg")
    smile: Emotion = Emotion("笑い", "./images/smile.jpg")

    def __str__(self):
        return f"1.{self.default.value}、2.{self.anger.value}、3.{self.crying.value}、4.{self.smile.value}"

    def get_by_idx(self, idx):
        if idx == 1:
            return self.default
        if idx == 2:
            return self.anger
        if idx == 3:
            return self.crying
        if idx == 4:
            return self.smile
        return self.default
