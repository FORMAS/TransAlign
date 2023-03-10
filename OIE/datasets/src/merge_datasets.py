import pathlib
import random


class Merge:
    def __init__(self, datasets: list, output_name: str):
        self.datasets = datasets
        self.merged = ""

        for i in range(len(datasets)):
            with open(datasets[i], "r", encoding="utf-8") as file:
                data = file.read()
                data = data.split("\n\n")
                random.shuffle(data)
                random.shuffle(data)
                random.shuffle(data)
                data = "\n\n".join(data)
                self.merged += data

        path = pathlib.Path("merges")
        path.mkdir(parents=True, exist_ok=True)

        with open(f"merges/{output_name}_corpus.txt", "a", encoding="utf-8") as file:
            file.write(self.merged)

        print(f"len {output_name}: ", len(self.merged.split("\n\n")))

if __name__ == "__main__":
    datasets = ["../outputs/ls_test/ls_test_corpus.txt", "../outputs/ls_dev/ls_dev_corpus.txt", "../splits/pud_200.txt"]
    TEST_SIZE = 0.0
    DEV_SIZE = 0.0
    OUTPUT_NAME = "ls_train_plus"
    IN_PATH = "merges"
    OUT_PATH = "saida_pos_tag"
    Merge(datasets, OUTPUT_NAME)
    #split.train_dev_test(TEST_SIZE, DEV_SIZE, OUTPUT_NAME, IN_PATH, OUT_PATH)