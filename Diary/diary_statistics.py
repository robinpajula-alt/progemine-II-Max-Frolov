class DiaryStatistics:
    @staticmethod
    def get_statistics(diary):
        arv = len(diary.sissekanded)
        pikkus = 0
        for sissekanne in diary.sissekanded:
            pikkus = pikkus + len(sissekanne)
        kesk_arv = pikkus / arv
        return arv, kesk_arv

    @staticmethod
    def print_statistics(diary):
        arv, kesk_arv = DiaryStatistics.get_statistics(diary)
        print("sissekannete arv: " + str(arv))
        print("keskmine tähemärkide arv sissekandes: " + str(kesk_arv))