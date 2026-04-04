from diary import Diary
class DiaryPersistence:
    @staticmethod
    def save_to_file(diary, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for sissekanne in diary.sissekanded:
                f.write(sissekanne + "\n")

    @staticmethod
    def load_from_file(filename):
        diary = Diary()
        with open(filename, "r", encoding="utf-8") as f:
            for rida in f:
                puhas_rida = rida.strip()
                if puhas_rida:
                    diary.sissekanded.append(puhas_rida)
        diary.loendur = len(diary.sissekanded)
        return diary